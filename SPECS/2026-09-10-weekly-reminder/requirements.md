# Weekly "Use Up" Reminder — Requirements

## Context

The list already shows days-left warnings for every item. This feature adds a
small **reminder panel** at the top of the page: "Use up this week: …" listing
anything that will expire within the next 7 days, so the user knows at a
glance what to plan meals around.

## Scope (what we build)

1. A panel at the top of the page (before the add-food form) titled
   `Use up this week:`.
2. It lists the names of every item expiring within the next **7 days**
   (including today), as plain text.
3. When nothing expires in the window, the panel is hidden — no empty box.
4. A helper `week_items(foods)` filters the food dicts to that window, so the
   logic stays separate from the template.

## Decisions

- **In-app panel only.** Email/SMS is a non-goal; the reminder lives on the
  page.
- Window constant: `REMINDER_DAYS = 7`, one named place to change it.
- Items counted: `0 <= days_left <= 7`. Already-expired items are not "to use
  up" — they are past saving, so they stay out of the panel (the red
  warnings cover them).
- Plain text; no colors, no icons.
- No schema change.

## Out of scope

- Sending reminders anywhere (no email/SMS/notifications).
- Turning the reminder on/off.
- Showing categories in the panel.

## Non-negotiable rules from the constitution

- Simple over clever.
- Test-first (red/green).
- No repeating yourself.
- Easy for a beginner to read.