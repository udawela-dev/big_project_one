# Days-Left Warnings — Plan

Work in task groups, in order. For each group that touches code, write the
test first, watch it fail (red), then write the code to pass it (green).

Remember to run the checks (`python -m unittest`) at the end of every group,
and make sure the existing add-food tests still pass too.

## T1 — Days math and status text (pure functions)

- Add tests to `test_app.py` for:
  - `days_left("2026-09-15")` vs today (use `date.today()` in the test, so it
    never goes stale),
  - `days_left` for a past date gives a negative number,
  - `status_text(5)` → `5 days left`,
  - `status_text(2)` → `2 days left — Expiring soon!`,
  - `status_text(0)` → `Expires today!`,
  - `status_text(-3)` → `Expired 3 days ago`,
  - exactly 3 days left → flagged as expiring soon (boundary case).
- RED: functions don't exist yet.
- GREEN: implement `days_left(expiry_date)` and `status_text(days)` in
  `app.py`, plus the `EXPIRING_SOON_DAYS = 3` constant.
- CHECK: `python -m unittest` — new tests pass, old ones still pass.

## T2 — Show the warnings on the page

- Tests (RED) seeded through `db.add_food`:
  - an item expiring in 5 days shows `5 days left`,
  - an item expiring in 2 days shows `Expiring soon`,
  - an item from 3 days ago shows `Expired 3 days ago`.
- GREEN: in the route, compute days and status for each item and pass them to
  the template; update `templates/index.html` to print the status text under
  each item.
- CHECK: all tests pass.

## T3 — Simple logging

- Add one `logging` configuration line in `app.py` (`logging.basicConfig`).
- Log one line per request that matters:
  - viewing the list → `Viewed food list (N items)`,
  - adding food → `Added food: <name> (<expiry_date>)`. (After the categories
    feature landed, the message gained the category:
    `Added food: Milk (2026-09-20, Dairy)`.)
- No tests for logging itself; just keep the whole suite green.
- CHECK: `python -m unittest` still passes.

## T4 — End-to-end verification (manual)

- Seed a few items, including one within 3 days and one past date.
- Open the Codio public URL and confirm the messages look right.
- Restart the server and confirm items and warnings are still there.
- CHECK: manual checks from validation.md all pass.

## Notes for later features

- If urgency sorting ever comes, `days_left` is ready to be reused.
- The `EXPIRING_SOON_DAYS` constant is the single place to change the
  threshold.