# Project Brainstorming

## Idea 1
- **Problem:Finding Lost Digital Information**
- **Who experiences this:Students, office workers, researchers, and anyone who regularly uses multiple digital devices and apps.**
- **Why it matters:People waste time searching through different apps and folders, may lose important information, and sometimes repeat work because they cannot find something they previously saved.**

## Idea 2
- **Problem:Drivers often spend a lot of time looking for available parking, especially near shopping centres, universities, workplaces, and busy areas.**
- **Who experiences this:Drivers, students, workers, and visitors.**
- **Why it matters:It wastes time, increases frustration, and can cause people to arrive late.**

## Idea 3
- **Problem:*Reducing food waste, People forget what food they have at home and when it expires.*
- **Who experiences this:Families, students, and households.**
- **Why it matters:Large amounts of usable food are thrown away unnecessarily.**

---

## Selected Project
- **App Name:** FreshTrack
- **Target User:** Students, families, and households who want to stop wasting food.
- **Core Problem:** People forget what food they have and when it expires, so usable food gets thrown away.
- **Purpose:** Let users keep a simple list of the food they own (with expiry dates) so they always know what to eat before it goes bad.

---

## Core Requirements
- Add food: the user types a food name and its expiry date.
- View the list: every added food item is shown on the page.
- Days-left warnings: show how many days until each item expires, and flag items that are expiring soon.

---

## Non-Goals
- No accounts or logins.
- No linking to shops or online stores.
- No user registration or login system (single-user local application).
- No mobile app or responsive mobile framework.
- No email or SMS notifications.
- No third-party API integrations.
- No export functionality (PDF, CSV, etc.).

---

## Database Questions

For each core requirement, write the specific question the database must be able to answer to make it work, plus the query that answers it.

- Requirement 1 → Which food items has the user added (name + expiry date)?
  `SELECT name, expiry_date FROM food;`
- Requirement 2 → How do I show every food item, newest or oldest first?
  `SELECT * FROM food ORDER BY id DESC;` (newest first) or `ASC` (oldest first)
- Requirement 3 → Which items expire soon (within X days) or are already past their date?
  `SELECT * FROM food WHERE expiry_date <= date('now', '+3 days');`

---

## Schema

```
Table: food
- id:          INTEGER PRIMARY KEY AUTOINCREMENT
- name:        TEXT     # the name of the food item (required)
- expiry_date: TEXT     # the date the food expires (YYYY-MM-DD, required)
```

