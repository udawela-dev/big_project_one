# Color-Coded Warnings — Requirements

## Context

Builds on the days-left warnings feature. The page already says "5 days left",
"2 days left — Expiring soon!", and "Expired 3 days ago". Now the message also
gets a color, so a quick glance at the list shows what needs eating first.

## Scope (what we build)

1. Each status message gets one of three colors:
   - **green** — more than 3 days left (safe),
   - **yellow** — expiring soon (3 days or fewer, same threshold as the
     existing warnings),
   - **red** — expires today or already past (includes "Expires today!").
2. A helper `status_color(days)` returns one of `"safe"`, `"soon"`,
   `"expired"` so the template can pick a CSS class. No color printing in
   business logic, just a named bucket.
3. The colors come from a small set of CSS classes in the page styles —
   plain HTML/CSS, no libraries.

## Decisions

- Buckets reuse the existing `EXPIRING_SOON_DAYS = 3` constant (single source
  of truth).
- `days_left` and `status_text` are unchanged — this feature only adds the
  color bucket.
- No schema change.
- Simple logging continues to live on the routes (unchanged from the
  days-left feature).

## Out of scope

- Changing the warning text.
- Choosing colors per category.
- Sorting by color/urgency.

## Non-negotiable rules from the constitution

- Simple over clever.
- Test-first (red/green).
- No repeating yourself.
- Easy for a beginner to read.