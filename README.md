# FreshTrack

> Keep a list of the food you have and when it expires.

Repository: [github.com/udawela-dev/big_project_one](https://github.com/udawela-dev/big_project_one)

FreshTrack is a simple web app that helps you stop wasting food. You keep a
list of the food you own, with its expiry date, so you always know what to eat
before it goes bad.

## The problem it solves

People forget what food they have at home and when it expires. We buy things,
tuck them into the fridge or the pantry, and then lose track — until we find a
mouldy carton at the back and throw it away. A lot of perfectly good food gets
wasted simply because nobody remembers it was there or that it was about to go
off.

## The solution

FreshTrack gives you one simple, always-visible list of everything you own:
the food name, its category, and its expiry date. For every item it shows
how many days are left, colour-coded so the most urgent items catch your eye:

- 🟢 green — plenty of time left
- 🟡 yellow — expiring within 3 days
- 🔴 red — expires today or is already past

There is also a weekly "use up this week" panel, so you know at a glance what
to plan meals around before it spoils.

## Key features

1. **Add food** — type a food name, pick an expiry date, and choose a
   category.
2. **View the list** — every item is shown, newest first.
3. **Days-left warnings** — each item says exactly how many days are left
   ("5 days left", "Expires today!", "Expired 3 days ago").
4. **Colour-coded warnings** — green / yellow / red badges so urgent items
   stand out at a glance.
5. **Categories** — Dairy, Meat, Veg, Fruit, Pantry, and Other.
6. **Weekly "use up" reminder** — a panel listing everything expiring within
   the next 7 days.
7. **Edit and remove** — change an item's details any time, or take it off
   the list once it's been eaten.
8. **Sort by expiry date** — switch from "Newest first" to "Soonest first"
   to float the most urgent items to the top.
9. **Fridge and Pantry sections** — the list is split into two clear
   sections, each with its own count.
10. **Dashboard counts** — at the top, three quick numbers: how many items
    are in the fridge, how many in the pantry, and the total.

Everything is validated server-side: an empty name, an impossible date, or a
category that isn't on the list is caught and shown as a friendly message
instead of being saved.

## Tech stack

- **Backend:** Python with Flask. Flask serves the web pages and handles the
  forms. Run it with one command: `python app.py`.
- **Frontend:** Plain HTML and CSS. No frameworks, no build tools, no
  JavaScript — forms submit normally and the page reloads with the new list.
  (There's a separate edit page, `templates/edit.html`, with the item's
  current details filled in.)
- **Storage:** SQLite, using Python's built-in `sqlite3` module. No ORM, no
  extra packages — the database is just one local file called
  `freshtrack.db`.
- **Tests:** `unittest` from the Python standard library. `python -m unittest`
  runs all 65 tests.
- **Logging:** Python's built-in `logging` module logs when the list is
  viewed and when food is added, edited, or removed.

### How to run it

Make sure Flask is installed, then from this folder:

```
python app.py
```

It serves on port `3000`. On Codio, the page is at
`https://${CODIO_HOSTNAME}-3000.codio.io/` — replace the hostname part with
your box's name.

### How to run the tests

```
python -m unittest
```

## Database design

The database is SQLite and lives in a single file, `freshtrack.db`. It has
one table:

```
Table: food
- id:          INTEGER PRIMARY KEY AUTOINCREMENT
- name:        TEXT     # the name of the food item (required)
- expiry_date: TEXT     # the date the food expires (YYYY-MM-DD, required)
- category:    TEXT     # one of Dairy, Meat, Veg, Fruit, Pantry, Other (default "Other")
```

- Each row is one food item. The `id` is a number SQLite creates for each new
  row, so every item has a unique place to point at (used by the edit and
  remove buttons).
- The expiry date is stored as text in `YYYY-MM-DD` format — the same format an
  `<input type="date">` sends, and it sorts correctly as text. The days-left
  number isn't stored; it's calculated from today's date every time the page
  loads, so it's always fresh.
- Small helper functions in `db.py` are the only place that talks to SQL:
  `add_food`, `all_foods`, `get_food`, `update_food`, and `delete_food`.

## What I learned

Building FreshTrack was my first real web app, and I learned a lot by making
it one small step at a time. Here are the biggest things.

**Working test-first.** Before writing any feature, I wrote a failing test
first. It felt strange at the beginning — why write a test for something that
doesn't exist yet? — but it meant I always knew what "done" looked like, and
when the test went green I had real proof the feature worked. Running the
full test suite after every change caught little mistakes (like a renamed
function or a changed date format) before a user ever saw them.

**Planning in small slices.** The project was built feature by feature, and
each one had its own spec: requirements, a plan, then validation. Starting
with the thinnest thing that worked end-to-end (add food → see it in the
list) and then growing from there beat trying to build everything at once.
When something broke, it was much easier to find the problem because only one
small thing had changed.

**Understanding how the web actually works.** Before this, a web page felt
like magic. Now I get the basic exchange: the browser sends a request (a GET
to view a page, or a POST with form data), Flask's routes decide what to do,
and the server sends back HTML for the browser to draw. Form validation
taught me that you can't trust what the browser sends — it has to be checked
again in Python.

**Reading and writing SQL.** I used SQLite for the first time. Making a table
with `CREATE TABLE`, saving with `INSERT`, reading with `SELECT`, and
updating/deleting rows — these were new ideas, but the pattern is short and
now it doesn't scare me. I also learned to keep all the SQL in one place
(`db.py`) so the rest of the app stays easy to read, and to use `?` placeholders
so the values are escaped safely.

**Sorting and data "on the fly".** The days-left warning is not stored in the
database — it's calculated whenever the page loads. That was a small insight
that saves a lot of bookkeeping: some things are better computed fresh than
saved ahead of time. Sorting by expiry date was also easier than I expected
once I knew the `YYYY-MM-DD` format sorts correctly as text.

**Keeping code simple.** The easiest-to-read solution really is the best
choice for a beginner project. Named constants like `EXPIRING_SOON_DAYS = 3`
made the "magic number" understandable, small helper functions with one job
each made the templates stay almost pure HTML, and boring, obvious code was
still the fastest to debug.

If I kept going, the things I'd want to learn next are: dates in JavaScript
on the client side, saving preferences (like the sort choice) so they survive
a refresh, and maybe adding quantities so the list can track more than one of
the same item. But as a first complete app, FreshTrack showed me how far a
little Python, a handful of routes, and one simple table can go.