# Main GUI application
#!/usr/bin/env python3

"""
FocusPulse Elite - The Ultimate Masterpiece GUI Application

Built with ❤️ by Hajrah Saleha Kazi
LinkedIn: https://linkedin.com/in/hajrah-saleha-kazi

The most sophisticated, elegant, and user-friendly productivity tracker ever created.
This module contains the main GUI application for the structured package.

Version: 4.2.0 - Professional Structure Edition
License: MIT
"""

import os
import sys
import json
import time
import threading
import webbrowser
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
import logging
from collections import defaultdict, deque

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter import font as tkfont

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.animation import FuncAnimation
import matplotlib.dates as mdates
import seaborn as sns

# Configure matplotlib for optimal display
plt.style.use('default')
plt.rcParams['figure.facecolor'] = '#ffffff'
plt.rcParams['axes.facecolor'] = '#fafbfc'
plt.rcParams['font.size'] = 10

# Import from other modules in the package
try:
    from .tracker import MasterpieceActivityTracker
    from .database import AdvancedDatabaseManager
    from .models import LiveSessionData, AdvancedFocusSession
except ImportError:
    # Fallback for single-file compatibility
    import sys
    from pathlib import Path
    
    # Add current directory to path
    current_dir = Path(__file__).parent
    sys.path.insert(0, str(current_dir))
    
    try:
        from tracker import MasterpieceActivityTracker
        from database import AdvancedDatabaseManager
        from models import LiveSessionData, AdvancedFocusSession
    except ImportError:
        # Final fallback - define classes inline for compatibility
        print("⚠️  Running in compatibility mode")

