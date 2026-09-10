# FreshTrack — Roadmap

## Current state

FreshTrack is a complete web app. A user can add food (name + expiry date +
category), see the list newest-first, and every item shows a color-coded
days-left warning. The list can also be viewed **soonest-first** so the most
urgent items float to the top. There is also a weekly "use up" reminder panel
and full edit/remove support. The database is SQLite; the server runs on Flask.

## Done

1. **Add food** — a form where the user types a food name and its expiry
   date. *(SPECS/2026-09-09-add-food — implemented, tests green)*
2. **View the list** — every added food item is shown on the page. *(came
   with add food)*
3. **Show days-left warnings** — for each item, how many days until it
   expires, flagging items expiring soon (3-day threshold). *(SPECS/
   2026-09-10-days-left-warnings — implemented, tests green)*
4. **Color-coded expiry warnings** (green = fine, yellow = soon, red = past).
   *(SPECS/2026-09-10-color-coded-warnings — implemented, tests green)*
5. **Categories for food** (Dairy, Meat, Veg, Fruit, Pantry, Other).
   *(SPECS/2026-09-10-categories — implemented, tests green)*
6. **Weekly "use up" reminder** — panel listing items expiring within 7
   days. *(SPECS/2026-09-10-weekly-reminder — implemented, tests green)*
7. **Edit and remove** — edit any item's details, or remove it from the
   list. *(SPECS/2026-09-10-edit-and-remove — implemented, tests green)*
8. **Sort by expiry date** — a "Soonest first" view so the most urgent
   items appear at the top (default stays newest-first). *(SPECS/
   2026-09-10-sort-by-expiry — implemented, tests green)*

## Long-term vision (not yet planned)

- Anything that comes next.