import os
import tempfile
import unittest
from datetime import date, timedelta

import db
from app import (
    REMINDER_DAYS,
    app,
    days_left,
    sort_foods,
    status_color,
    status_text,
    week_items,
)


class FreshTrackTests(unittest.TestCase):
    """Shared setup: every test uses its own throwaway database file."""

    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        db.DATABASE = os.path.join(self.tmp_dir.name, "test.db")
        db.init_db()
        self.client = app.test_client()

    def tearDown(self):
        self.tmp_dir.cleanup()


class IndexPageTests(FreshTrackTests):
    """Tests for the home page (T1)."""

    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class DatabaseTests(FreshTrackTests):
    """Tests for the database helpers in db.py (T2)."""

    def test_init_db_creates_food_table(self):
        db.connect().execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='food'"
        ).fetchone()
        # If the table is missing, the line above raises an error and the
        # test fails. So reaching this point means the table exists.
        self.assertTrue(True)

    def test_add_food_saves_a_row(self):
        db.add_food("Milk", "2026-09-20")
        rows = db.all_foods()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1], "Milk")
        self.assertEqual(rows[0][2], "2026-09-20")

    def test_all_foods_returns_newest_first(self):
        db.add_food("Bread", "2026-09-15")
        db.add_food("Cheese", "2026-09-30")
        rows = db.all_foods()
        self.assertEqual(rows[0][1], "Cheese")
        self.assertEqual(rows[1][1], "Bread")


class AddFoodTests(FreshTrackTests):
    """Tests for the add-food form (T3)."""

    def test_empty_name_is_rejected(self):
        response = self.client.post(
            "/add", data={"name": "   ", "expiry_date": "2026-09-20"}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(db.all_foods()), 0)

    def test_impossible_date_is_rejected(self):
        response = self.client.post(
            "/add", data={"name": "Milk", "expiry_date": "2026-13-40"}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(db.all_foods()), 0)

    def test_wrong_date_format_is_rejected(self):
        response = self.client.post(
            "/add", data={"name": "Milk", "expiry_date": "20/09/2026"}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(db.all_foods()), 0)

    def test_valid_submission_is_saved_and_redirects(self):
        response = self.client.post(
            "/add", data={"name": "Milk", "expiry_date": "2026-09-20"}
        )
        self.assertEqual(response.status_code, 302)
        rows = db.all_foods()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1], "Milk")

        page = self.client.get("/")
        self.assertIn("Milk", page.get_data(as_text=True))

    def test_success_message_shows_and_list_is_updated(self):
        response = self.client.post(
            "/add",
            data={"name": "Milk", "expiry_date": "2026-09-20"},
            follow_redirects=True,
        )
        page = response.get_data(as_text=True)
        self.assertIn("was added to your list", page)
        self.assertIn('<li class="food-item">', page)
        self.assertIn("Milk", page)


class DaysLeftTests(FreshTrackTests):
    """Tests for the days-left helpers (T1)."""

    @staticmethod
    def in_days(n):
        """A date n days from today, as YYYY-MM-DD."""
        return (date.today() + timedelta(days=n)).isoformat()

    def test_days_left_for_a_future_date(self):
        self.assertEqual(days_left(self.in_days(5)), 5)

    def test_days_left_for_a_past_date_is_negative(self):
        self.assertEqual(days_left(self.in_days(-3)), -3)

    def test_status_text_many_days_left(self):
        self.assertEqual(status_text(5), "5 days left")

    def test_status_text_expiring_soon(self):
        self.assertEqual(status_text(2), "2 days left — Expiring soon!")

    def test_status_text_exactly_three_days_is_expiring_soon(self):
        self.assertEqual(status_text(3), "3 days left — Expiring soon!")

    def test_status_text_today(self):
        self.assertEqual(status_text(0), "Expires today!")

    def test_status_text_expired(self):
        self.assertEqual(status_text(-3), "Expired 3 days ago")


class WarningDisplayTests(FreshTrackTests):
    """Tests for the warnings shown on the page (T2)."""

    @staticmethod
    def in_days(n):
        return (date.today() + timedelta(days=n)).isoformat()

    def test_page_shows_days_left(self):
        db.add_food("Milk", self.in_days(5))
        page = self.client.get("/").get_data(as_text=True)
        self.assertIn("5 days left", page)

    def test_page_flags_expiring_soon(self):
        db.add_food("Yogurt", self.in_days(2))
        page = self.client.get("/").get_data(as_text=True)
        self.assertIn("Expiring soon", page)

    def test_page_shows_expired(self):
        db.add_food("Old Bread", self.in_days(-3))
        page = self.client.get("/").get_data(as_text=True)
        self.assertIn("Expired 3 days ago", page)


