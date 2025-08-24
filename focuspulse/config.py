# Configuration settings
"""
FocusPulse Elite - Configuration Module

Built with ❤️ by Hajrah Saleha Kazi
LinkedIn: https://linkedin.com/in/hajrah-saleha-kazi

Centralized configuration for application-level constants,
user settings, and environment-specific tweaks.

Version: 4.2.0
License: MIT
"""

import os
from pathlib import Path
import sys

# --- MAIN DIRECTORY & ENV ---
BASE_DIR = Path(__file__).parent.resolve()

# --- Database file ---
DATABASE_PATH = BASE_DIR / "focuspulse_masterpiece.db"

# --- Export directories ---
EXPORT_DIR = BASE_DIR / "exports"
EXPORT_DIR.mkdir(exist_ok=True)

# --- Logging ---
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "focuspulse.log"
LOG_DIR.mkdir(exist_ok=True)

# --- Color Palette (can be imported if consistent across GUI modules) ---
COLOR_PALETTE = {
    'primary_dark': '#1e3a8a',
    'primary': '#3b82f6',
    'primary_light': '#60a5fa',
    'secondary': '#059669',
    'accent': '#f59e0b',
    'success': '#10b981',
    'warning': '#f59e0b',
    'danger': '#ef4444',
    'info': '#3b82f6',
    'text_primary': '#1f2937',
    'text_secondary': '#6b7280',
    'text_light': '#9ca3af',
    'background': '#f8fafc',
    'surface': '#ffffff',
    'surface_elevated': '#f1f5f9',
    'border': '#e2e8f0',
    'live_success': '#22c55e',
    'live_warning': '#eab308',
    'live_danger': '#dc2626',
}

# --- Application metadata ---
APP_NAME = "FocusPulse Elite"
APP_VERSION = "4.2.0"
CREATOR = "Hajrah Saleha Kazi"
CREATOR_LINKEDIN = "https://linkedin.com/in/hajrah-saleha-kazi"

# --- Default user preferences ---
USER_PREFERENCES = {
    "theme": "auto",  # "auto", "light", "dark"
    "analytics_days": 30,
    "font_family": "Segoe UI",
    "font_size": 12,
    "autosave_interval_sec": 60,
    "enable_ai_insights": True,
    "show_welcome_on_start": True,
}

# --- Feature toggles ---
FEATURE_TOGGLES = {
    "ml_enabled": True,
    "windows_tracking": os.name == "nt",
    "macos_tracking": sys.platform == "darwin",
    "pynput_enabled": True,
    "debug_mode": False,
}

# --- Helper functions for config access (optional) ---
def get_database_path():
    return str(DATABASE_PATH)

def get_log_file():
    return str(LOG_FILE)

def get_export_dir():
    return str(EXPORT_DIR)

def get_color_palette():
    return COLOR_PALETTE.copy()

def get_user_pref(key: str, default=None):
    return USER_PREFERENCES.get(key, default)
