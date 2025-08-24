# focuspulse/models.py
from dataclasses import dataclass, field
from datetime import datetime
from collections import deque
from typing import Optional

@dataclass
class LiveSessionData:
    """Real-time session tracking data"""
    start_time: datetime
    current_app: str
    current_window: str
    duration_seconds: int = 0
    focus_scores: deque = field(default_factory=lambda: deque(maxlen=300))
    productivity_scores: deque = field(default_factory=lambda: deque(maxlen=300))
    activity_events: deque = field(default_factory=lambda: deque(maxlen=60))
    timestamps: deque = field(default_factory=lambda: deque(maxlen=300))

@dataclass
class AdvancedFocusSession:
    # Copy the full class definition from app.py
    pass
