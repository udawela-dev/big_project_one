# Add Food — Validation

This feature is done, and can be merged, when all of the following pass.

## Automated checks

1. Run `python -m unittest` from the project root.
   - Every test passes (red/green discipline: no test was written after its
     code).
2. Run a quick lint on the Python files you added (e.g. `python -m py_compile`
   on each) — no syntax errors.

## Manual checks (on Codio)

3. Start the server bound to `0.0.0.0:3000` and confirm the public URL loads.
4. Add a food item with a valid name and a future date
   (e.g. name "Milk", date `2026-09-20`):
   - the page reloads,
   - "Milk 2026-09-20" appears at the top of the list,
   - the form is empty again.
5. Submit an empty name with a valid date → a friendly message shows, nothing
   is saved.
6. Submit a valid name with a bad date (e.g. `2026-13-40`) → a friendly
   message shows, nothing is saved.
7. Restart the server, reopen the page → "Milk 2026-09-20" is still there
   (SQLite persistence really works).

## Spec conformance review

8. Compare what was built against:
   - this feature spec (`requirements.md`, `plan.md`),
   - the constitution (`SPECS/MISSION.md`, `SPECS/TECH.md`).
9. List any differences to the user and update the specs only after the user
   approves.

## Merge gate

- All automated tests pass.
- All manual checks pass.
- Any spec differences were shown to the user and approved.
- Then ask the user before merging `feature/add-food` into `main`.