# Color-Coded Warnings — Validation

Done when all of the following pass.

## Automated checks

1. `python -m unittest` — all tests pass (new + existing, no regressions).
2. `python -m py_compile app.py db.py test_app.py` — no syntax errors.

## Manual checks (on Codio)

3. Open the public URL with the demo items:
   - an item with 4+ days left shows its message in **green**,
   - an item with 1–3 days left shows **yellow**,
   - an item expired or expiring today shows **red**.
4. The warning text is unchanged from the days-left feature.

## Spec conformance review

5. Compare against `requirements.md`, `plan.md`, and the constitution
   (`SPECS/`). Surface any differences to the user; update specs only after
   approval.

## Merge gate

- Automated checks pass.
- Manual checks pass.
- Differences (if any) approved by the user, then ask for a final sign-off.