#!/bin/bash

echo "========================================"
echo "Starting File Organization Agent"
echo "========================================"
echo

# Check if virtual environment exists
if [ ! -f "venv/bin/activate" ]; then
    echo "ERROR: Virtual environment not found"
    echo "Please run ./install.sh first"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Start the application
echo "Starting the File Organization Agent..."
echo "Web interface will be available at: http://localhost:5000"
echo
echo "Press Ctrl+C to stop the application"
echo
python src/main.py

