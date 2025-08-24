# Utility functions
"""
FocusPulse Elite - Utility Functions

Built with ❤️ by Hajrah Saleha Kazi
LinkedIn: https://linkedin.com/in/hajrah-saleha-kazi

General helpers for formatting, time conversion, statistical calculations,
and cross-platform convenience tools.

Version: 4.2.0
License: MIT
"""

import os
import sys
from datetime import datetime, timedelta

def format_duration(seconds: int) -> str:
    """
    Format a duration in seconds as H:MM:SS or MM:SS.
    """
    if seconds < 0:
        return "0:00"
    hours = seconds // 3600
    mins = (seconds % 3600) // 60
    secs = seconds % 60
    if hours > 0:
        return f"{hours}:{mins:02}:{secs:02}"
    return f"{mins}:{secs:02}"

def nice_date(dt: datetime) -> str:
    """
    Return a user-friendly date label for a session.
    """
    today = datetime.now().date()
    if dt.date() == today:
        return "Today"
    elif dt.date() == today - timedelta(days=1):
        return "Yesterday"
    else:
        return dt.strftime("%d %b %Y")

def safe_float(val, default: float = 0.0) -> float:
    """
    Convert to float if possible, else provide a default.
    """
    try:
        return float(val)
    except Exception:
        return default

def moving_average(data, window: int = 5):
    """
    Compute a simple moving average for a list of values.
    """
    import numpy as np
    if not data or window < 1:
        return []
    return np.convolve(data, [1./window]*window, mode='valid')

def slugify(text: str) -> str:
    """
    Sanitize a filename or identifier string.
    """
    import re
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def clamp(val, min_val, max_val):
    """
    Clamp a value to a specified range.
    """
    return max(min_val, min(max_val, val))

def open_file_location(path: str):
    """Open file explorer (cross-platform) showing the given file or folder."""
    if not os.path.exists(path):
        return
    if sys.platform == 'win32':
        os.startfile(os.path.normpath(path))
    elif sys.platform == 'darwin':
        # macOS
        os.system(f'open "{os.path.abspath(path)}"')
    else:
        # linux
        os.system(f'xdg-open "{os.path.abspath(path)}"')

def random_color():
    """
    Generate a random hex color string.
    """
    import random
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def ensure_dir(path: str):
    """Ensure a directory exists."""
    import os
    os.makedirs(path, exist_ok=True)

def seconds_to_minutes(seconds: float) -> float:
    """
    Convert seconds to minutes, rounded to 1 decimal.
    """
    return round(seconds / 60.0, 1)

def is_windows() -> bool:
    """Return True if on Windows OS."""
    return sys.platform.startswith("win")

def is_mac() -> bool:
    """Return True if on macOS."""
    return sys.platform == "darwin"

def is_linux() -> bool:
    """Return True if on Linux."""
    return sys.platform.startswith("linux")
