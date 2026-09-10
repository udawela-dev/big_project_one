# Categories — Requirements

## Context

FreshTrack currently stores `name` and `expiry_date`. This feature adds a
**category** to each food item (dairy, meat, veg, …) so the list is easier to
scan. The category is chosen from a fixed list, not typed freely — that keeps
the data tidy and the validation simple.

## Scope (what we build)

1. A new `category` column on the `food` table, defaulting to `"Other"`.
2. The add-food form gets a dropdown with the fixed list:
   `Dairy, Meat, Veg, Fruit, Cupboard, Other`.
3. Submitting the form saves the chosen category ("Other" if needed).
4. The list shows the category next to each item.
5. Validation: an unknown category value is rejected server-side.

## Decisions

- **Fixed picklist** — a `<select>` in the form and a `CATEGORIES` constant
  in `app.py` as the single source of truth.
- **Backward compatibility — recreate the dev database.** Categories need a
  new column. `CREATE TABLE IF NOT EXISTS` will not add the column to the
  existing file, so `freshtrack.db` is deleted once and recreated by
  `init_db()` on next start. This is a learning project — no important data
  is lost. (This decision was confirmed with the user.)
- `add_food` gains a third parameter `add_food(name, expiry_date,
  category="Other")` so all existing callers and tests keep working unchanged.
- No grouping or filtering by category in this feature — just show it.

## Out of scope

- Grouping the list by category.
- Filtering by category.
- Editing an item's category after adding.
- Free-text categories.

## Non-negotiable rules from the constitution

- Simple over clever.
- Test-first (red/green).
- No repeating yourself.
- Easy for a beginner to read.