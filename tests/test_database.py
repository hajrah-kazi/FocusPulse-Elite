# Tests for database
"""
FocusPulse Elite — Database Unit Tests

Tests for AdvancedDatabaseManager, session storage, and demo data retrieval.

Author: Hajrah Saleha Kazi
"""
# tests/test_database.py
import sys
import os
import unittest
from datetime import datetime, timedelta

# Add the parent directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now import from the focuspulse package
from focuspulse.app import AdvancedDatabaseManager, AdvancedFocusSession

class TestAdvancedDatabaseManager(unittest.TestCase):


    def setUp(self):
        # Use a temporary database to avoid polluting production data
        self.test_db = "test_focuspulse_db.db"
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
        self.db = AdvancedDatabaseManager(db_path=self.test_db)

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_init_database_creates_sessions_table(self):
        """Database initializes and sessions table exists."""
        import sqlite3
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sessions'")
        table = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(table)
        self.assertEqual(table[0], "sessions")

    def test_demo_data_present(self):
        """Demo data is injected and retrievable."""
        sessions = self.db.get_sessions(days=10)
        self.assertIsInstance(sessions, list)
        self.assertGreaterEqual(len(sessions), 1)
        # Check fields
        first = sessions[0]
        self.assertIsInstance(first, AdvancedFocusSession)
        self.assertIsInstance(first.application, str)
        self.assertGreater(first.duration_seconds, 0)
        self.assertGreaterEqual(first.focus_score, 0)
        self.assertGreaterEqual(first.productivity_score, 0)

    def test_get_sessions_respects_days(self):
        """Sessions are filtered by days parameter."""
        # Our demo sessions should include dates within the last 2 days
        recent = self.db.get_sessions(days=2)
        all_sessions = self.db.get_sessions(days=100)
        self.assertLessEqual(len(recent), len(all_sessions))
        self.assertTrue(all(s.timestamp >= datetime.now() - timedelta(days=2)
                            for s in recent))

    def test_insert_and_retrieve_custom_session(self):
        """Can insert and retrieve a custom session record."""
        import sqlite3
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        # Use similar fields as demo data
        custom_session = (
            datetime.now().isoformat(),
            "testapp.exe",
            "Unit Test Window",
            1234,
            "Testing",
            "UnitTest",
            99.5,
            98.7,
            1.1,
            100, 200, 50, 10, 0,
            300, 934, "afternoon", 8.4, 2, 512, 17, "excellent", True
        )
        cursor.execute('''
            INSERT INTO sessions (
                timestamp, application, window_title, duration_seconds,
                category, subcategory, focus_score, productivity_score, distraction_score,
                typing_events, mouse_events, clicks, scrolls, app_switches,
                idle_time, active_time, peak_activity_period, energy_level, context_switches,
                memory_usage_mb, cpu_usage_percent, screen_time_quality, break_compliance
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', custom_session)
        conn.commit()
        conn.close()
        sessions = self.db.get_sessions(days=1)
        found = [s for s in sessions if s.application == "testapp.exe"]
        self.assertTrue(found)
        self.assertEqual(found[0].category, "Testing")

if __name__ == "__main__":
    unittest.main()