class StatusColorTests(FreshTrackTests):
    """Tests for the status_color helper (color-coded warnings T1)."""

    def test_far_off_is_safe(self):
        self.assertEqual(status_color(5), "safe")

    def test_exactly_three_days_is_soon(self):
        self.assertEqual(status_color(3), "soon")

    def test_one_day_is_soon(self):
        self.assertEqual(status_color(1), "soon")

    def test_today_is_expired(self):
        self.assertEqual(status_color(0), "expired")

    def test_past_date_is_expired(self):
        self.assertEqual(status_color(-2), "expired")


class ColorDisplayTests(FreshTrackTests):
    """Tests for the colors shown on the page (color-coded warnings T2)."""

    @staticmethod
    def in_days(n):
        return (date.today() + timedelta(days=n)).isoformat()

    def test_safe_item_uses_safe_class(self):
        db.add_food("Milk", self.in_days(5))
        page = self.client.get("/").get_data(as_text=True)
        self.assertIn('class="badge status-safe"', page)

    def test_soon_item_uses_soon_class(self):
        db.add_food("Yogurt", self.in_days(2))
        page = self.client.get("/").get_data(as_text=True)
        self.assertIn('class="badge status-soon"', page)

    def test_expired_item_uses_expired_class(self):
        db.add_food("Old Bread", self.in_days(-3))
        page = self.client.get("/").get_data(as_text=True)
        self.assertIn('class="badge status-expired"', page)


class CategoryDbTests(FreshTrackTests):
    """Tests for the category column (categories T1)."""

    def test_add_food_with_category_saves_it(self):
        db.add_food("Milk", "2026-09-20", "Dairy")
        rows = db.all_foods()
        self.assertEqual(rows[0][3], "Dairy")

    def test_add_food_defaults_to_other(self):
        db.add_food("Bread", "2026-09-20")
        rows = db.all_foods()
        self.assertEqual(rows[0][3], "Other")

    def test_all_foods_returns_category(self):
        db.add_food("Cheese", "2026-09-20", "Dairy")
        rows = db.all_foods()
        self.assertEqual(len(rows[0]), 4)


class CategoryFormTests(FreshTrackTests):
    """Tests for the category dropdown (categories T2)."""

    @staticmethod
    def in_days(n):
        return (date.today() + timedelta(days=n)).isoformat()

    def test_valid_category_is_saved_and_shown(self):
        self.client.post(
            "/add",
            data={
                "name": "Milk",
                "expiry_date": self.in_days(5),
                "category": "Dairy",
            },
        )
        rows = db.all_foods()
        self.assertEqual(rows[0][3], "Dairy")
        page = self.client.get("/").get_data(as_text=True)
        self.assertIn("Dairy", page)

    def test_unknown_category_is_rejected(self):
        response = self.client.post(
            "/add",
            data={
                "name": "Candy",
                "expiry_date": self.in_days(5),
                "category": "MadeUp",
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(db.all_foods()), 0)

    def test_missing_category_defaults_to_other(self):
        self.client.post(
            "/add",
            data={"name": "Bread", "expiry_date": self.in_days(5)},
        )
        rows = db.all_foods()
        self.assertEqual(rows[0][3], "Other")

    def test_cupboard_category_is_rejected(self):
        response = self.client.post(
            "/add",
            data={
                "name": "Biscuits",
                "expiry_date": self.in_days(30),
                "category": "Cupboard",
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(db.all_foods()), 0)

    def test_pantry_category_is_saved(self):
        response = self.client.post(
            "/add",
            data={
                "name": "Pasta",
                "expiry_date": self.in_days(300),
                "category": "Pantry",
            },
        )
        self.assertEqual(response.status_code, 302)
        rows = db.all_foods()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][3], "Pantry")


class WeeklyReminderTests(FreshTrackTests):
    """Tests for the week_items filter (weekly reminder T1)."""

    @staticmethod
    def food(name, days):
        """A food dict with the given number of days until expiry."""
        return {"name": name, "days_left": days}

    def test_keeps_item_with_six_days_left(self):
        self.assertEqual(
            week_items([self.food("Milk", 6)]), [self.food("Milk", 6)]
        )

    def test_keeps_item_expiring_today(self):
        self.assertEqual(
            week_items([self.food("Yogurt", 0)]), [self.food("Yogurt", 0)]
        )

    def test_drops_expired_item(self):
        self.assertEqual(week_items([self.food("Old Bread", -2)]), [])

    def test_drops_item_eight_days_out(self):
        self.assertEqual(week_items([self.food("Cheese", 8)]), [])

    def test_keeps_item_exactly_at_reminder_days(self):
        self.assertEqual(
            week_items([self.food("Apples", REMINDER_DAYS)]),
            [self.food("Apples", REMINDER_DAYS)],
        )


