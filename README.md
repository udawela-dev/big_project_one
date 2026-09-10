# FreshTrack

FreshTrack is a simple web app that helps you stop wasting food. You keep a
list of the food you own, with its expiry date, so you always know what to eat
before it goes bad.

## What it is built with

- Python with Flask (backend)
- HTML, CSS, and vanilla JavaScript (frontend)
- SQLite via Python's built-in `sqlite3` module — food stays saved across restarts

## How to run it

Make sure Flask is installed, then from this folder:

```
python app.py
```

It serves on port `3000`. On Codio, the page is at
`https://${CODIO_HOSTNAME}-3000.codio.io/` — replace the hostname part with
your box's name.

## Where to find things

- `SPECS/MISSION.md` — the project's purpose and values
- `SPECS/TECH.md` — the tech stack and engineering standards
- `SPECS/ROADMAP.md` — current state, next steps, long-term vision
- `design.md` — the original brainstorming and selected project