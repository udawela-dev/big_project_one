# Edit and Remove — Validation

This feature is done, and can be merged, when all of the following pass.

## Automated checks

1. Run `python -m unittest` from the project root.
   - Every test passes, including all the earlier features (no regressions).
2. Run `python -m py_compile app.py db.py test_app.py` — no syntax errors.

## Manual checks (on Codio)

3. Start the server bound to `0.0.0.0:3000` and open the public URL.
4. Add two items, then:
   - click **Edit** on one of them — the form is filled in with its current
     details,
   - change the name (and optionally the date/category), save — you return to
     the home page and the new details are shown,
   - click **Remove** on the other item — it disappears from the list and the
     page reloads.
5. Try to edit an item with an empty name → a friendly message shows and the
   item is unchanged.
6. Editing an item that no longer exists (e.g. after it was removed) shows a
   friendly "not found" message.
7. Restart the server — edits and removes are persisted (SQLite).

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
- Then ask the user before merging into `main`.