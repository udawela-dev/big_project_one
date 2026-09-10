# Categories — Plan

Task groups in order, test-first (red/green).

## T1 — Database: category column

- Tests (RED):
  - the `food` table has a `category` column,
  - `add_food("Milk", "2026-09-20", "Dairy")` saves the category,
  - `add_food("Bread", "2026-09-20")` defaults to `"Other"`,
  - `all_foods()` returns the category too.
- GREEN:
  - update the `CREATE TABLE` statement in `db.py` with
    `category TEXT NOT NULL DEFAULT 'Other'`,
  - extend `add_food` with the `category="Other"` parameter,
  - extend `all_foods` to select the category.
- CHECK: `python -m unittest` — new tests green, all old tests green.
- NOTE for the developer: the dev DB must be recreated once
  (`rm freshtrack.db`) so the table gets the new column.

## T2 — Form and validation

- Tests (RED):
  - POST with a valid category (`Dairy`) saves and shows it,
  - POST with an unknown category (`"Snacks"`) is rejected with a 400,
  - POST without a category still works → becomes `"Other"`.
- GREEN:
  - add `CATEGORIES` constant in `app.py`,
  - validate the category in the `/add` route,
  - pass `category` through to `db.add_food`,
  - update `build_foods()` to include the category,
  - template: add the `<select>` to the form and show the category in each
    list item.
- CHECK: all tests pass.

## T3 — Verification

- Recreate the dev DB, run `python -m unittest` (full suite green),
  `py_compile` clean.
- Manual: add food with different categories via the public URL and check
  they appear on the list.
- Run the checks in validation.md.