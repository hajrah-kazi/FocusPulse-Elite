# Tests for tracker
"""
FocusPulse Elite — Tracker Logic Unit Tests

Tests for MasterpieceActivityTracker, session lifecycle,
and database integration.

Author: Hajrah Saleha Kazi
"""

import unittest
from datetime import datetime, timedelta
import os

# Adjust import path as necessary for your project structure
from app import MasterpieceActivityTracker, AdvancedDatabaseManager

class TestMasterpieceActivityTracker(unittest.TestCase):

    def setUp(self):
        # Use a temporary test database
        self.test_db = "test_focuspulse.db"
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
        self.db_manager = AdvancedDatabaseManager(db_path=self.test_db)
        self.tracker = MasterpieceActivityTracker()
        self.tracker.db_manager = self.db_manager

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_start_stop_tracking(self):
        """Test session starts, produces live data, and properly stops."""
        self.tracker.start_tracking()
        self.assertTrue(self.tracker.is_tracking)
        self.tracker.live_session.duration_seconds = 30
        # Simulate some events
        self.tracker.live_session.focus_scores.append(95.0)
        self.tracker.live_session.productivity_scores.append(98.0)
        self.tracker.stop_tracking()
        self.assertFalse(self.tracker.is_tracking)
        self.assertIsNone(self.tracker.live_session)

    def test_get_live_session_data(self):
        """Test live session data is available during tracking."""
        self.tracker.start_tracking()
        live = self.tracker.get_live_session_data()
        self.assertIsNotNone(live)
        self.tracker.stop_tracking()
        live = self.tracker.get_live_session_data()
        self.assertIsNone(live)

    def test_export_data(self):
        """Test export generates a CSV for at least demo data."""
        fname = self.tracker.export_enhanced_data("csv", days=30)
        self.assertTrue(fname.endswith(".csv"))
        self.assertTrue(os.path.exists(fname))
        # Check CSV is not empty
        with open(fname, 'r') as f:
            lines = f.readlines()
        self.assertGreater(len(lines), 1)
        os.remove(fname)

    def test_database_sessions(self):
        """Test sessions retrieval from the database."""
        sessions = self.db_manager.get_sessions(days=7)
        self.assertTrue(isinstance(sessions, list))
        self.assertGreaterEqual(len(sessions), 1)
        session = sessions[0]
        self.assertTrue(hasattr(session, 'focus_score'))
        self.assertTrue(hasattr(session, 'productivity_score'))

if __name__ == "__main__":
    unittest.main()
