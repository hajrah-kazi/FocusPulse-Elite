# Installation script
#!/usr/bin/env python3

"""
Setup script for FocusPulse Elite
Built with ❤️ by Hajrah Saleha Kazi
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="focuspulse-elite",
    version="4.2.0",
    author="Hajrah Saleha Kazi",
    author_email="hajrah.kazi@example.com",
    description="The Ultimate Masterpiece Productivity Analytics Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hajrahkazi/focuspulse-elite",
    project_urls={
        "LinkedIn": "https://linkedin.com/in/hajrah-saleha-kazi",
        "Bug Tracker": "https://github.com/hajrahkazi/focuspulse-elite/issues",
        "Documentation": "https://github.com/hajrahkazi/focuspulse-elite/wiki",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business :: Scheduling",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Natural Language :: English",
    ],
    keywords="productivity, tracking, analytics, focus, time-management, gui, tkinter",
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.5.0",
        "numpy>=1.21.0",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.0",
        "psutil>=5.8.0",
        "scikit-learn>=1.0.0",
        "pywin32>=304;platform_system=='Windows'",
        "pynput>=1.7.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.910",
        ],
        "build": [
            "pyinstaller>=4.0",
            "cx-freeze>=6.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "focuspulse=focuspulse.main:main",
            "focuspulse-elite=focuspulse.main:main",
        ],
        "gui_scripts": [
            "focuspulse-gui=focuspulse.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "focuspulse": [
            "assets/*",
            "data/*",
            "config/*",
        ],
    },
    zip_safe=False,
    platforms=["any"],
    license="MIT",
    
    # Additional metadata
    maintainer="Hajrah Saleha Kazi",
    maintainer_email="hajrah.kazi@example.com",
    
    # Options for different install scenarios
    options={
        "build_exe": {
            "packages": ["tkinter", "matplotlib", "pandas", "numpy"],
            "include_files": ["README.md", "LICENSE"],
        }
    },
    
    # Custom commands
    cmdclass={},
    
    # Data files for system-wide installation
    data_files=[
        ("share/applications", ["focuspulse.desktop"]) if os.name != 'nt' else (),
        ("share/pixmaps", ["assets/icons/focuspulse.png"]) if os.name != 'nt' else (),
    ],
)

# Post-install message
print("""
🚀 FocusPulse Elite Installation Complete!

✨ Features Installed:
   🎯 Real-time productivity tracking
   📊 Live graphs and analytics  
   🧠 AI-powered insights
   🎨 Professional UI with fixed layout
   ⏹️ Prominent START/STOP controls

🌟 Built with ❤️ by Hajrah Saleha Kazi
   LinkedIn: https://linkedin.com/in/hajrah-saleha-kazi

📖 Quick Start:
   Run: focuspulse
   Or:  python -m focuspulse

📚 Documentation: https://github.com/hajrahkazi/focuspulse-elite/wiki

Thank you for choosing FocusPulse Elite! 🎉
""")
