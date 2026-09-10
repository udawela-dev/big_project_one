# Add Food — Requirements

## Context

FreshTrack's first working slice (the walking skeleton on the roadmap). This is
the thinnest end-to-end feature: a user opens the page, types a food name and
an expiry date, and the item is saved and shown in the list. Everything else
(days-left warnings, categories, reminders) comes later.

## Scope (what we build)

> **Later note (2026-09-10):** after this feature shipped, later roadmap items
> added a third form field (`category`) and a third database column. They are
> described in `SPECS/2026-09-10-categories/`. The steps below describe the
> original first slice exactly as it was built.

1. A home page that shows a form and the saved food list.
2. The form has two fields: **food name** (text) and **expiry date** (a date
   picker, saved as `YYYY-MM-DD`).
3. Submitting the form saves the item to SQLite and shows the updated list,
   newest item first.
4. Basic validation: empty name is rejected, and the date must be a real
   `YYYY-MM-DD` date. Rejected input shows a friendly message and nothing is
   saved.

## Decisions

- **Plain HTML form + page reload.** No JavaScript fetch. The browser sends a
  normal POST and the page reloads with the new list.
- **SQLite via Python's built-in `sqlite3`.** Single local database file, no
  ORM.
- **Validation lives in Python**, server-side, so it works even with JS off.
- **`unittest` from the Python standard library** for tests — no extra
  packages to install.
- **Schema** (single table):

  ```
  Table: food
  - id:          INTEGER PRIMARY KEY AUTOINCREMENT
  - name:        TEXT     # the name of the food item (required)
  - expiry_date: TEXT     # the date the food expires (YYYY-MM-DD, required)
  ```

  (The `category` column shown in `db.py` today was added later by the
  categories feature — see `SPECS/2026-09-10-categories/`.)

- Sorting newest first uses `ORDER BY id DESC`.

## Out of scope (explicitly not in this feature)

- Days-left / "expiring soon" warnings (next roadmap item).
- Editing or deleting food items.
- Categories, quantities, notes.
- Any JavaScript on the page.
- Logins, exports, notifications (see constitution).

## Non-negotiable rules from the constitution

- Simple over clever.
- Test-first (red/green): write a failing test, then the code to pass it.
- No repeating yourself.
- Code must stay easy for a beginner to read.