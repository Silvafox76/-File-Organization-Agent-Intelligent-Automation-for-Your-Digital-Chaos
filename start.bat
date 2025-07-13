@echo off
echo ========================================
echo Starting File Organization Agent
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found
    echo Please run install.bat first
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Start the application
echo Starting the File Organization Agent...
echo Web interface will be available at: http://localhost:5000
echo.
echo Press Ctrl+C to stop the application
echo.
python src\main.py

