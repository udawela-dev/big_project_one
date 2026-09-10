# Edit and Remove — Plan

Work in task groups, in order. For every group that touches code, write the
test first, watch it fail (red), then write the code to pass it (green).

Remember to run the checks (`python -m unittest`) at the end of every group,
and keep all the existing tests green.

## T1 — Database helpers

- Tests (RED) in `test_app.py`:
  - `add_food` then `get_food(id)` returns the same row,
  - `get_food` for a missing id returns `None`,
  - `update_food(id, ...)` changes the row's values,
  - `delete_food(id)` removes the row,
  - `delete_food` leaves other rows alone.
- GREEN: implement `get_food`, `update_food`, `delete_food` in `db.py`.
- CHECK: `python -m unittest` — new tests green, old tests still green.

## T2 — Edit page (GET)

- Test (RED): `GET /edit/<id>` returns the page with the item's current name
  and expiry date filled in.
- GREEN: add the `/edit/<id>` GET route in `app.py` and a small
  `templates/edit.html` prefilled form.
- Also handle a missing item: `GET /edit/<missing>` shows a friendly "not
  found" message (404).
- CHECK: all tests pass.

## T3 — Edit save (POST)

- Tests (RED):
  - a valid POST saves the changes and redirects (302),
  - an empty name is rejected (400) and nothing changes,
  - a bad date is rejected (400),
  - an unknown category is rejected (400).
- GREEN: handle POST in the `/edit/<id>` route with the same validation as
  add-food; on success call `db.update_food` and redirect to the home page; on
  error re-render `edit.html` with a friendly message.
- CHECK: all tests pass.

## T4 — Remove

- Tests (RED):
  - POST `/remove/<id>` deletes the item,
  - it redirects back to the home page (302),
  - other items are left alone.
- GREEN: add the `/remove/<id>` POST route in `app.py` that calls
  `db.delete_food` and redirects home.
- CHECK: all tests pass.

## T5 — Links on the home page + final checks

- Test (RED): the home page shows an **Edit** link and a **Remove** button for
  each item.
- GREEN: add the link and the small remove form to each list item in
  `templates/index.html`.
- Add the two logging lines with the built-in `logging` module (edited food,
  removed food).
- CHECK: `python -m unittest` full suite green; `py_compile` clean.
- Manual: on Codio, edit an item and save, then remove an item — both show up
  on the home page. Run the checks in validation.md.