#!/usr/bin/env python3
"""
Setup script for Steam Stats EDA Dashboard project.
Run this script to initialize the project environment.
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is 3.8 or higher."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required.")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version}")
    return True

def install_requirements():
    """Install required packages."""
    print("📦 Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements")
        return False

def create_config_file():
    """Create config.py from template."""
    config_template = Path("config/config_template.py")
    config_file = Path("config/config.py")
    
    if config_template.exists() and not config_file.exists():
        with open(config_template, 'r') as template:
            content = template.read()
        
        with open(config_file, 'w') as config:
            config.write(content)
        
        print("✅ Created config/config.py from template")
        print("📝 Please edit config/config.py with your specific settings")
    else:
        print("ℹ️  Config file already exists or template not found")

def verify_structure():
    """Verify that all necessary directories exist."""
    required_dirs = [
        "data/raw",
        "data/processed", 
        "data/external",
        "notebooks",
        "src/data",
        "src/features",
        "src/models",
        "src/visualization",
        "dashboards",
        "config",
        "tests",
        "docs"
    ]
    
    missing_dirs = []
    for directory in required_dirs:
        if not Path(directory).exists():
            missing_dirs.append(directory)
    
    if missing_dirs:
        print(f"❌ Missing directories: {missing_dirs}")
        return False
    else:
        print("✅ All required directories exist")
        return True

def display_next_steps():
    """Display next steps for the user."""
    print("\n🎉 Setup complete! Next steps:")
    print("1. Download a Steam dataset from Kaggle")
    print("2. Place the dataset in data/raw/ directory")
    print("3. Update the dataset filename in config/config.py")
    print("4. Run the EDA notebook: jupyter notebook notebooks/01_steam_eda.ipynb")
    print("5. Launch the dashboard: streamlit run dashboards/streamlit_app.py")
    print("\n📚 For more information, see README.md and docs/project_structure.md")

def main():
    """Main setup function."""
    print("🚀 Setting up Steam Stats EDA Dashboard...")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    # Create config file
    create_config_file()
    
    # Verify project structure
    if not verify_structure():
        print("❌ Project structure verification failed")
        return
    
    # Display next steps
    display_next_steps()

if __name__ == "__main__":
    main()