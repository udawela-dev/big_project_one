# Fridge and Pantry Sections — Requirements

## Context

The list currently shows every food item together under "Your food". A user's
fridge and pantry are different places though: fridge items need eating before
they spoil, while pantry goods last for months. This feature splits the list
into two clear sections so a quick glance shows each place separately.

## Scope (what we build)

1. The home page shows two sections instead of one flat list:
   - **Fridge** — every item whose category is *not* `Pantry`
     (Dairy, Meat, Veg, Fruit, Other).
   - **Pantry** — every item whose category is `Pantry`.
2. Each section is headed by its name and the number of items in it,
   e.g. `Fridge (16)`.
3. A section with no items is **hidden** (no empty box). If both sections are
   empty, the existing "Nothing here yet" message shows.
4. The sort choice (Newest first / Soonest first) applies to **both** sections.
5. Everything else stays the same: add-food form, weekly reminder panel,
   color-coded warnings, edit/remove.

## Decisions

- **Section rule is simple:** `category == "Pantry"` → pantry, everything
  else → fridge. The "Other" category counts as fridge in this feature
  (that is where the seeded items like eggs and sauces live).
- **Computed in `show_page`** from the already-built food dicts; the template
  just renders the two lists. No schema change, no new database work.
- The split happens **after** sorting, so both sections honour the sort.
- The weekly reminder panel is unchanged and covers both places together.

## Out of scope (explicitly not in this feature)

- Sub-sections for each category (no separate Meat/Dairy lists).
- Moving an item between sections by dragging.
- Remembering which section the user was looking at.

## Non-negotiable rules from the constitution

- Simple over clever.
- Test-first (red/green): write a failing test, then the code to pass it.
- No repeating yourself.
- Code must stay easy for a beginner to read.