class ReminderPanelTests(FreshTrackTests):
    """Tests for the reminder panel on the page (weekly reminder T2)."""

    @staticmethod
    def in_days(n):
        return (date.today() + timedelta(days=n)).isoformat()

    def test_panel_shows_item_expiring_this_week(self):
        db.add_food("Yogurt", self.in_days(3))
        page = self.client.get("/").get_data(as_text=True)
        self.assertIn("Use up this week:", page)
        self.assertIn("Yogurt", page)

    def test_panel_absent_when_nothing_expires_soon(self):
        db.add_food("Milk", self.in_days(10))
        page = self.client.get("/").get_data(as_text=True)
        self.assertNotIn("Use up this week:", page)


class RemoveItemTests(FreshTrackTests):
    """Tests for removing a food item."""

    def add_one(self, name="Milk", expiry="2099-01-01"):
        db.add_food(name, expiry)
        return db.all_foods()[0][0]

    def test_remove_deletes_the_item(self):
        food_id = self.add_one()
        self.client.post(f"/remove/{food_id}")
        self.assertEqual(len(db.all_foods()), 0)

    def test_remove_redirects_back_to_home(self):
        food_id = self.add_one()
        response = self.client.post(f"/remove/{food_id}")
        self.assertEqual(response.status_code, 302)

    def test_remove_leaves_other_items_alone(self):
        food_id = self.add_one("Milk")
        self.add_one("Bread", "2099-02-02")
        self.client.post(f"/remove/{food_id}")
        rows = db.all_foods()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1], "Bread")

    def test_home_page_has_remove_buttons(self):
        self.add_one()
        page = self.client.get("/").get_data(as_text=True)
        self.assertIn("Remove", page)


class EditItemTests(FreshTrackTests):
    """Tests for editing a food item."""

    def add_one(self, name="Milk", expiry="2099-01-01", category="Dairy"):
        db.add_food(name, expiry, category)
        food_id = db.all_foods()[0][0]
        return food_id, (name, expiry, category)

    def test_edit_page_shows_prefilled_form(self):
        food_id, (name, expiry, _) = self.add_one()
        page = self.client.get(f"/edit/{food_id}").get_data(as_text=True)
        self.assertIn(name, page)
        self.assertIn(expiry, page)

    def test_edit_saves_changes_and_redirects(self):
        food_id, _ = self.add_one()
        response = self.client.post(
            f"/edit/{food_id}",
            data={
                "name": "Almond Milk",
                "expiry_date": "2099-05-05",
                "category": "Dairy",
            },
        )
        self.assertEqual(response.status_code, 302)
        rows = db.all_foods()
        self.assertEqual(rows[0][1], "Almond Milk")
        self.assertEqual(rows[0][2], "2099-05-05")

    def test_edit_rejects_empty_name(self):
        food_id, (name, expiry, _) = self.add_one()
        response = self.client.post(
            f"/edit/{food_id}",
            data={"name": "  ", "expiry_date": "2099-05-05"},
        )
        self.assertEqual(response.status_code, 400)
        rows = db.all_foods()
        self.assertEqual(rows[0][1], name)
        self.assertEqual(rows[0][2], expiry)

    def test_edit_rejects_bad_date(self):
        food_id, _ = self.add_one()
        response = self.client.post(
            f"/edit/{food_id}",
            data={"name": "Milk", "expiry_date": "2099-13-40"},
        )
        self.assertEqual(response.status_code, 400)

    def test_edit_rejects_unknown_category(self):
        food_id, _ = self.add_one()
        response = self.client.post(
            f"/edit/{food_id}",
            data={"name": "Milk", "expiry_date": "2099-05-05", "category": "MadeUp"},
        )
        self.assertEqual(response.status_code, 400)

    def test_home_page_has_edit_links(self):
        self.add_one()
        page = self.client.get("/").get_data(as_text=True)
        self.assertIn("Edit", page)


