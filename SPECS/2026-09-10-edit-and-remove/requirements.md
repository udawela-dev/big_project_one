# Edit and Remove — Requirements

## Context

FreshTrack already lets the user add food (name, expiry date, category) and see
the list. Sometimes an item's details change, or an item has been eaten and
should leave the list. This feature adds **editing** (change any item's details)
and **removing** (take an item off the list).

## Scope (what we build)

1. Every food item on the home page has an **Edit** link and a **Remove**
   button.
2. Clicking **Edit** opens a page at `/edit/<id>` with the item's current
   details filled in (name, expiry date, category).
3. Saving the edit updates the item and sends the user back to the home page.
4. The same validation rules as add-food apply on save:
   - name is required (stripped, not empty),
   - date must be a real `YYYY-MM-DD` date,
   - category must be one of the fixed `CATEGORIES`.
   A problem shows a friendly message and nothing is saved.
5. Editing an item that no longer exists shows a friendly "not found" message.
6. Clicking **Remove** deletes the item and sends the user back to the home
   page.

## Decisions

- **Plain HTML forms + page reload.** Same pattern as add-food: no JavaScript
  fetch.
- **Validation lives in Python**, exactly like the add-food route.
- **Remove is a small POST form**, not a link — so a stray refresh or
  pre-fetch can never delete an item by accident.
- **Database helpers** in `db.py`, each with one job:
  - `get_food(food_id)` — one item as a row, or `None`,
  - `update_food(food_id, name, expiry_date, category)` — save changes,
  - `delete_food(food_id)` — remove the item.
- **Separate edit template** (`templates/edit.html`) with a form that posts
  back to `/edit/<id>`.
- No schema change — this feature only reads and changes existing rows.
- Simple logging stays on the routes (consistent with the earlier features):
  log with the built-in `logging` module when an item is edited or removed.

## Out of scope (explicitly not in this feature)

- Undo for a remove.
- A confirmation pop-up before removing.
- Deleting several items at once.
- Quantities, notes, or any new data fields.

## Non-negotiable rules from the constitution

- Simple over clever.
- Test-first (red/green): write a failing test, then the code to pass it.
- No repeating yourself.
- Code must stay easy for a beginner to read.