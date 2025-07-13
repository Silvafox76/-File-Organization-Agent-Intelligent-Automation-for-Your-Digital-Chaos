# Quick Start Guide

## File Organization Agent - Get Started in 5 Minutes

### Prerequisites
- Windows 10/11 or Linux/macOS
- Python 3.11 or later installed
- 4 GB RAM minimum
- Internet connection for initial setup

### Installation (Windows)

1. **Download** the File Organization Agent package
2. **Extract** the ZIP file to your desired location (e.g., `C:\FileOrganizer`)
3. **Open Command Prompt** as Administrator
4. **Navigate** to the installation directory: `cd C:\FileOrganizer`
5. **Run installer**: `install.bat`
6. **Wait** for installation to complete (2-3 minutes)

### Installation (Linux/macOS)

1. **Download** the File Organization Agent package
2. **Extract** the archive to your desired location
3. **Open Terminal**
4. **Navigate** to the installation directory: `cd /path/to/FileOrganizer`
5. **Run installer**: `./install.sh`
6. **Wait** for installation to complete (2-3 minutes)

### First Run

#### Windows
1. **Double-click** `start.bat` or run it from Command Prompt
2. **Wait** for the application to start (30 seconds)
3. **Open browser** to `http://localhost:5000`

#### Linux/macOS
1. **Run** `./start.sh` from Terminal
2. **Wait** for the application to start (30 seconds)
3. **Open browser** to `http://localhost:5000`

### Quick Test

1. **Click** "Scan Files" tab
2. **Enter** a test directory path (e.g., `C:\Users\YourName\Downloads`)
3. **Click** "Scan" button
4. **Review** the discovered files and their metadata

### Basic Organization

1. **Click** "Organize" tab
2. **Create a simple rule**:
   - Rule name: "Move PDFs"
   - Condition: File Extension equals ".pdf"
   - Action: Move to "C:\Users\YourName\Documents\PDFs"
3. **Click** "Apply Rules"
4. **Check** the results to see organized files

### Find Duplicates

1. **Click** "Duplicates" tab
2. **Click** "Find Duplicates"
3. **Review** any duplicate files found
4. **Decide** which duplicates to keep or remove

### Get Recommendations

1. **Click** "Recommendations" tab
2. **Click** "Get Recommendations"
3. **Review** suggested organization strategies
4. **Implement** recommendations by creating rules

### Stopping the Application

- **Windows**: Close the Command Prompt window or press `Ctrl+C`
- **Linux/macOS**: Press `Ctrl+C` in the Terminal

### Troubleshooting

**Application won't start?**
- Verify Python 3.11+ is installed: `python --version`
- Check if port 5000 is available
- Run installation again: `install.bat` or `./install.sh`

**Can't access web interface?**
- Try `http://127.0.0.1:5000` instead of `localhost`
- Check Windows Firewall settings
- Ensure no other application is using port 5000

**Slow performance?**
- Start with smaller directories (< 1000 files)
- Close other applications to free memory
- Use SSD storage for better performance

### Next Steps

1. **Read** the full `README.md` for detailed documentation
2. **Configure** categorization keywords in the Configuration tab
3. **Create** custom organization rules for your specific needs
4. **Set up** regular organization schedules
5. **Backup** your configuration and rules

### Support

For detailed documentation, troubleshooting, and advanced features, refer to the complete `README.md` file included with the application.

---

**Congratulations!** You now have a powerful file organization system running on your computer. Start with small test directories and gradually expand to larger file collections as you become familiar with the system.

