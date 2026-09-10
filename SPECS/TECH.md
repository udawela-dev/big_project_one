# FreshTrack — Tech

## Stack

- **Backend:** Python with Flask. Flask serves the web pages (simple to run:
  `python app.py`).
- **Frontend:** Plain HTML, CSS, and vanilla JavaScript. No React, no other
  libraries or frameworks.
- **Storage:** SQLite via Python's built-in `sqlite3` module. The food stays
  saved even when the server restarts.

## How the app works

- Flask shows a page where the user adds food.
- Each food item is stored in a SQLite database, with a name and an expiry date.
- Pages are built with regular HTML/CSS; a little vanilla JavaScript makes the
  page feel alive without reloading.

## Engineering standards

### Test-first (red/green)
Write a small failing test first, watch it fail (red), then write the minimal
code to make it pass (green).

### Thinnest working version first
Get one tiny feature working end-to-end before growing the app. Start with
"add food and see it on the list", then add features one at a time.

### Simple over clever
Always pick the easiest-to-read solution, even when a fancier one exists.

### No repeating yourself
If the same code is written twice, pull it into one shared spot.

## Rules for running a server (Codio)

- Bind to `0.0.0.0`, never `127.0.0.1`.
- Use a port in the range 1024–9499. Preferred default: `3000`.
- The public URL is `https://${CODIO_HOSTNAME}-3000.codio.io/`.
- Announce and verify the URL whenever the server starts.