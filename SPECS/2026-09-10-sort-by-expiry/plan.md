# Sort by Expiry Date — Plan

Task groups in order, test-first (red/green) for every code group.

## T1 — The `sort_foods` helper

- Tests (RED) in `test_app.py` for `sort_foods(foods, sort)`:
  - with `sort="expiry"`, food dicts come back ordered by `expiry_date`
    (earliest date first),
  - with the default (`sort="newest"` or no argument), the list is returned
    unchanged.
- GREEN: implement `sort_foods` in `app.py`.
- CHECK: `python -m unittest` — new tests green, all old tests still green.

## T2 — Route and links

- Tests (RED):
  - the page at `/?sort=expiry` lists the soonest-expiring item before a
    later-expiring one,
  - the default page (`/`) still lists newest-first,
  - the page contains the two links "Newest first" and "Soonest first".
- GREEN:
  - the `index` route reads `request.args.get("sort")` and passes the foods
    through `sort_foods`,
  - the template gains two small sort links above the list, with the active
    one highlighted,
  - pass the current `sort` value into the template.
- CHECK: all tests pass.

## T3 — Verification

- `python -m unittest` full suite green; `py_compile` clean.
- Manual: add items with different expiry dates, open the public URL, click
  "Soonest first" and check the order — then "Newest first" and check it goes
  back.
- Run the checks in validation.md.