# Add Food — Plan

Work in task groups, in order. For each group that touches code, write the
test first, watch it fail (red), then write the code to pass it (green).

Remember to run the checks (`python -m unittest` for tests) at the end of
every group.

## T1 — Project scaffolding

- Create a minimal Flask `app.py` with one home route that returns a "Hello"
  page (temporary).
- Create `test_app.py` with one test: the home page returns a 200 OK.
- RED: the test fails because `app.py` isn't there yet.
- GREEN: make it pass.
- CHECK: `python -m unittest` passes.

## T2 — Database layer

- Create `db.py` with:
  - a `connect()` helper that opens the database file,
  - an `init_db()` that creates the `food` table if it does not exist,
  - helper functions `add_food(name, expiry_date)` and `all_foods()`.
- Write tests BEFORE the helpers exist (RED):
  - adding a food increases the row count,
  - `all_foods()` returns saved items,
  - `all_foods()` returns newest first (`ORDER BY id DESC`).
- GREEN: implement the helpers.
- CHECK: tests pass. A `freshtrack.db` file is created on first run (add it to
  `.gitignore`).

## T3 — Add-food route with validation

- Home route now renders a form plus the food list.
- New route handles the POST:
  - name is stripped and must not be empty,
  - date must match `YYYY-MM-DD` and be a real calendar date,
  - on error, re-render the page with a friendly message and nothing saved,
  - on success, save and redirect back to the list (redirect-after-post).
- Tests BEFORE the code (RED):
  - empty name → rejected, nothing added,
  - impossible date (e.g. `2026-13-40`) → rejected,
  - valid submission → item saved and shown on the page.
- GREEN: implement.
- CHECK: all tests pass.

## T4 — Template and page

- Split the HTML into `templates/index.html` (Flask's `render_template`).
- Show the list newest first, with name and expiry date.
- Show the friendly error message when present.
- CHECK: tests still pass.

## T5 — End-to-end verification (manual)

- Run the server bound to `0.0.0.0:3000`.
- Open the Codio public URL, add a real item, watch it appear (feature spec
  validation.md has the exact steps).
- CHECK: manual checks from validation.md all pass.

## Notes for later features

- Validate a fresh database on each server start with `init_db()`.
- Keep tests fast: point tests at a temporary database file, not the real one.