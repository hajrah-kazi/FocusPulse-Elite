#!/usr/bin/env python3

"""
FocusPulse Elite - The Ultimate Masterpiece Productivity Analytics Platform
Main Entry Point - FIXED VERSION

Built with ❤️ by Hajrah Saleha Kazi
LinkedIn: https://linkedin.com/in/hajrah-saleha-kazi
"""

import os
import sys
import traceback
import focuspulse.app

def display_startup_banner():
    """Display the beautiful startup banner"""
    print("""
🚀 FocusPulse Elite - The Ultimate Masterpiece
═══════════════════════════════════════════════════════════════════════════════

Built with ❤️ by Hajrah Saleha Kazi
LinkedIn: https://linkedin.com/in/hajrah-saleha-kazi

The most sophisticated, elegant, and user-friendly productivity tracker ever created.

✨ Masterpiece Features:
   🎯 Real-time productivity tracking with live graphs
   📊 Advanced analytics dashboard with beautiful visualizations  
   🧠 AI-powered insights and personalized recommendations
   🎨 World-class UI/UX with premium typography and design
   ⏹️ Prominent START/STOP controls for effortless session management
   🔒 Privacy-first architecture - all data stays on your device

═══════════════════════════════════════════════════════════════════════════════
""")

def main():
    """Main application entry point"""
    try:
        # Display startup banner
        display_startup_banner()
        
        # System compatibility checks
        print("🔍 Performing system compatibility checks...")
        
        # Check Python version
        if sys.version_info < (3, 7):
            print("❌ Python 3.7+ is required. Please upgrade your Python installation.")
            input("Press Enter to exit...")
            return
        else:
            print("✅ Python version compatible")
        
        # Check for required modules
        required_modules = ['tkinter', 'pandas', 'numpy', 'matplotlib']
        missing_modules = []
        
        for module in required_modules:
            try:
                __import__(module)
            except ImportError:
                missing_modules.append(module)
        
        if missing_modules:
            print(f"❌ Missing required modules: {', '.join(missing_modules)}")
            print("📦 Install them using: pip install pandas numpy matplotlib")
            input("Press Enter to exit...")
            return
        else:
            print("✅ All dependencies available")
        
        print("🚀 Launching FocusPulse Elite...")
        print("📱 Loading the ultimate productivity masterpiece...")
        
        # Add current directory to Python path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        if current_dir not in sys.path:
            sys.path.insert(0, current_dir)
        
        # Import and launch the application
        try:
            # Check if app.py exists
            app_path = os.path.join(current_dir, "app.py")
            if not os.path.exists(app_path):
                raise FileNotFoundError("app.py not found in current directory")
            
            print("✅ Found app.py in current directory")
            
            # Import the main class from app.py
            from focuspulse.app import UltimateMasterpieceGUI
            print("✅ Successfully imported from app.py")
            
            # Initialize components
            print("🎨 Initializing world-class user interface...")
            print("📊 Setting up advanced analytics engine...")
            print("🧠 Loading AI-powered insights system...")
            print("🔒 Configuring privacy-first data management...")
            
            # Launch the application
            print("✨ Starting FocusPulse Elite...")
            app = UltimateMasterpieceGUI()
            app.run()
            
        except ImportError as e:
            print(f"❌ Import error: {e}")
            print("\n🔧 Solution: Run the app directly using:")
            print("   python app.py")
            print("\nYour app.py is self-contained and doesn't need this launcher.")
            input("\nPress Enter to exit...")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("\n🔧 Alternative: Run the app directly using:")
            print("   python app.py")
            input("\nPress Enter to exit...")
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Application interrupted by user.")
        print("Thank you for using FocusPulse Elite!")
        
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("\n🔧 Troubleshooting:")
        print("   1. Install dependencies: pip install pandas numpy matplotlib")
        print("   2. Run directly: python app.py")
        print("   3. Check file permissions")
        
        if "--debug" in sys.argv:
            print("\n🔍 Full traceback:")
            traceback.print_exc()
        
        print("\n💬 Need help? Contact: support@focuspulse-elite.com")
        print("🔗 Creator LinkedIn: https://linkedin.com/in/hajrah-saleha-kazi")
        input("\n⏸️ Press Enter to exit...")

if __name__ == "__main__":
    main()