# === THE ULTIMATE FIXED MASTERPIECE GUI ===
class UltimateMasterpieceGUI:
    """
    The Ultimate Masterpiece GUI Application
    
    This class represents the pinnacle of productivity tracking interface design,
    combining elegant aesthetics with powerful functionality to create an
    unparalleled user experience.
    
    Features:
    - Fixed header layout with prominent START/STOP controls
    - Real-time productivity tracking with live graphs
    - Advanced analytics dashboard with beautiful visualizations
    - AI-powered insights and recommendations
    - Professional typography and color system
    - Privacy-first local data storage
    """

    def __init__(self):
        """Initialize the ultimate masterpiece GUI"""
        try:
            self.tracker = MasterpieceActivityTracker()
        except NameError:
            # Compatibility fallback
            from tracker import MasterpieceActivityTracker
            self.tracker = MasterpieceActivityTracker()
            
        self.tracking_thread = None
        
        # Initialize the ultimate window
        self.root = tk.Tk()
        self.root.title("FocusPulse Elite - The Ultimate Masterpiece by Hajrah Saleha Kazi")
        self.root.geometry("1400x900")
        
        # Maximize window on startup
        try:
            self.root.state('zoomed')  # Windows
        except tk.TclError:
            try:
                self.root.attributes('-zoomed', True)  # Linux
            except tk.TclError:
                # macOS fallback
                self.root.attributes('-fullscreen', False)
                self.root.geometry("1400x900")
        
        # ULTIMATE MASTERPIECE COLOR PALETTE
        self.colors = {
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
        
        self.root.configure(bg=self.colors['background'])
        
        # Initialize all components
        self.setup_masterpiece_fonts()
        self.setup_masterpiece_styles()
        self.create_fixed_layout()
        self.setup_all_tabs()
        self.start_live_updates()
        
        # Handle window closing
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_masterpiece_fonts(self):
        """Setup the most elegant typography system"""
        try:
            self.fonts = {
                'display_xl': tkfont.Font(family="Segoe UI", size=32, weight="bold"),
                'display_lg': tkfont.Font(family="Segoe UI", size=28, weight="bold"),
                'display_md': tkfont.Font(family="Segoe UI", size=24, weight="bold"),
                'heading_xl': tkfont.Font(family="Segoe UI", size=22, weight="bold"),
                'heading_lg': tkfont.Font(family="Segoe UI", size=20, weight="bold"),
                'heading_md': tkfont.Font(family="Segoe UI", size=18, weight="bold"),
                'heading_sm': tkfont.Font(family="Segoe UI", size=16, weight="bold"),
                'body_xl': tkfont.Font(family="Segoe UI", size=16),
                'body_lg': tkfont.Font(family="Segoe UI", size=14),
                'body_md': tkfont.Font(family="Segoe UI", size=12),
                'body_sm': tkfont.Font(family="Segoe UI", size=11),
                'ui_lg': tkfont.Font(family="Segoe UI", size=14, weight="bold"),
                'ui_md': tkfont.Font(family="Segoe UI", size=12, weight="bold"),
                'ui_sm': tkfont.Font(family="Segoe UI", size=11),
                'caption': tkfont.Font(family="Segoe UI", size=10),
                'mono': tkfont.Font(family="Consolas", size=11),
                'button_xl': tkfont.Font(family="Segoe UI", size=18, weight="bold"),
                'button_lg': tkfont.Font(family="Segoe UI", size=16, weight="bold"),
                'button_md': tkfont.Font(family="Segoe UI", size=14, weight="bold"),
            }
        except Exception as e:
            # Fallback fonts for systems without Segoe UI
            print(f"⚠️  Using fallback fonts: {e}")
            self.fonts = {
                'display_xl': ('Arial', 32, 'bold'),
                'display_lg': ('Arial', 28, 'bold'),
                'display_md': ('Arial', 24, 'bold'),
                'heading_xl': ('Arial', 22, 'bold'),
                'heading_lg': ('Arial', 20, 'bold'),
                'heading_md': ('Arial', 18, 'bold'),
                'heading_sm': ('Arial', 16, 'bold'),
                'body_xl': ('Arial', 16),
                'body_lg': ('Arial', 14),
                'body_md': ('Arial', 12),
                'body_sm': ('Arial', 11),
                'ui_lg': ('Arial', 14, 'bold'),
                'ui_md': ('Arial', 12, 'bold'),
                'ui_sm': ('Arial', 11),
                'caption': ('Arial', 10),
                'mono': ('Courier', 11),
                'button_xl': ('Arial', 18, 'bold'),
                'button_lg': ('Arial', 16, 'bold'),
                'button_md': ('Arial', 14, 'bold'),
            }

    def setup_masterpiece_styles(self):
        """Setup the most sophisticated TTK styles"""
        style = ttk.Style()
        
        try:
            style.theme_use('clam')
        except Exception:
            # Use default theme if clam is not available
            pass
        
        # Configure notebook styles
        style.configure('Masterpiece.TNotebook', 
                       background=self.colors['surface'],
                       borderwidth=0)
        
        style.configure('Masterpiece.TNotebook.Tab',
                       background=self.colors['surface_elevated'],
                       foreground=self.colors['text_secondary'],
                       padding=[20, 12],
                       focuscolor='none')
        
        style.map('Masterpiece.TNotebook.Tab',
                  background=[('selected', self.colors['surface']),
                              ('active', self.colors['primary_light'])],
                  foreground=[('selected', self.colors['primary']),
                              ('active', 'white')])

    def create_fixed_layout(self):
        """Create properly structured layout without excessive scrollbars"""
        # === HEADER SECTION (Fixed at top) ===
        self.create_header()
        
        # === LIVE TRACKING BAR (Fixed below header) ===
        self.create_live_bar()
        
        # === MAIN CONTENT AREA (Expandable) ===
        self.create_main_content()

    def create_header(self):
        """Create fixed header with proper button layout"""
        # Header frame - fixed height, spans full width
        self.header = tk.Frame(
            self.root, 
            bg=self.colors['primary_dark'], 
            height=120
        )
        self.header.pack(fill=tk.X, side=tk.TOP)
        self.header.pack_propagate(False)  # Maintain fixed height
        
        # Header content with proper grid layout
        header_content = tk.Frame(self.header, bg=self.colors['primary_dark'])
        header_content.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        # Configure grid weights for responsive layout
        header_content.grid_columnconfigure(0, weight=1)  # Left side expands
        header_content.grid_columnconfigure(1, weight=0)  # Right side fixed
        
        # Left side - App branding
        brand_frame = tk.Frame(header_content, bg=self.colors['primary_dark'])
        brand_frame.grid(row=0, column=0, sticky="w", padx=(20, 0))
        
        tk.Label(
            brand_frame,
            text="🚀 FocusPulse Elite",
            font=self.fonts['display_md'],
            fg='white',
            bg=self.colors['primary_dark']
        ).pack(anchor=tk.W)
        
        tk.Label(
            brand_frame,
            text="The Ultimate Productivity Masterpiece",
            font=self.fonts['body_lg'],
            fg=self.colors['primary_light'],
            bg=self.colors['primary_dark']
        ).pack(anchor=tk.W, pady=(2, 0))
        
        tk.Label(
            brand_frame,
            text="Crafted with ❤️ by Hajrah Saleha Kazi",
            font=self.fonts['body_md'],
            fg=self.colors['primary_light'],
            bg=self.colors['primary_dark']
        ).pack(anchor=tk.W, pady=(5, 0))
        
        # Right side - Control buttons with proper layout
        controls_frame = tk.Frame(header_content, bg=self.colors['primary_dark'])
        controls_frame.grid(row=0, column=1, sticky="e", padx=(0, 20))
        
        # Button layout using grid for precise control
        # Row 0: START TRACKING (big button)
        self.btn_start_tracking = tk.Button(
            controls_frame,
            text="▶️  START TRACKING",
            font=self.fonts['button_xl'],
            bg=self.colors['live_success'],
            fg='white',
            relief='raised',
            padx=20,
            pady=12,
            cursor='hand2',
            command=self.start_tracking,
            bd=3
        )
        self.btn_start_tracking.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 8))
        
        # Row 1: STOP TRACKING + LinkedIn (smaller buttons side by side)
        self.btn_stop_tracking = tk.Button(
            controls_frame,
            text="⏹️ STOP",
            font=self.fonts['button_md'],
            bg=self.colors['live_danger'],
            fg='white',
            relief='raised',
            padx=15,
            pady=8,
            cursor='hand2',
            command=self.stop_tracking,
            state='disabled',
            bd=3
        )
        self.btn_stop_tracking.grid(row=1, column=0, sticky="ew", padx=(0, 5))
        
        linkedin_btn = tk.Button(
            controls_frame,
            text="🔗 LinkedIn",
            font=self.fonts['ui_md'],
            bg='white',
            fg=self.colors['primary_dark'],
            relief='raised',
            padx=12,
            pady=8,
            cursor='hand2',
            command=self.open_linkedin,
            bd=2
        )
        linkedin_btn.grid(row=1, column=1, sticky="ew", padx=(5, 0))
        
        # Configure column weights for buttons
        controls_frame.grid_columnconfigure(0, weight=1)
        controls_frame.grid_columnconfigure(1, weight=1)
        
        self.add_hover_effects()

    def create_live_bar(self):
        """Create live tracking status bar"""
        self.live_bar = tk.Frame(
            self.root,
            bg=self.colors['surface_elevated'],
            height=70
        )
        self.live_bar.pack(fill=tk.X, pady=(2, 0))
        self.live_bar.pack_propagate(False)
        
        live_content = tk.Frame(self.live_bar, bg=self.colors['surface_elevated'])
        live_content.pack(fill=tk.BOTH, expand=True, padx=30, pady=12)
        
        # Configure grid for live content
        live_content.grid_columnconfigure(1, weight=1)  # Middle expands
        
        # Status indicator
        self.status_indicator = tk.Label(
            live_content,
            text="●",
            font=self.fonts['display_md'],
            fg=self.colors['text_light'],
            bg=self.colors['surface_elevated']
        )
        self.status_indicator.grid(row=0, column=0, padx=(0, 15))
        
        # Session info (expandable)
        info_frame = tk.Frame(live_content, bg=self.colors['surface_elevated'])
        info_frame.grid(row=0, column=1, sticky="ew")
        
        self.session_status_label = tk.Label(
            info_frame,
            text="Ready to Track",
            font=self.fonts['heading_sm'],
            fg=self.colors['text_primary'],
            bg=self.colors['surface_elevated']
        )
        self.session_status_label.pack(anchor=tk.W)
        
        self.session_details_label = tk.Label(
            info_frame,
            text="Click START TRACKING to begin monitoring your productivity",
            font=self.fonts['body_md'],
            fg=self.colors['text_secondary'],
            bg=self.colors['surface_elevated']
        )
        self.session_details_label.pack(anchor=tk.W)
        
        # Live metrics (right side)
        metrics_frame = tk.Frame(live_content, bg=self.colors['surface_elevated'])
        metrics_frame.grid(row=0, column=2, padx=(15, 0))
        
        # Metrics in a horizontal layout
        self.live_duration_label = tk.Label(
            metrics_frame,
            text="Duration: 0:00",
            font=self.fonts['ui_md'],
            fg=self.colors['text_primary'],
            bg=self.colors['surface_elevated']
        )
        self.live_duration_label.pack(side=tk.LEFT, padx=(0, 15))
        
        self.live_focus_label = tk.Label(
            metrics_frame,
            text="Focus: --",
            font=self.fonts['ui_md'],
            fg=self.colors['text_primary'],
            bg=self.colors['surface_elevated']
        )
        self.live_focus_label.pack(side=tk.LEFT, padx=(0, 15))
        
        self.live_productivity_label = tk.Label(
            metrics_frame,
            text="Productivity: --",
            font=self.fonts['ui_md'],
            fg=self.colors['text_primary'],
            bg=self.colors['surface_elevated']
        )
        self.live_productivity_label.pack(side=tk.LEFT)

    def create_main_content(self):
        """Create main content area with proper tabs"""
        # Main content frame - expands to fill remaining space
        main_frame = tk.Frame(self.root, bg=self.colors['surface'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(10, 20))
        
        # Notebook for tabs - expands fully within main frame
        self.notebook = ttk.Notebook(main_frame, style='Masterpiece.TNotebook')
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tab frames
        self.dashboard_frame = tk.Frame(self.notebook, bg=self.colors['surface'])
        self.analytics_frame = tk.Frame(self.notebook, bg=self.colors['surface'])
        self.insights_frame = tk.Frame(self.notebook, bg=self.colors['surface'])
        self.settings_frame = tk.Frame(self.notebook, bg=self.colors['surface'])
        
        # Add tabs
        self.notebook.add(self.dashboard_frame, text='  🏠 Dashboard  ')
        self.notebook.add(self.analytics_frame, text='  📊 Analytics  ')
        self.notebook.add(self.insights_frame, text='  🧠 AI Insights  ')
        self.notebook.add(self.settings_frame, text='  ⚙️ Settings  ')

    def add_hover_effects(self):
        """Add elegant hover effects"""
        def create_hover_effect(button, normal_bg, hover_bg):
            def on_enter(e):
                if button['state'] != 'disabled':
                    button.configure(bg=hover_bg)
            def on_leave(e):
                if button['state'] != 'disabled':
                    button.configure(bg=normal_bg)
            button.bind("<Enter>", on_enter)
            button.bind("<Leave>", on_leave)
        
        create_hover_effect(self.btn_start_tracking, self.colors['live_success'], '#1ea854')
        create_hover_effect(self.btn_stop_tracking, self.colors['live_danger'], '#b91c1c')

    def setup_all_tabs(self):
        """Setup all tabs with proper content"""
        self.setup_dashboard_tab()
        self.setup_analytics_tab()
        self.setup_insights_tab()
        self.setup_settings_tab()

    def setup_dashboard_tab(self):
        """Create dashboard with live graphs and stats"""
        # Use scrollable frame only for dashboard content (not the whole app)
        canvas = tk.Canvas(self.dashboard_frame, bg=self.colors['surface'])
        scrollbar = ttk.Scrollbar(self.dashboard_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['surface'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Enable mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Content container
        container = tk.Frame(scrollable_frame, bg=self.colors['surface'])
        container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # === LIVE SESSION GRAPH ===
        self.create_live_graph(container)
        
        # === STATS SECTION ===
        self.create_stats_section(container)
        
        # === WELCOME SECTION ===
        self.create_welcome_section(container)

    def create_live_graph(self, parent):
        """Create live session graph"""
        graph_frame = tk.Frame(
            parent,
            bg='white',
            relief='raised',
            bd=2
        )
        graph_frame.pack(fill=tk.X, pady=(0, 30))
        
        # Graph header
        header = tk.Frame(graph_frame, bg='white')
        header.pack(fill=tk.X, padx=20, pady=(15, 0))
        
        tk.Label(
            header,
            text="📈 Live Session Performance",
            font=self.fonts['heading_lg'],
            fg=self.colors['text_primary'],
            bg='white'
        ).pack(side=tk.LEFT)
        
        self.graph_status_badge = tk.Label(
            header,
            text="● Ready",
            font=self.fonts['ui_md'],
            fg=self.colors['text_light'],
            bg='white'
        )
        self.graph_status_badge.pack(side=tk.RIGHT)
        
        # Graph area
        graph_container = tk.Frame(graph_frame, bg='white')
        graph_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=(10, 20))
        
        # Create matplotlib figure
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(12, 8))
        self.fig.patch.set_facecolor('white')
        
        # Focus plot
        self.focus_line, = self.ax1.plot([], [], color=self.colors['primary'], linewidth=2, label='Focus Score')
        self.ax1.set_ylim(0, 100)
        self.ax1.set_ylabel('Focus Score')
        self.ax1.set_title('Real-Time Productivity Tracking')
        self.ax1.grid(True, alpha=0.3)
        self.ax1.legend()
        
        # Productivity plot
        self.prod_line, = self.ax2.plot([], [], color=self.colors['secondary'], linewidth=2, label='Productivity Score')
        self.ax2.set_ylim(0, 100)
        self.ax2.set_ylabel('Productivity Score')
        self.ax2.set_xlabel('Time (minutes)')
        self.ax2.grid(True, alpha=0.3)
        self.ax2.legend()
        
        plt.tight_layout()
        
        # Embed in tkinter
        self.canvas_widget = FigureCanvasTkAgg(self.fig, master=graph_container)
        self.canvas_widget.draw()
        self.canvas_widget.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def create_stats_section(self, parent):
        """Create stats cards"""
        stats_frame = tk.Frame(parent, bg=self.colors['surface'])
        stats_frame.pack(fill=tk.X, pady=(0, 30))
        
        tk.Label(
            stats_frame,
            text="📊 Performance Analytics",
            font=self.fonts['heading_lg'],
            fg=self.colors['text_primary'],
            bg=self.colors['surface']
        ).pack(anchor=tk.W, pady=(0, 20))
        
        self.stats_container = tk.Frame(stats_frame, bg=self.colors['surface'])
        self.stats_container.pack(fill=tk.X)
        
        self.update_stats()

    def update_stats(self):
        """Update stats display"""
        # Clear existing widgets
        for widget in self.stats_container.winfo_children():
            widget.destroy()
        
        try:
            sessions = self.tracker.db_manager.get_sessions(days=7)
        except Exception:
            sessions = []
        
        if not sessions:
            # Empty state
            empty_frame = tk.Frame(self.stats_container, bg=self.colors['surface'])
            empty_frame.pack(expand=True, pady=50)
            
            tk.Label(
                empty_frame,
                text="🎯 Your Analytics Journey Begins Here",
                font=self.fonts['heading_xl'],
                fg=self.colors['primary'],
                bg=self.colors['surface']
            ).pack(pady=(0, 15))
            
            tk.Label(
                empty_frame,
                text="Start tracking to unlock powerful insights",
                font=self.fonts['body_lg'],
                fg=self.colors['text_secondary'],
                bg=self.colors['surface']
            ).pack()
        else:
            # Create stats grid
            total_time = sum([s.duration_seconds for s in sessions]) / 3600
            avg_focus = np.mean([s.focus_score for s in sessions])
            avg_productivity = np.mean([s.productivity_score for s in sessions])
            peak_session = max(sessions, key=lambda s: s.focus_score)
            
            stats = [
                ("🎯", f"{len(sessions)}", "Sessions", self.colors['primary']),
                ("⏱️", f"{total_time:.1f}h", "Focus Time", self.colors['secondary']),
                ("📈", f"{avg_focus:.0f}/100", "Avg Focus", self.colors['accent']),
                ("🚀", f"{avg_productivity:.0f}/100", "Productivity", self.colors['success']),
                ("⭐", f"{peak_session.focus_score:.0f}/100", "Peak Score", self.colors['warning'])
            ]
            
            # Create cards in grid
            grid_frame = tk.Frame(self.stats_container, bg=self.colors['surface'])
            grid_frame.pack(fill=tk.X)
            
            for i, (icon, value, label, color) in enumerate(stats):
                card = tk.Frame(
                    grid_frame,
                    bg='white',
                    relief='raised',
                    bd=2
                )
                card.grid(row=0, column=i, padx=8, pady=5, sticky='nsew', ipadx=15, ipady=15)
                
                # Configure grid weights
                grid_frame.grid_columnconfigure(i, weight=1)
                
                # Card content
                tk.Label(card, text=icon, font=('Arial', 28), bg='white', fg=color).pack(pady=(10, 5))
                tk.Label(card, text=value, font=self.fonts['heading_md'], bg='white', fg=self.colors['text_primary']).pack()
                tk.Label(card, text=label, font=self.fonts['body_md'], bg='white', fg=self.colors['text_secondary']).pack(pady=(0, 10))

    def create_welcome_section(self, parent):
        """Create welcome section"""
        welcome_frame = tk.Frame(
            parent,
            bg=self.colors['surface_elevated'],
            relief='raised',
            bd=2
        )
        welcome_frame.pack(fill=tk.X)
        
        content = tk.Frame(welcome_frame, bg=self.colors['surface_elevated'])
        content.pack(fill=tk.BOTH, expand=True, padx=30, pady=25)
        
        tk.Label(
            content,
            text="✨ Master Your Productivity Journey",
            font=self.fonts['heading_xl'],
            fg=self.colors['primary'],
            bg=self.colors['surface_elevated']
        ).pack(anchor=tk.W, pady=(0, 20))
        
        instructions = [
            "🎯 Click the prominent START TRACKING button in the header to begin",
            "📊 Watch real-time graphs update as you work",
            "⏹️ Use the STOP button to end your session anytime",
            "🧠 Receive AI-powered insights to optimize your workflow",
            "📈 Export comprehensive analytics for long-term tracking"
        ]
        
        for instruction in instructions:
            tk.Label(
                content,
                text=instruction,
                font=self.fonts['body_lg'],
                fg=self.colors['text_primary'],
                bg=self.colors['surface_elevated'],
                anchor=tk.W
            ).pack(fill=tk.X, pady=5, padx=(15, 0))

    def setup_analytics_tab(self):
        """Create analytics tab"""
        container = tk.Frame(self.analytics_frame, bg=self.colors['surface'])
        container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Header
        header = tk.Frame(container, bg=self.colors['surface'])
        header.pack(fill=tk.X, pady=(0, 30))
        
        tk.Label(
            header,
            text="📊 Advanced Analytics Dashboard",
            font=self.fonts['heading_xl'],
            fg=self.colors['primary'],
            bg=self.colors['surface']
        ).pack(side=tk.LEFT)
        
        refresh_btn = tk.Button(
            header,
            text="🔄 Refresh",
            font=self.fonts['ui_md'],
            bg=self.colors['secondary'],
            fg='white',
            relief='raised',
            padx=15,
            pady=8,
            cursor='hand2',
            command=self.refresh_analytics,
            bd=2
        )
        refresh_btn.pack(side=tk.RIGHT)
        
        # Content area
        self.analytics_content = tk.Frame(container, bg=self.colors['surface'])
        self.analytics_content.pack(fill=tk.BOTH, expand=True)
        
        self.refresh_analytics()

    def refresh_analytics(self):
        """Refresh analytics content"""
        # Clear existing content
        for widget in self.analytics_content.winfo_children():
            widget.destroy()
        
        try:
            sessions = self.tracker.db_manager.get_sessions(days=30)
            
            if not sessions:
                # Empty state
                empty_frame = tk.Frame(self.analytics_content, bg=self.colors['surface'])
                empty_frame.pack(expand=True)
                
                tk.Label(
                    empty_frame,
                    text="📊 Analytics Dashboard",
                    font=self.fonts['heading_xl'],
                    fg=self.colors['primary'],
                    bg=self.colors['surface']
                ).pack(pady=(100, 20))
                
                tk.Label(
                    empty_frame,
                    text="Start tracking to unlock comprehensive analytics",
                    font=self.fonts['body_lg'],
                    fg=self.colors['text_secondary'],
                    bg=self.colors['surface']
                ).pack()
            else:
                # Show analytics summary
                summary_frame = tk.Frame(
                    self.analytics_content,
                    bg='white',
                    relief='raised',
                    bd=2
                )
                summary_frame.pack(fill=tk.BOTH, expand=True, pady=10)
                
                summary_content = tk.Frame(summary_frame, bg='white')
                summary_content.pack(fill=tk.BOTH, expand=True, padx=30, pady=25)
                
                tk.Label(
                    summary_content,
                    text="📈 Performance Summary",
                    font=self.fonts['heading_lg'],
                    fg=self.colors['primary'],
                    bg='white'
                ).pack(pady=(0, 20))
                
                # Calculate stats
                total_time = sum([s.duration_seconds for s in sessions]) / 3600
                avg_focus = np.mean([s.focus_score for s in sessions])
                avg_productivity = np.mean([s.productivity_score for s in sessions])
                
                # Find top app
                app_performance = {}
                for s in sessions:
                    app_name = s.application.replace('.exe', '').title()
                    if app_name not in app_performance:
                        app_performance[app_name] = []
                    app_performance[app_name].append(s.focus_score)
                
                top_app = "None"
                top_score = 0
                if app_performance:
                    top_app, scores = max(app_performance.items(), key=lambda x: np.mean(x[1]))
                    top_score = np.mean(scores)
                
                summary_text = f"""🎯 Sessions Analyzed: {len(sessions)} sessions
⏱️ Total Focus Time: {total_time:.1f} hours
📊 Average Focus: {avg_focus:.1f}/100
🚀 Average Productivity: {avg_productivity:.1f}/100
💻 Top App: {top_app} ({top_score:.1f}/100)

Your productivity shows {"excellent" if avg_focus >= 85 else "good" if avg_focus >= 70 else "developing"} patterns.
Keep using the START/STOP buttons to build more comprehensive analytics!"""
                
                tk.Label(
                    summary_content,
                    text=summary_text.strip(),
                    font=self.fonts['body_lg'],
                    fg=self.colors['text_primary'],
                    bg='white',
                    justify=tk.LEFT
                ).pack(anchor=tk.W)
                
        except Exception as e:
            # Error state
            error_frame = tk.Frame(self.analytics_content, bg=self.colors['surface'])
            error_frame.pack(expand=True)
            
            tk.Label(
                error_frame,
                text=f"⚠️ Error loading analytics: {e}",
                font=self.fonts['body_lg'],
                fg=self.colors['danger'],
                bg=self.colors['surface']
            ).pack(pady=100)

    def setup_insights_tab(self):
        """Create insights tab"""
        container = tk.Frame(self.insights_frame, bg=self.colors['surface'])
        container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Header
        header = tk.Frame(container, bg=self.colors['surface'])
        header.pack(fill=tk.X, pady=(0, 30))
        
        tk.Label(
            header,
            text="🧠 AI-Powered Insights",
            font=self.fonts['heading_xl'],
            fg=self.colors['primary'],
            bg=self.colors['surface']
        ).pack(side=tk.LEFT)
        
        generate_btn = tk.Button(
            header,
            text="✨ Generate",
            font=self.fonts['ui_md'],
            bg=self.colors['accent'],
            fg='white',
            relief='raised',
            padx=15,
            pady=8,
            cursor='hand2',
            command=self.generate_insights,
            bd=2
        )
        generate_btn.pack(side=tk.RIGHT)
        
        # Content area
        self.insights_content = tk.Frame(container, bg=self.colors['surface'])
        self.insights_content.pack(fill=tk.BOTH, expand=True)
        
        self.generate_insights()

    def generate_insights(self):
        """Generate AI insights"""
        # Clear existing content
        for widget in self.insights_content.winfo_children():
            widget.destroy()
        
        try:
            sessions = self.tracker.db_manager.get_sessions(days=14)
            
            if not sessions:
                # Empty state
                empty_frame = tk.Frame(self.insights_content, bg=self.colors['surface'])
                empty_frame.pack(expand=True)
                
                tk.Label(
                    empty_frame,
                    text="🧠 AI Insights Engine",
                    font=self.fonts['heading_xl'],
                    fg=self.colors['primary'],
                    bg=self.colors['surface']
                ).pack(pady=(100, 20))
                
                tk.Label(
                    empty_frame,
                    text="Start tracking to unlock AI-powered recommendations",
                    font=self.fonts['body_lg'],
                    fg=self.colors['text_secondary'],
                    bg=self.colors['surface']
                ).pack()
            else:
                # Generate insights
                insights = self.create_insights(sessions)
                
                # Header
                tk.Label(
                    self.insights_content,
                    text=f"🎯 {len(insights)} Insights from {len(sessions)} Sessions",
                    font=self.fonts['heading_md'],
                    fg=self.colors['primary'],
                    bg=self.colors['surface']
                ).pack(pady=(0, 20))
                
                # Display insights
                for insight in insights:
                    self.create_insight_card(insight)
                    
        except Exception as e:
            # Error state
            error_frame = tk.Frame(self.insights_content, bg=self.colors['surface'])
            error_frame.pack(expand=True)
            
            tk.Label(
                error_frame,
                text=f"⚠️ Error generating insights: {e}",
                font=self.fonts['body_lg'],
                fg=self.colors['danger'],
                bg=self.colors['surface']
            ).pack(pady=100)

    def create_insights(self, sessions):
        """Create insight recommendations"""
        insights = []
        
        avg_focus = np.mean([s.focus_score for s in sessions])
        avg_productivity = np.mean([s.productivity_score for s in sessions])
        
        # Performance insight
        if avg_focus >= 85:
            insights.append({
                'title': '🏆 Excellent Focus Performance!',
                'description': f'Outstanding! Your focus score of {avg_focus:.1f}/100 shows exceptional concentration.',
                'recommendation': 'Keep up this excellent work! You\'re in the top tier of productivity.',
                'color': self.colors['success']
            })
        elif avg_focus >= 70:
            insights.append({
                'title': '🎯 Good Focus Level',
                'description': f'Good work! Your focus score of {avg_focus:.1f}/100 shows solid performance.',
                'recommendation': 'Try eliminating distractions to reach the next level.',
                'color': self.colors['primary']
            })
        else:
            insights.append({
                'title': '💪 Focus Improvement Opportunity',
                'description': f'Your focus score of {avg_focus:.1f}/100 has room for growth.',
                'recommendation': 'Start with 15-minute focused sessions and build up gradually.',
                'color': self.colors['accent']
            })
        
        # Control insight
        insights.append({
            'title': '🎮 Perfect Session Control',
            'description': 'The START and STOP buttons provide excellent session management.',
            'recommendation': 'Continue using these prominent controls for precise tracking.',
            'color': self.colors['info']
        })
        
        return insights

    def create_insight_card(self, insight):
        """Create insight card widget"""
        card = tk.Frame(
            self.insights_content,
            bg='white',
            relief='raised',
            bd=2
        )
        card.pack(fill=tk.X, pady=10)
        
        # Colored header strip
        strip = tk.Frame(card, bg=insight['color'], height=4)
        strip.pack(fill=tk.X)
        
        # Content
        content = tk.Frame(card, bg='white')
        content.pack(fill=tk.BOTH, expand=True, padx=25, pady=20)
        
        # Title
        tk.Label(
            content,
            text=insight['title'],
            font=self.fonts['heading_md'],
            fg=insight['color'],
            bg='white'
        ).pack(anchor=tk.W, pady=(0, 10))
        
        # Description
        tk.Label(
            content,
            text=insight['description'],
            font=self.fonts['body_lg'],
            fg=self.colors['text_primary'],
            bg='white',
            wraplength=600,
            justify=tk.LEFT
        ).pack(anchor=tk.W, pady=(0, 15))
        
        # Recommendation
        rec_frame = tk.Frame(content, bg=insight['color'])
        rec_frame.pack(fill=tk.X)
        
        rec_content = tk.Frame(rec_frame, bg=insight['color'])
        rec_content.pack(fill=tk.BOTH, expand=True, padx=15, pady=12)
        
        tk.Label(
            rec_content,
            text="💡 Recommendation:",
            font=self.fonts['ui_md'],
            fg='white',
            bg=insight['color']
        ).pack(anchor=tk.W)
        
        tk.Label(
            rec_content,
            text=insight['recommendation'],
            font=self.fonts['body_md'],
            fg='white',
            bg=insight['color'],
            wraplength=600,
            justify=tk.LEFT
        ).pack(anchor=tk.W, pady=(5, 0))

    def setup_settings_tab(self):
        """Create settings tab"""
        # Use scrollable content for settings
        canvas = tk.Canvas(self.settings_frame, bg=self.colors['surface'])
        scrollbar = ttk.Scrollbar(self.settings_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['surface'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        container = tk.Frame(scrollable_frame, bg=self.colors['surface'])
        container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Title
        tk.Label(
            container,
            text="⚙️ Settings & About",
            font=self.fonts['heading_xl'],
            fg=self.colors['primary'],
            bg=self.colors['surface']
        ).pack(pady=(0, 30))
        
        # About card
        about_card = tk.Frame(
            container,
            bg='white',
            relief='raised',
            bd=2
        )
        about_card.pack(fill=tk.BOTH, expand=True)
        
        about_content = tk.Frame(about_card, bg='white')
        about_content.pack(fill=tk.BOTH, expand=True, padx=30, pady=25)
        
        about_text = """🚀 FocusPulse Elite - Masterpiece Edition v4.2.0

Built with ❤️ by Hajrah Saleha Kazi

The most sophisticated, elegant, and user-friendly productivity tracking platform ever created.

✨ Key Features:

🎯 Real-Time Session Tracking
• Live performance monitoring with elegant visualizations
• Prominent START and STOP TRACKING buttons in header
• Intelligent focus and productivity scoring algorithms

🧠 Advanced AI Analytics Engine
• Machine learning-powered pattern recognition
• Personalized productivity insights and recommendations
• Sophisticated trend analysis and performance optimization

🎨 World-Class User Experience
• Fixed header layout with proper button placement
• Clean, professional interface with premium typography
• Optimal scrolling only where needed
• Responsive design that adapts to your workflow

📊 Comprehensive Analytics Dashboard
• Beautiful data visualizations and performance metrics
• Real-time graphs with live session tracking
• Export capabilities for long-term analysis

🔒 Privacy-First Architecture
• All data stored securely on your local device
• No external tracking or data collection
• Complete control over your productivity information

🎮 Perfect Control Interface
• Large, prominent START TRACKING button in header
• Equally accessible STOP TRACKING button
• Intuitive session management with visual feedback

🌟 About the Creator:

Hajrah Saleha Kazi is a visionary data scientist and software architect who specializes in creating transformative applications that empower human potential. Her expertise spans advanced analytics, machine learning, and user experience design.

Connect with Hajrah on LinkedIn to explore her groundbreaking work in data science and technology.

Thank you for choosing FocusPulse Elite! 🚀✨"""
        
        tk.Label(
            about_content,
            text=about_text,
            font=self.fonts['body_md'],
            fg=self.colors['text_primary'],
            bg='white',
            justify=tk.LEFT,
            wraplength=800
        ).pack(anchor=tk.W)
        
        # LinkedIn button
        linkedin_frame = tk.Frame(about_content, bg='white')
        linkedin_frame.pack(pady=(20, 0))
        
        linkedin_btn = tk.Button(
            linkedin_frame,
            text="🔗 Connect with Hajrah Saleha Kazi on LinkedIn",
            font=self.fonts['heading_sm'],
            bg=self.colors['primary'],
            fg='white',
            relief='raised',
            padx=30,
            pady=15,
            cursor='hand2',
            command=self.open_linkedin,
            bd=2
        )
        linkedin_btn.pack()

    def start_live_updates(self):
        """Start live update system"""
        self.update_live_display()

    def update_live_display(self):
        """Update live session display"""
        try:
            live_session = self.tracker.get_live_session_data()
            
            if live_session and self.tracker.is_tracking:
                # Update status
                self.status_indicator.config(text="●", fg=self.colors['live_success'])
                
                # Update session info
                mins = live_session.duration_seconds // 60
                secs = live_session.duration_seconds % 60
                
                self.session_status_label.config(
                    text="🔴 TRACKING ACTIVE",
                    fg=self.colors['live_success']
                )
                
                self.session_details_label.config(
                    text=f"Session: {live_session.current_app} • Duration: {mins}m {secs}s"
                )
                
                # Update metrics
                if live_session.focus_scores:
                    current_focus = live_session.focus_scores[-1]
                    current_productivity = live_session.productivity_scores[-1]
                    
                    self.live_focus_label.config(text=f"Focus: {current_focus:.0f}/100")
                    self.live_productivity_label.config(text=f"Productivity: {current_productivity:.0f}/100")
                
                self.live_duration_label.config(text=f"Duration: {mins}:{secs:02d}")
                
                # Update graph status
                self.graph_status_badge.config(text="● Live Tracking", fg=self.colors['live_success'])
                
                # Update graphs
                self.update_live_graphs(live_session)
                
            else:
                # Reset to ready state
                self.status_indicator.config(text="●", fg=self.colors['text_light'])
                self.session_status_label.config(text="Ready to Track", fg=self.colors['text_primary'])
                self.session_details_label.config(text="Click START TRACKING to begin monitoring")
                
                self.live_focus_label.config(text="Focus: --")
                self.live_productivity_label.config(text="Productivity: --")
                self.live_duration_label.config(text="Duration: 0:00")
                
                self.graph_status_badge.config(text="● Ready", fg=self.colors['text_light'])
            
            # Update stats
            self.update_stats()
            
        except Exception as e:
            print(f"Live update error: {e}")
        
        # Schedule next update
        self.root.after(1000, self.update_live_display)

    def update_live_graphs(self, live_session):
        """Update live graphs"""
        try:
            if not live_session.timestamps or not live_session.focus_scores:
                return
            
            # Convert to minutes
            start_time = live_session.start_time
            time_minutes = [(ts - start_time).total_seconds() / 60 for ts in live_session.timestamps]
            
            # Update plots
            self.focus_line.set_data(time_minutes, list(live_session.focus_scores))
            self.prod_line.set_data(time_minutes, list(live_session.productivity_scores))
            
            if time_minutes:
                max_time = max(time_minutes) + 1
                self.ax1.set_xlim(0, max_time)
                self.ax2.set_xlim(0, max_time)
            
            # Refresh canvas
            self.canvas_widget.draw_idle()
            
        except Exception as e:
            print(f"Graph update error: {e}")

    def open_linkedin(self, event=None):
        """Open LinkedIn profile"""
        webbrowser.open("https://linkedin.com/in/hajrah-saleha-kazi")

    def start_tracking(self):
        """Start tracking session"""
        try:
            self.tracker.start_tracking()
            
            # Update UI
            self.btn_start_tracking.config(
                text="🔴 TRACKING ACTIVE",
                bg=self.colors['warning'],
                state='disabled'
            )
            self.btn_stop_tracking.config(
                state='normal',
                bg=self.colors['live_danger']
            )
            
            messagebox.showinfo(
                "Tracking Started! 🎉",
                "🚀 FocusPulse Elite is now monitoring your productivity!\n\nWatch the live graphs update as you work. Use the STOP button when ready! ✨\n\nCrafted by Hajrah Saleha Kazi"
            )
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not start tracking: {e}")

    def stop_tracking(self):
        """Stop tracking session"""
        try:
            self.tracker.stop_tracking()
            
            # Update UI
            self.btn_start_tracking.config(
                text="▶️  START TRACKING",
                bg=self.colors['live_success'],
                state='normal'
            )
            self.btn_stop_tracking.config(
                state='disabled',
                bg=self.colors['text_light']
            )
            
            messagebox.showinfo(
                "Session Completed! 🌟",
                "Outstanding work! Your productivity session has been completed and analyzed.\n\nGreat job on your focused work! 🎯\n\nCrafted by Hajrah Saleha Kazi"
            )
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not stop tracking: {e}")

    def export_data(self):
        """Export productivity data"""
        try:
            filename = self.tracker.export_enhanced_data("csv", days=30)
            if filename:
                messagebox.showinfo(
                    "Export Successful! 💾",
                    f"Your data has been exported to: {filename}\n\nAnalyze your patterns and keep optimizing! 📊\n\nCrafted by Hajrah Saleha Kazi"
                )
            else:
                messagebox.showwarning(
                    "No Data Available",
                    "No data found for export.\nStart tracking sessions to build your analytics! 🚀"
                )
        except Exception as e:
            messagebox.showerror("Export Error", f"Could not export data: {e}")

    def on_closing(self):
        """Handle app closing"""
        try:
            if self.tracker.is_tracking:
                self.tracker.stop_tracking()
            
            plt.close('all')
            self.root.destroy()
            
        except Exception as e:
            print(f"Shutdown error: {e}")
            self.root.destroy()

    def run(self):
        """Launch the application"""
        try:
            print("🚀 Launching FocusPulse Elite...")
            self.root.mainloop()
        except Exception as e:
            print(f"Application error: {e}")

# === MAIN ENTRY POINT ===
def main():
    """Launch FocusPulse Elite"""
    try:
        print("🚀 FocusPulse Elite - The Ultimate Masterpiece")
        print("=" * 70)
        print("Built with ❤️ by Hajrah Saleha Kazi")
        print("LinkedIn: https://linkedin.com/in/hajrah-saleha-kazi")
        print("=" * 70)
        print("✨ Features:")
        print("   🎯 Real-time productivity tracking")
        print("   📊 Live graphs and analytics")
        print("   🧠 AI-powered insights")
        print("   🎨 Professional UI with fixed layout")
        print("   ⏹️ Prominent START/STOP controls")
        print("=" * 70)
        
        app = UltimateMasterpieceGUI()
        app.run()
        
    except Exception as e:
        print(f"❌ Error launching app: {e}")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
