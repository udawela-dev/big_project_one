# Days-Left Warnings — Requirements

## Context

Second feature for FreshTrack, built on top of the add-food feature. The user
can already add food and see the list. Now every item also shows how many days
are left until it expires, and items that are about to go bad are flagged.

## Scope (what we build)

1. Every food item on the page shows its days remaining:
   - more than 3 days → `5 days left`
2. Items that will expire within 3 days are flagged:
   - 1 to 3 days → `2 days left — Expiring soon!`
3. Items expiring today:
   - 0 days → `Expires today!`
4. Items past their date:
   - any past date → `Expired 3 days ago`
5. All of this is **plain text** — no colors in this feature (colors stay in
   the long-term vision).
6. Simple logging on the routes (Python's built-in `logging` module): log
   when the list is viewed and when food is added. Logging lines live away
   from the business logic so the logic stays easy to read.

## Decisions

- **Computed server-side in Python** at render time, not in JavaScript.
- **Threshold: 3 days.** Set once, stored in a named constant so it is easy
  to change later.
- **Schema is unchanged.** No new columns. Days remaining are calculated from
  `expiry_date` on the fly, so all existing rows keep working with no
  migration. (Backward compatibility: keep everything the add-food feature
  already does — nothing is removed or renamed.)
- **Sorting stays newest-first** (`ORDER BY id DESC`). No urgency reordering
  in this feature.
- **Helper functions** with a single job each:
  - `days_left(expiry_date)` — how many days from today until the date,
  - `status_text(days)` — the message for a days number.
- The existing add-food behavior and its tests must stay green.

## Out of scope (explicitly not in this feature)

- Color coding (green/yellow/red).
- Sorting by urgency (most urgent items floating to the top).
- Categories, quantities, notes.
- Editing or deleting items.
- Changing the 3-day threshold from the page.

## Non-negotiable rules from the constitution

- Simple over clever.
- Test-first (red/green).
- No repeating yourself.
- Code must stay easy for a beginner to read.