class SortByExpiryTests(FreshTrackTests):
    """Tests for the sort-by-expiry feature (soonest first)."""

    @staticmethod
    def in_days(n):
        return (date.today() + timedelta(days=n)).isoformat()

    def test_sort_foods_expiry_order(self):
        foods = [
            {"name": "Cheese", "expiry_date": "2026-09-30"},
            {"name": "Bread", "expiry_date": "2026-09-15"},
            {"name": "Milk", "expiry_date": "2026-09-20"},
        ]
        sorted_foods = sort_foods(foods, "expiry")
        self.assertEqual(
            [food["name"] for food in sorted_foods],
            ["Bread", "Milk", "Cheese"],
        )

    def test_sort_foods_default_keeps_newest_order(self):
        foods = [
            {"name": "Cheese", "expiry_date": "2026-09-30"},
            {"name": "Bread", "expiry_date": "2026-09-15"},
        ]
        self.assertEqual(sort_foods(foods), foods)

    def test_expiry_sort_shows_soonest_item_first(self):
        # Both items expire outside the 7-day reminder window, and their names
        # do not appear elsewhere on the page, so the only places they show
        # up are the food-list entries themselves.
        db.add_food("Yogurt", self.in_days(10))
        db.add_food("Butter", self.in_days(20))
        page = self.client.get("/?sort=expiry").get_data(as_text=True)
        self.assertLess(page.index("Yogurt"), page.index("Butter"))

    def test_default_page_stays_newest_first(self):
        db.add_food("Yogurt", self.in_days(10))
        db.add_food("Butter", self.in_days(20))
        page = self.client.get("/").get_data(as_text=True)
        self.assertLess(page.index("Butter"), page.index("Yogurt"))

    def test_page_has_sort_links(self):
        page = self.client.get("/").get_data(as_text=True)
        self.assertIn("Soonest first", page)
        self.assertIn("Newest first", page)


class FridgePantrySectionsTests(FreshTrackTests):
    """Tests for showing fridge and pantry items in separate sections."""

    @staticmethod
    def in_days(n):
        return (date.today() + timedelta(days=n)).isoformat()

    def test_page_shows_fridge_and_pantry_headings(self):
        db.add_food("Milk", self.in_days(5), "Dairy")
        db.add_food("Pasta", self.in_days(300), "Pantry")
        page = self.client.get("/").get_data(as_text=True)
        self.assertIn('class="section-subtitle">Fridge', page)
        self.assertIn('class="section-subtitle">Pantry', page)

    def test_fridge_and_pantry_items_appear_in_their_own_sections(self):
        db.add_food("Butter", self.in_days(30), "Dairy")
        db.add_food("Pasta", self.in_days(300), "Pantry")
        page = self.client.get("/").get_data(as_text=True)

        fridge_heading = page.index('class="section-subtitle">Fridge')
        pantry_heading = page.index('class="section-subtitle">Pantry')
        self.assertLess(fridge_heading, pantry_heading)

        butter_idx = page.index("Butter")
        self.assertGreater(butter_idx, fridge_heading)
        self.assertLess(butter_idx, pantry_heading)

        pasta_idx = page.index("Pasta")
        self.assertGreater(pasta_idx, pantry_heading)

    def test_fridge_heading_hidden_when_no_fridge_items(self):
        db.add_food("Rice", self.in_days(200), "Pantry")
        page = self.client.get("/").get_data(as_text=True)
        self.assertNotIn('class="section-subtitle">Fridge', page)
        self.assertIn('class="section-subtitle">Pantry', page)
        self.assertIn("Rice", page)

    def test_section_counts_are_shown(self):
        db.add_food("Milk", self.in_days(5), "Dairy")
        db.add_food("Pasta", self.in_days(300), "Pantry")
        page = self.client.get("/").get_data(as_text=True)
        self.assertIn("Fridge (1)", page)
        self.assertIn("Pantry (1)", page)


class DashboardTests(FreshTrackTests):
    """Tests for the fridge/pantry dashboard counts."""

    @staticmethod
    def in_days(n):
        return (date.today() + timedelta(days=n)).isoformat()

    def test_dashboard_shows_fridge_and_pantry_labels(self):
        db.add_food("Milk", self.in_days(5), "Dairy")
        db.add_food("Pasta", self.in_days(300), "Pantry")
        page = self.client.get("/").get_data(as_text=True)
        self.assertIn("Fridge items", page)
        self.assertIn("Pantry items", page)

    def test_dashboard_counts_are_correct(self):
        db.add_food("Milk", self.in_days(5), "Dairy")
        db.add_food("Rice", self.in_days(200), "Pantry")
        db.add_food("Baked Beans", self.in_days(300), "Pantry")
        page = self.client.get("/").get_data(as_text=True)
        self.assertIn('data-section="fridge">1<', page)
        self.assertIn('data-section="pantry">2<', page)

    def test_dashboard_shows_zero_when_populated_later(self):
        # Nothing in the database yet -> dashboard shows 0 / 0.
        page = self.client.get("/").get_data(as_text=True)
        self.assertIn('data-section="fridge">0<', page)
        self.assertIn('data-section="pantry">0<', page)

    def test_dashboard_updates_after_removing_item(self):
        db.add_food("Milk", self.in_days(5), "Dairy")
        db.add_food("Pasta", self.in_days(300), "Pantry")
        food_id = db.all_foods()[0][0]  # newest item = Pasta
        self.client.post(f"/remove/{food_id}")
        page = self.client.get("/").get_data(as_text=True)
        self.assertIn('data-section="pantry">0<', page)
        self.assertIn('data-section="fridge">1<', page)


if __name__ == "__main__":
    unittest.main()