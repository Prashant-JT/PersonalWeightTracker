@echo off
REM Setup script for Personal Weight Tracker (Windows)
REM This script creates a virtual environment and installs dependencies

echo 🚀 Setting up Personal Weight Tracker environment...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    exit /b 1
)

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo ✅ Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo 📥 Installing dependencies from requirements.txt...
pip install -r requirements.txt

REM Create .env file if it doesn't exist
if not exist .env (
    echo 📝 Creating .env file from .env.example...
    copy .env.example .env
    echo ✅ .env file created. Please edit it with your settings.
) else (
    echo ℹ️  .env file already exists.
)

echo.
echo ✅ Setup complete!
echo.
echo To activate the virtual environment, run:
echo   venv\Scripts\activate
echo.
echo To run the application, use:
echo   streamlit run Home.py
echo.
echo To deactivate the virtual environment, run:
echo   deactivate

pause

@REM Made with Bob
