# Sort by Expiry Date — Validation

Done when all of the following pass.

## Automated checks

1. `python -m unittest` — all tests pass (new + existing, no regressions).
2. `python -m py_compile app.py db.py test_app.py` — no syntax errors.

## Manual checks (on Codio)

3. Open the public URL with at least three items, e.g.:
   - "Milk" expiring in 10 days,
   - "Bread" expiring in 2 days,
   - "Cheese" already expired.
4. The page loads in the default **Newest first** order.
5. Click **Soonest first**:
   - the order becomes Cheese (expired), Bread (2 days), Milk (10 days),
   - the "Soonest first" link is highlighted.
6. Click **Newest first**:
   - the original order returns,
   - the "Newest first" link is highlighted.
7. The add-food form, the warnings, colors, and the weekly reminder all still
   work exactly as before when switching sorts.

## Spec conformance review

8. Compare against `requirements.md`, `plan.md`, and the constitution
   (`SPECS/`). Surface any differences to the user; update specs only after
   approval.

## Merge gate

- Automated checks pass.
- Manual checks pass.
- Differences (if any) approved by the user, then ask for a final sign-off.