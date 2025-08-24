# Developer Guide
# FocusPulse Elite — Developer Guide

**A masterpiece productivity analytics platform by Hajrah Saleha Kazi**  
[LinkedIn](https://linkedin.com/in/hajrah-saleha-kazi)

---

## 📦 Project Structure

```
focuspulse/
│
├── app.py                # Main entry point; launches UI
├── config.py             # Global config (colors, paths, metadata)
├── database.py           # Database manager (SQLite, demo data, CRUD)
├── models.py             # Core dataclasses for session and live data
├── utils.py              # Utility functions (formatting, cross-platform helpers)
├── __init__.py           # Module marker
│
├── exports/              # User-exported analytics/data (.gitkeep for Git)
├── logs/                 # Log output (runtime info, errors)
│
├── resources/            # Optional static resources (icons, doc, etc.)
└── ...
```

---

## 🚀 Development Setup

1. **Install Dependencies**

    ```
    pip install -r requirements.txt
    ```

    - Main external packages: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn` (optional), `psutil`, `tkinter`.

2. **Run Application**

    ```
    python app.py
    ```

3. **Environment**

    - Python 3.8+
    - SQLite3 is standard in Python; no extra DB server required.
    - All data stored in the working directory (see `config.py`).

---

## 🧩 Key Components

### Models (`models.py`)
- `LiveSessionData`: Live, real-time tracking buffer (not persisted).
- `AdvancedFocusSession`: Comprehensive record for one tracked session.

### Database (`database.py`)
- Handles DB schema for `sessions`.
- Injects demo data on first run.
- Use `get_sessions(days=N)` for analytics/insights.

### Configuration (`config.py`)
- Set theme colors, export/log paths, preferences.
- Update/extend as needed for new features.

### GUI (`app.py`)
- **Tkinter**-based with prominent header, tabbed main area, live plots (Matplotlib).
- Editing UI: adjust only via recommended font/style settings for consistency.
- All live updates run on Tkinter after-loop (thread safe).
- All user messages/branding centralized for ease of customization.

### Utilities (`utils.py`)
- General-purpose helpers (formatting, OS detection, file tools).

---

## ⚙️ Extending the App

### Add a New Data Field

1. Add field to `AdvancedFocusSession` in `models.py`.
2. Update DB schema in `database.py` (`CREATE TABLE` and `.executemany` call for demo data).
3. Update session generation code in `app.py` to populate the new field where needed.
4. Update analytics/export logic if the field should be presented to the user.

### New Analytics or Visualization

- Add your code inside the analytics tab setup in `app.py` (see `setup_analytics_tab` and `refresh_analytics`).
- For visualizations: create a new Matplotlib figure and embed via FigureCanvasTkAgg.

### Add a New Insight

- Edit or extend `generate_insights` and `create_insights` in `app.py`.
- Customizable logic can use any fields present on recent session objects.

### Packaging/Distribution

- Keeps all user data local. For redistributable builds, recommend packaging with PyInstaller or similar.
- Keep `resources/` for artwork/icons.

---

## 🧪 Testing

- Designed for manual, interactive testing via the GUI.
- Analytics and export are deterministic with the included demo data (first run).
- For unit tests, target functions in `utils.py` and mock session objects for analytics methods.

---

## 🛡️ Security & Privacy

- **No tracking, telemetry, or external data dependencies.**
- All analytics and AI recommendations are computed locally.
- Reviewing DB or export code will reveal precise local-only operation.

---

## 👩‍💻 Contribution Guidelines

- Write clean, readable code.
- Document new classes/modules.
- Match the style guide set by original files.
- **Credit the creator** Hajrah Saleha Kazi in all major file docstrings.

---

Thank you for contributing to **FocusPulse Elite**!
```
