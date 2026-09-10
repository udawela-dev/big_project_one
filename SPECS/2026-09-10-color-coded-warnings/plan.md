# Color-Coded Warnings — Plan

Task groups in order, test-first (red/green) for every code group.

## T1 — The color bucket helper

- Tests (RED) for `status_color(days)`:
  - `status_color(5)` → `"safe"`,
  - `status_color(3)` → `"soon"` (boundary — exactly 3 is expiring soon),
  - `status_color(1)` → `"soon"`,
  - `status_color(0)` → `"expired"`,
  - `status_color(-2)` → `"expired"`.
- GREEN: implement `status_color(days)` in `app.py`.
- CHECK: `python -m unittest` — new tests green, all old tests still green.

## T2 — Colors on the page

- Test (RED): an item expiring in 5 days renders with the `safe` CSS class;
  an item expiring in 2 days with `soon`; an expired item with `expired`.
- GREEN: add `color` to each food dict in `build_foods()`, and use it as a CSS
  class on the status message in `templates/index.html`. Add three small CSS
  rules (green/yellow/red) in a `<style>` block in the page head.
- CHECK: all tests pass.

## T3 — Verification

- `python -m unittest` full suite green; `py_compile` clean.
- Manual: open the public URL, confirm the demo items show in the right
  colors. Run the checks in validation.md.