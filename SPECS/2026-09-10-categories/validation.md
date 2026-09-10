# Categories — Validation

Done when all of the following pass.

## Automated checks

1. `python -m unittest` — all tests pass (new + existing, no regressions).
2. `python -m py_compile app.py db.py test_app.py` — no syntax errors.

## Manual checks (on Codio)

3. Recreate the dev database once (`rm freshtrack.db`, then start the server
   so `init_db()` rebuilds it with the `category` column).
4. Add food using the dropdown (try two different categories) — the items
   appear on the list with their categories.
5. The rest of the add-food flow still works (name required, date validated).

## Spec conformance review

6. Compare against `requirements.md`, `plan.md`, and the constitution
   (`SPECS/`). Surface any differences to the user; update specs only after
   approval.

## Merge gate

- Automated checks pass.
- Manual checks pass.
- Differences (if any) approved by the user, then ask for a final sign-off.