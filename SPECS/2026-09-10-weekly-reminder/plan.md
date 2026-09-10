# Weekly "Use Up" Reminder — Plan

Task groups in order, test-first (red/green).

## T1 — The `week_items` filter

- Tests (RED) for `week_items(foods)`, using food dicts with known
  `days_left` values:
  - keeps an item with 6 days left,
  - keeps an item expiring today (0 days left),
  - drops an expired item (−2 days),
  - drops an item 8 days out (outside the window) — boundary check for the
    constant,
  - keeps an item at exactly `REMINDER_DAYS` (7) — boundary.
- GREEN: implement `week_items(foods)` and `REMINDER_DAYS = 7` in `app.py`.
- CHECK: both `status_text`/`days_left` and the new tests pass.

## T2 — The panel on the page

- Test (RED): seed an item expiring in 3 days → the page contains
  `Use up this week:` and the item's name. Seed only a safe item (5 days left,
  no — use 10 days) and an expired item → the panel is absent.
- GREEN: in the `index` route, compute `week_items(foods)` and pass it to the
  template; add the panel markup at the top of `templates/index.html`,
  wrapped in `{% if week_items %}` … `{% endif %}`.
- CHECK: all tests pass.

## T3 — Verification

- `python -m unittest` full suite green; `py_compile` clean.
- Manual: with demo data (a 2-day item and a 10-day item) the panel lists only
  the 2-day item; open the public URL to confirm.
- Run the checks in validation.md.