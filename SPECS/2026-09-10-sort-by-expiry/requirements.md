# Sort by Expiry Date — Requirements

## Context

The list has always shown items newest-first (the order they were added).
Users still need a quick glance at what is *about to go off* — that is why the
days-left warnings and the weekly reminder exist. This feature adds a second
way to view the list: **soonest expiry first**, so the most urgent items float
to the top.

## Scope (what we build)

1. Two sort choices above the list:
   - **Newest first** — the original ordering (most recently added at the
     top). This stays the default.
   - **Soonest first** — items ordered by expiry date, earliest date first
     (including already-expired items, which have the earliest dates).
2. A click switches the list and highlights the active choice.
3. A helper `sort_foods(foods, sort)` does the ordering, keeping the logic
   away from the template.
4. The rest of the page (add form, warnings, weekly reminder) behaves exactly
   as before.

## Decisions

- **Default stays newest-first.** The add-food feature promised "newest item
  first", and existing tests rely on it — so the new order is opt-in via
  `?sort=expiry`.
- **Sort key is the `expiry_date` string** (`YYYY-MM-DD` sorts correctly as
  text), so `sort_foods` stays simple and beginner-friendly.
- **No schema change.**
- **No persistence of the choice** — no cookies or saved preference. Refreshing
  without `?sort=expiry` shows the default order. (Keeps it simple; students
  have not learned cookies.)
- Expired items appear at the top in soonest-first view because their dates are
  earliest — prompt attention (or disposal) for the most urgent rows.

## Out of scope (explicitly not in this feature)

- Sorting by category or by name.
- A dropdown-style sort selector.
- Remembering the user's sort choice between visits.
- Changing the default newest-first ordering.

## Non-negotiable rules from the constitution

- Simple over clever.
- Test-first (red/green): write a failing test, then the code to pass it.
- No repeating yourself.
- Code must stay easy for a beginner to read.