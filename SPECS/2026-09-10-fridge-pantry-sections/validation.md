# Fridge and Pantry Sections — Validation

Done when all of the following pass.

## Automated checks

1. `python -m unittest` — all tests pass (new + existing, no regressions).
2. `python -m py_compile app.py db.py test_app.py` — no syntax errors.

## Manual checks (on Codio)

3. Open the public URL with seeded data:
   - a **Fridge** section shows the fridge items (Dairy, Meat, Veg, Fruit,
     Other) with a count,
   - a **Pantry** section shows the pantry items with a count,
   - no item appears in the wrong section.
4. Switch between **Newest first** and **Soonest first** — both sections
   re-order but the two sections stay separate.
5. With a fridge-only or pantry-only database, the empty section heading is
   hidden and only the populated section shows.
6. The add-food form, weekly reminder, warnings, and edit/remove all still
   work.

## Spec conformance review

7. Compare against `requirements.md`, `plan.md`, and the constitution
   (`SPECS/`). Surface any differences to the user; update specs only after
   approval.

## Merge gate

- Automated checks pass.
- Manual checks pass.
- Differences (if any) approved by the user, then ask for a final sign-off.