# Database management
"""
FocusPulse Elite - Advanced Database Manager

Built with ❤️ by Hajrah Saleha Kazi
LinkedIn: https://linkedin.com/in/hajrah-saleha-kazi

Handles local persistent storage of tracked session data using SQLite, including schema,
demo data, and session retrieval for advanced analytics.

Version: 4.2.0
License: MIT
"""

import sqlite3
from datetime import datetime, timedelta

try:
    from .models import AdvancedFocusSession
except ImportError:
    from models import AdvancedFocusSession

class AdvancedDatabaseManager:
    """
    Manages the FocusPulse Elite SQLite database,
    including schema setup, demo data injection, and complex session queries.
    """

    def __init__(self, db_path="focuspulse_masterpiece.db"):
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """Initialize masterpiece SQLite schema and inject demo data"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS sessions")
            cursor.execute('''
                CREATE TABLE sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    application TEXT NOT NULL,
                    window_title TEXT,
                    duration_seconds INTEGER,
                    category TEXT,
                    subcategory TEXT,
                    focus_score REAL,
                    productivity_score REAL,
                    distraction_score REAL,
                    typing_events INTEGER DEFAULT 0,
                    mouse_events INTEGER DEFAULT 0,
                    clicks INTEGER DEFAULT 0,
                    scrolls INTEGER DEFAULT 0,
                    app_switches INTEGER DEFAULT 0,
                    idle_time REAL DEFAULT 0,
                    active_time REAL DEFAULT 0,
                    peak_activity_period TEXT DEFAULT '',
                    energy_level REAL DEFAULT 5.0,
                    context_switches INTEGER DEFAULT 0,
                    memory_usage_mb REAL DEFAULT 0,
                    cpu_usage_percent REAL DEFAULT 0,
                    screen_time_quality TEXT DEFAULT 'good',
                    break_compliance BOOLEAN DEFAULT FALSE
                )
            ''')
            self._insert_masterpiece_data(cursor)
            conn.commit()
            conn.close()
            print("✅ Masterpiece Database initialized!")
        except Exception as e:
            print(f"❌ Database error: {e}")

    def _insert_masterpiece_data(self, cursor):
        """Insert world-class demo data"""
        demo_sessions = [
            ("2025-08-24T09:00:00", "vscode.exe", "Python Development - FocusPulse Masterpiece", 4200,
             "Development", "Coding", 96, 98, 4, 220, 380, 110, 30, 1,
             180, 4020, "morning", 9.8, 1, 320, 18, "exceptional", True),
            ("2025-08-24T11:15:00", "figma.exe", "UI/UX Design - Masterpiece Interface", 3600,
             "Design", "UI/UX", 94, 96, 6, 180, 320, 85, 20, 1,
             200, 3400, "morning", 9.5, 1, 280, 22, "exceptional", True),
            ("2025-08-24T14:30:00", "chrome.exe", "Research - Best Design Practices", 2100,
             "Research", "Web", 88, 90, 12, 120, 240, 95, 35, 3,
             120, 1980, "afternoon", 8.8, 2, 380, 30, "excellent", True),
            ("2025-08-24T16:45:00", "notion.so", "Documentation - Technical Specs", 2700,
             "Productivity", "Writing", 91, 93, 9, 160, 220, 60, 25, 1,
             180, 2520, "afternoon", 9.1, 1, 340, 25, "exceptional", True),
            ("2025-08-23T10:00:00", "photoshop.exe", "Creative Design - Brand Assets", 3900,
             "Design", "Graphics", 93, 91, 8, 200, 350, 90, 35, 2,
             240, 3660, "morning", 9.2, 1, 450, 35, "exceptional", True),
        ]

        cursor.executemany('''
            INSERT INTO sessions (
                timestamp, application, window_title, duration_seconds,
                category, subcategory, focus_score, productivity_score, distraction_score,
                typing_events, mouse_events, clicks, scrolls, app_switches,
                idle_time, active_time, peak_activity_period, energy_level, context_switches,
                memory_usage_mb, cpu_usage_percent, screen_time_quality, break_compliance
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', demo_sessions)

    def get_sessions(self, days: int = 7):
        """Retrieve recent AdvancedFocusSession objects from the database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cutoff_date = (datetime.now() - timedelta(days=days)).isoformat()
            cursor.execute(
                "SELECT * FROM sessions WHERE timestamp >= ? ORDER BY timestamp DESC", (cutoff_date,)
            )
            sessions = []
            for row in cursor.fetchall():
                session = AdvancedFocusSession(
                    id=row[0],
                    timestamp=datetime.fromisoformat(row[1]),
                    application=row[2],
                    window_title=row[3] or "",
                    duration_seconds=row[4] or 0,
                    category=row[5] or "Uncategorized",
                    subcategory=row[6] or "Unknown",
                    focus_score=row[7] or 50.0,
                    productivity_score=row[8] or 50.0,
                    distraction_score=row[9] or 50.0,
                    typing_events=row[10] or 0,
                    mouse_events=row[11] or 0,
                    clicks=row[12] or 0,
                    scrolls=row[13] or 0,
                    app_switches=row[14] or 0,
                    idle_time=row[15] or 0.0,
                    active_time=row[16] or 0.0,
                    peak_activity_period=row[17] or "",
                    energy_level=row[18] or 5.0,
                    context_switches=row[19] or 0,
                    memory_usage_mb=row[20] or 0.0,
                    cpu_usage_percent=row[21] or 0.0,
                    screen_time_quality=row[22] or "good",
                    break_compliance=bool(row[23]) if row[23] is not None else False
                )
                sessions.append(session)
            conn.close()
            return sessions
        except Exception as e:
            print(f"Error getting sessions: {e}")
            return []
