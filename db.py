"""Small helpers for saving food items to SQLite.

The database file lives next to the app and is called freshtrack.db.
Tests point DATABASE at a temporary file instead.
"""

import sqlite3

DATABASE = "freshtrack.db"


def connect(db_path=None):
    """Open a connection to the database file."""
    path = db_path or DATABASE
    return sqlite3.connect(path)


def init_db():
    """Create the food table if it does not exist yet."""
    with connect() as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS food ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "name TEXT NOT NULL, "
            "expiry_date TEXT NOT NULL, "
            "category TEXT NOT NULL DEFAULT 'Other')"
        )


def add_food(name, expiry_date, category="Other"):
    """Save one food item. Returns nothing."""
    with connect() as conn:
        conn.execute(
            "INSERT INTO food (name, expiry_date, category) VALUES (?, ?, ?)",
            (name, expiry_date, category),
        )


def all_foods():
    """Return every food item, newest first."""
    with connect() as conn:
        rows = conn.execute(
            "SELECT id, name, expiry_date, category FROM food "
            "ORDER BY id DESC"
        ).fetchall()
    return rows


def get_food(food_id):
    """Return one food item as a row, or None if it does not exist."""
    with connect() as conn:
        row = conn.execute(
            "SELECT id, name, expiry_date, category FROM food WHERE id = ?",
            (food_id,),
        ).fetchone()
    return row


def delete_food(food_id):
    """Remove one food item. Returns nothing."""
    with connect() as conn:
        conn.execute("DELETE FROM food WHERE id = ?", (food_id,))


def update_food(food_id, name, expiry_date, category):
    """Change one food item's details. Returns nothing."""
    with connect() as conn:
        conn.execute(
            "UPDATE food SET name = ?, expiry_date = ?, category = ? WHERE id = ?",
            (name, expiry_date, category, food_id),
        )