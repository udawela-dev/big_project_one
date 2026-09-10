# Dashboard Counts — Plan

Task groups in order, test-first (red/green) for every code group.

## T1 — Dashboard tests

- Tests (RED) in `test_app.py`:
  - the page shows the "Fridge items" and "Pantry items" labels,
  - with 1 fridge item and 2 pantry items, the dashboard reads
    `data-section="fridge">1<` and `data-section="pantry">2<`,
  - with an empty database the dashboard reads `0` for both,
  - after removing an item the dashboard count drops.
- CHECK: the tests fail because the dashboard markup does not exist yet.

## T2 — Dashboard markup

- GREEN: in `templates/index.html`, add the dashboard section under the
  header with three `.stat` boxes:
  - Fridge items → `{{ fridge_foods|length }}`,
  - Pantry items → `{{ pantry_foods|length }}`,
  - Total items → `{{ foods|length }}`.
- Add a few small CSS rules (`.dashboard`, `.stat`, `.stat-count`,
  `.stat-label`) to match the existing card look.
- CHECK: `python -m unittest` — new tests green, all old tests still green.

## T3 — Verification

- `python -m unittest` full suite green; `py_compile` clean.
- Manual: open the public URL and add/remove a couple of items — the dashboard
  numbers change to match the Fridge/Pantry sections below.
- Run the checks in validation.md.