# Dashboard Counts — Requirements

## Context

The user wants a quick overview of how much food is left without reading the
whole list. This feature adds a small **dashboard** at the top of the home page
that shows, at a glance, how many items remain in the fridge and how many in
the pantry.

## Scope (what we build)

1. A dashboard strip at the top of the home page (under the header, before the
   weekly reminder and the add-food form) with three numbers:
   - **Fridge items** — count of items whose category is not `Pantry`,
   - **Pantry items** — count of items whose category is `Pantry`,
   - **Total items** — everything added.
2. The numbers come straight from the food list already built for the page —
   no new queries, no schema change.
3. The dashboard updates automatically as items are added, edited, or removed.

## Decisions

- **Same split rule as the Fridge/Pantry sections:** `category == "Pantry"` →
  pantry, everything else → fridge. One source of truth.
- **Plain HTML/CSS**, same card look as the rest of the page. No JavaScript.
- Each number carries `data-section="fridge"` / `data-section="pantry"` /
  `data-section="total"` so tests (and any later styling) can target them.
- Counts are lengths of the lists already passed to the template.

## Out of scope (explicitly not in this feature)

- Charts or graphs.
- Expiry-based stats (e.g. "expiring this week" is already the reminder panel).
- Clicking the dashboard to filter the list.

## Non-negotiable rules from the constitution

- Simple over clever.
- Test-first (red/green): write a failing test, then the code to pass it.
- No repeating yourself.
- Code must stay easy for a beginner to read.