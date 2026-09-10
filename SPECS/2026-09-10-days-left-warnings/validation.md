# Days-Left Warnings — Validation

This feature is done when all of the following pass.

## Automated checks

1. Run `python -m unittest` from the project root.
   - Every test passes, including the existing add-food tests (no
     regression).
2. Run `python -m py_compile app.py db.py test_app.py` — no syntax errors.

## Manual checks (on Codio)

3. Start the server bound to `0.0.0.0:3000` and open the public URL.
4. Add food so the list contains:
   - an item expiring in 5+ days → shows `5 days left` (no warning),
   - an item expiring in exactly 3 days → shows `Expiring soon!`,
   - an item expiring in 2 days → shows `2 days left — Expiring soon!`,
   - an item from 3 days ago → shows `Expired 3 days ago`.
5. Dates past expiry show the *expired* message, never "days left".
6. Restart the server — the items and their warnings are still there.
7. The add-food behavior still works (add an item, it appears at the top of
   the list).

## Logging spot-check

8. Look at the server console/log output: you should see the
   `Viewed food list (N items)` line when the page loads and an
   `Added food: ...` line when you add food.

## Spec conformance review

9. Compare what was built against:
   - this feature spec (`requirements.md`, `plan.md`),
   - the constitution (`SPECS/MISSION.md`, `SPECS/TECH.md`).
10. List any differences to the user and update the specs only after the user
    approves.

## Merge gate

- All automated tests pass.
- All manual checks pass.
- Any spec differences were shown to the user and approved.
- Ask the user before merging (no git is in use right now — just a final
  sign-off).