# Weekly "Use Up" Reminder — Validation

Done when all of the following pass.

## Automated checks

1. `python -m unittest` — all tests pass (new + existing, no regressions).
2. `python -m py_compile app.py db.py test_app.py` — no syntax errors.

## Manual checks (on Codio)

3. With the demo items in the database, open the public URL:
   - the panel shows the name of the item expiring within 7 days,
   - the panel does NOT show the already-expired item, nor the one expiring
     in 10 days,
   - when nothing expires within 7 days, no empty panel appears.
4. The warnings feature still works (messages and colors unchanged).

## Spec conformance review

5. Compare against `requirements.md`, `plan.md`, and the constitution
   (`SPECS/`). Surface any differences to the user; update specs only after
   approval.

## Merge gate

- Automated checks pass.
- Manual checks pass.
- Differences (if any) approved by the user, then ask for a final sign-off.