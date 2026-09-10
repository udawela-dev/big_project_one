# Dashboard Counts — Validation

Done when all of the following pass.

## Automated checks

1. `python -m unittest` — all tests pass (new + existing, no regressions).
2. `python -m py_compile app.py db.py test_app.py` — no syntax errors.

## Manual checks (on Codio)

3. Open the public URL with the seeded fridge and pantry items:
   - the dashboard shows the same Fridge count as the Fridge section heading,
   - the dashboard shows the same Pantry count as the Pantry section heading,
   - the Total matches the sum.
4. Add a new item → the dashboard number for that side goes up by one.
5. Remove an item → the corresponding dashboard number goes down by one.
6. The rest of the page (reminder, sort, edit/remove) still works.

## Spec conformance review

7. Compare against `requirements.md`, `plan.md`, and the constitution
   (`SPECS/`). Surface any differences to the user; update specs only after
   approval.

## Merge gate

- Automated checks pass.
- Manual checks pass.
- Differences (if any) approved by the user, then ask for a final sign-off.