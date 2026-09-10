# Fridge and Pantry Sections — Plan

Task groups in order, test-first (red/green) for every code group.

## T1 — Split the list in the route

- Tests (RED) in `test_app.py`:
  - the page shows a `Fridge (n)` heading and a `Pantry (n)` heading,
  - a fridge item (e.g. Dairy) appears between the Fridge heading and the
    Pantry heading,
  - a pantry item appears after the Pantry heading,
  - when there are no fridge items, the Fridge heading is hidden,
  - section counts are shown, e.g. `Fridge (1)` and `Pantry (1)`.
- GREEN: in `show_page`, build `fridge_foods` (category != "Pantry") and
  `pantry_foods` (category == "Pantry") and pass them to the template.
- CHECK: `python -m unittest` — new tests green, all old tests still green.

## T2 — Two sections in the template

- GREEN: in `templates/index.html`, loop over a small list of
  `[("Fridge", fridge_foods), ("Pantry", pantry_foods)]` and render the
  existing food-item markup under each section heading. Hide a section when it
  is empty; show the empty-state box only when both are empty.
- CHECK: all tests pass.

## T3 — Verification

- `python -m unittest` full suite green; `py_compile` clean.
- Manual: open the public URL and confirm the seeded fridge and pantry items
  appear in their own sections, with counts and working sort links.
- Run the checks in validation.md.