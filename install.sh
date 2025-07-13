#!/bin/bash

echo "========================================"
echo "File Organization Agent Installer"
echo "========================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.11 or later"
    exit 1
fi

echo "Python found. Checking version..."
python3 -c "import sys; exit(0 if sys.version_info >= (3, 11) else 1)"
if [ $? -ne 0 ]; then
    echo "ERROR: Python 3.11 or later is required"
    echo "Please update your Python installation"
    exit 1
fi

echo "Python version is compatible."
echo

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create virtual environment"
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo
echo "========================================"
echo "Installation completed successfully!"
echo "========================================"
echo
echo "To start the File Organization Agent:"
echo "1. Run: source venv/bin/activate"
echo "2. Run: python src/main.py"
echo "3. Open your browser to: http://localhost:5000"
echo
echo "Or simply run: ./start.sh"
echo

