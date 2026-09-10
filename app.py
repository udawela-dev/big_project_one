import os
from datetime import date, datetime
import logging
import re

from flask import Flask, redirect, render_template, request, url_for

import db

app = Flask(__name__)

EXPIRING_SOON_DAYS = 3
REMINDER_DAYS = 7
CATEGORIES = [
    "Dairy",
    "Meat",
    "Veg",
    "Fruit",
    "Pantry",
    "Other",
]

PORT = 3000
HOSTNAME = os.environ.get("CODIO_HOSTNAME")
PUBLIC_URL = f"https://{HOSTNAME}-{PORT}.codio.io/" if HOSTNAME else f"http://localhost:{PORT}/"


def days_left(expiry_date):
    """Whole days from today until expiry_date (negative = already expired)."""
    expiry = datetime.strptime(expiry_date, "%Y-%m-%d").date()
    return (expiry - date.today()).days


def status_text(days):
    """The warning message for a given number of days until expiry."""
    if days < 0:
        days_ago = -days
        suffix = "day" if days_ago == 1 else "days"
        return f"Expired {days_ago} {suffix} ago"
    if days == 0:
        return "Expires today!"
    suffix = "day" if days == 1 else "days"
    if days <= EXPIRING_SOON_DAYS:
        return f"{days} {suffix} left — Expiring soon!"
    return f"{days} {suffix} left"


def status_color(days):
    """The color bucket for a given number of days until expiry."""
    if days < 0:
        return "expired"
    if days == 0:
        return "expired"
    if days <= EXPIRING_SOON_DAYS:
        return "soon"
    return "safe"


def valid_date(value):
    """True only when value looks like a real calendar date (YYYY-MM-DD)."""
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def build_foods():
    """A list of food dicts, each with its days left and status message."""
    foods = []
    for item_id, name, expiry_date, category in db.all_foods():
        days = days_left(expiry_date)
        foods.append(
            {
                "id": item_id,
                "name": name,
                "expiry_date": expiry_date,
                "category": category,
                "days_left": days,
                "status": status_text(days),
                "color": status_color(days),
            }
        )
    return foods


def week_items(foods):
    """Food dicts to use up this week: expiring within REMINDER_DAYS days."""
    return [
        food for food in foods
        if 0 <= food["days_left"] <= REMINDER_DAYS
    ]


def sort_foods(foods, sort="newest"):
    """Return foods in the requested order.

    "newest" keeps the list in the order it was added (newest first).
    "expiry" sorts by expiry date, soonest (earliest date) first.
    """
    if sort == "expiry":
        return sorted(foods, key=lambda food: food["expiry_date"])
    return foods


def show_page(error=None, status=200, foods=None, added=None, sort="newest"):
    """Render the home page with the food list and an optional message."""
    if foods is None:
        foods = sort_foods(build_foods(), sort)
    fridge_foods = [food for food in foods if food["category"] != "Pantry"]
    pantry_foods = [food for food in foods if food["category"] == "Pantry"]
    return render_template(
        "index.html",
        foods=foods,
        fridge_foods=fridge_foods,
        pantry_foods=pantry_foods,
        week_items=week_items(foods),
        error=error,
        added=added,
        categories=CATEGORIES,
        sort=sort,
    ), status


@app.route("/")
def index():
    sort = request.args.get("sort", "newest")
    foods = sort_foods(build_foods(), sort)
    app.logger.info(f"Viewed food list ({len(foods)} items)")
    return show_page(foods=foods, added=request.args.get("added"), sort=sort)


@app.route("/add", methods=["POST"])
def add():
    sort = request.args.get("sort", "newest")
    name = request.form.get("name", "").strip()
    expiry_date = request.form.get("expiry_date", "").strip()
    category = request.form.get("category", "Other")

    if not name:
        return show_page("Please enter a food name.", status=400, sort=sort)

    if not valid_date(expiry_date):
        return show_page("Please enter a valid date (YYYY-MM-DD).", status=400, sort=sort)

    if category not in CATEGORIES:
        return show_page("Please pick a category from the list.", status=400, sort=sort)

    db.add_food(name, expiry_date, category)
    app.logger.info(f"Added food: {name} ({expiry_date}, {category})")
    return redirect(url_for("index", added=name))


@app.route("/edit/<int:food_id>", methods=["GET", "POST"])
def edit(food_id):
    food = db.get_food(food_id)
    if food is None:
        return show_page("That item is no longer there.", status=404)

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        expiry_date = request.form.get("expiry_date", "").strip()
        category = request.form.get("category", "Other")

        if not name:
            return render_edit(food_id, food, "Please enter a food name.", 400)
        if not valid_date(expiry_date):
            return render_edit(food_id, food, "Please enter a valid date (YYYY-MM-DD).", 400)
        if category not in CATEGORIES:
            return render_edit(food_id, food, "Please pick a category from the list.", 400)

        db.update_food(food_id, name, expiry_date, category)
        app.logger.info(f"Edited food: {food_id} -> {name} ({expiry_date}, {category})")
        return redirect(url_for("index"))

    return render_edit(food_id, food)


def render_edit(food_id, food, error=None, status=200):
    """Render the edit page with the item's current details filled in."""
    return render_template(
        "edit.html",
        food_id=food_id,
        food={
            "id": food[0],
            "name": food[1],
            "expiry_date": food[2],
            "category": food[3],
        },
        error=error,
        categories=CATEGORIES,
    ), status


@app.route("/remove/<int:food_id>", methods=["POST"])
def remove(food_id):
    db.delete_food(food_id)
    app.logger.info(f"Removed food: id {food_id}")
    return redirect(url_for("index"))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    db.init_db()
    app.run(host="0.0.0.0", port=PORT)