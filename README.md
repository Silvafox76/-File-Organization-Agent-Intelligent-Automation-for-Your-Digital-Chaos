# File Organization Agent

## Overview

The File Organization Agent is a comprehensive, intelligent file management system designed specifically for Windows computers. This powerful tool automates the tedious process of organizing files, categorizing content, and maintaining a clean digital workspace. Built with advanced machine learning capabilities and an intuitive web-based interface, the system can scan directories, analyze file content, detect duplicates, and provide intelligent recommendations for file organization.

## Key Features

### Intelligent File Scanning
- **Comprehensive Directory Traversal**: Recursively scans any specified directory structure
- **Metadata Extraction**: Automatically extracts file metadata including creation dates, modification times, file sizes, and extensions
- **Content Analysis**: Analyzes file content to determine appropriate categorization
- **Hash-based Identification**: Generates MD5 hashes for reliable duplicate detection

### Advanced Categorization System
- **Work Content Detection**: Automatically identifies work-related documents, reports, and business files
- **Course Material Organization**: Recognizes educational content, lecture notes, and academic materials
- **Personal File Management**: Categorizes personal photos, videos, and documents
- **Ski Video Optimization**: Specialized handling for ski and snowboard videos with keyframe extraction

### Duplicate Detection and Management
- **Hash-based Comparison**: Uses cryptographic hashing to identify exact duplicates
- **Size and Name Analysis**: Provides additional duplicate detection methods
- **Intelligent Recommendations**: Suggests which duplicates to keep or remove
- **Batch Processing**: Handles large numbers of files efficiently

### Rule-based Automation
- **Flexible Rule Engine**: Create custom rules based on file properties
- **Multiple Actions**: Support for moving, renaming, tagging, and deleting files
- **Conditional Logic**: Complex condition matching with multiple operators
- **Batch Application**: Apply rules to entire file collections

### Web-based Interface
- **Modern Design**: Clean, responsive interface that works on desktop and mobile
- **Real-time Updates**: Live progress tracking and status updates
- **Configuration Management**: Easy-to-use settings and rule configuration
- **Visual Feedback**: Clear results display with detailed file information

## System Requirements

### Minimum Requirements
- **Operating System**: Windows 10 or later (primary target), Linux (development/testing)
- **Python**: Python 3.11 or later
- **Memory**: 4 GB RAM minimum, 8 GB recommended
- **Storage**: 1 GB free space for installation
- **Network**: Internet connection for initial setup and updates

### Recommended Requirements
- **Operating System**: Windows 11
- **Python**: Python 3.11+
- **Memory**: 16 GB RAM for large file collections
- **Storage**: SSD with 10 GB free space
- **Processor**: Multi-core CPU for faster processing

## Installation Guide

### Prerequisites Installation

Before installing the File Organization Agent, ensure you have Python 3.11 or later installed on your system.

#### Installing Python on Windows
1. Download Python from the official website: https://www.python.org/downloads/
2. Run the installer and ensure "Add Python to PATH" is checked
3. Verify installation by opening Command Prompt and typing: `python --version`

#### Installing Git (Optional but Recommended)
1. Download Git from: https://git-scm.com/download/win
2. Install with default settings
3. Verify installation: `git --version`

### Application Installation

#### Method 1: Direct Download (Recommended for Users)
1. Download the latest release package from the project repository
2. Extract the ZIP file to your desired installation directory
3. Open Command Prompt as Administrator
4. Navigate to the installation directory: `cd path\to\file_organizer_app`
5. Install dependencies: `pip install -r requirements.txt`
6. Run the application: `python src\main.py`

#### Method 2: Development Installation (For Advanced Users)
1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd file_organizer_app`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
5. Install dependencies: `pip install -r requirements.txt`
6. Run the application: `python src\main.py`

### First-Time Setup

1. **Start the Application**: Run `python src\main.py` from the installation directory
2. **Access the Interface**: Open your web browser and navigate to `http://localhost:5000`
3. **Configure Settings**: Click on the "Configuration" tab to set up default categorization rules
4. **Test Scan**: Use the "Scan Files" tab to test the system with a small directory first

## User Guide

### Getting Started

#### Initial Configuration
Before using the File Organization Agent, it's important to configure the system according to your specific needs. The configuration process involves setting up categorization keywords and scan settings.

**Setting Up Categorization Keywords**:
1. Navigate to the "Configuration" tab in the web interface
2. Define keywords for each category:
   - **Work Keywords**: Terms like "report", "project", "business", "meeting", "proposal"
   - **Course Keywords**: Terms like "lecture", "assignment", "syllabus", "homework", "exam"
   - **Personal Keywords**: Terms like "vacation", "family", "photo", "personal", "birthday"
   - **Ski Keywords**: Terms like "ski", "snowboard", "mountain", "slope", "powder"
3. Click "Save Configuration" to store your settings

**Adjusting Scan Settings**:
- **Include Hidden Files**: Choose whether to scan hidden files and folders
- **Maximum Depth**: Set the maximum directory depth for recursive scanning
- **File Size Limits**: Configure minimum and maximum file sizes to process

#### Scanning Your First Directory

1. **Select Directory**: In the "Scan Files" tab, enter the path to the directory you want to organize
   - Example: `C:\Users\YourName\Downloads`
   - For testing, start with a smaller directory
2. **Initiate Scan**: Click the "Scan" button to begin the analysis process
3. **Review Results**: The system will display all discovered files with their metadata
4. **Analyze Statistics**: Review the file count and distribution statistics

### File Organization Workflow

#### Creating Organization Rules
The rule engine is the heart of the File Organization Agent. Rules define how files should be processed based on their properties.

**Rule Components**:
- **Rule Name**: A descriptive name for easy identification
- **Conditions**: Criteria that files must meet (file extension, path, name, size)
- **Operators**: How conditions are evaluated (equals, contains, greater than, less than)
- **Actions**: What to do with matching files (move, rename, tag, delete)
- **Action Values**: Specific parameters for actions (destination paths, new names, tags)

**Example Rules**:

*Rule 1: Organize PDF Documents*
- Name: "Move PDFs to Documents"
- Condition: File Extension equals ".pdf"
- Action: Move to "C:\Users\YourName\Documents\PDFs"

*Rule 2: Archive Old Files*
- Name: "Archive Files Older Than 1 Year"
- Condition: Modification Date less than "365 days ago"
- Action: Move to "C:\Users\YourName\Archive"

*Rule 3: Tag Work Documents*
- Name: "Tag Work Files"
- Condition: File Path contains "work"
- Action: Add Tag "work-related"

#### Applying Organization Rules
1. **Create Rules**: Use the "Organize" tab to define your organization rules
2. **Test Rules**: Start with a small subset of files to test rule effectiveness
3. **Apply Rules**: Click "Apply Rules" to execute all enabled rules
4. **Review Results**: Check the organization results to ensure files were processed correctly
5. **Refine Rules**: Modify rules based on results and apply again if needed

### Advanced Features

#### Duplicate Detection and Management
The duplicate detection system uses multiple algorithms to identify potentially duplicate files.

**Detection Methods**:
- **Hash Comparison**: Most reliable method using MD5 checksums
- **Size and Name**: Identifies files with identical sizes and similar names
- **Content Analysis**: Compares file content for near-duplicates

**Using Duplicate Detection**:
1. Navigate to the "Duplicates" tab
2. Click "Find Duplicates" to scan for duplicate files
3. Review the duplicate groups presented
4. Decide which files to keep or remove
5. Use the organization rules to automate duplicate handling

#### Intelligent Recommendations
The recommendation engine analyzes your files and suggests organization strategies.

**Recommendation Types**:
- **Category Suggestions**: Recommends appropriate categories for uncategorized files
- **Organization Patterns**: Identifies common file patterns and suggests rules
- **Cleanup Opportunities**: Highlights files that could be archived or deleted
- **Efficiency Improvements**: Suggests ways to optimize your file organization

**Using Recommendations**:
1. Go to the "Recommendations" tab
2. Click "Get Recommendations" to generate suggestions
3. Review each recommendation carefully
4. Implement suggestions by creating appropriate rules
5. Monitor the effectiveness of implemented recommendations

### Troubleshooting

#### Common Issues and Solutions

**Issue: Application Won't Start**
- **Solution**: Verify Python installation and dependencies
- **Check**: Ensure all required packages are installed: `pip install -r requirements.txt`
- **Verify**: Confirm Python version compatibility: `python --version`

**Issue: Slow Scanning Performance**
- **Solution**: Reduce scan depth or exclude large directories
- **Optimize**: Close other applications to free up system resources
- **Consider**: Scanning smaller directories in batches

**Issue: Files Not Being Categorized Correctly**
- **Solution**: Review and refine categorization keywords
- **Adjust**: Modify rule conditions to be more specific
- **Test**: Use smaller test sets to validate rule effectiveness

**Issue: Web Interface Not Accessible**
- **Solution**: Check if the application is running on the correct port
- **Verify**: Ensure no firewall is blocking port 5000
- **Try**: Access using `http://127.0.0.1:5000` instead of `localhost`

#### Performance Optimization

**For Large File Collections**:
- Process files in smaller batches
- Increase system memory allocation
- Use SSD storage for better I/O performance
- Close unnecessary applications during processing

**For Better Accuracy**:
- Regularly update categorization keywords
- Review and refine organization rules
- Monitor recommendation effectiveness
- Adjust rules based on usage patterns

## Technical Documentation

### Architecture Overview

The File Organization Agent follows a modular architecture designed for scalability, maintainability, and extensibility. The system is built using Python with a Flask web framework for the user interface and various specialized libraries for file processing and analysis.

#### Core Components

**File Scanner Module** (`file_scanner.py`):
The file scanner is responsible for traversing directory structures and extracting comprehensive metadata from discovered files. It utilizes Python's `os` and `pathlib` libraries for efficient file system navigation and implements recursive scanning with configurable depth limits.

Key features include:
- Recursive directory traversal with depth control
- Metadata extraction (size, timestamps, permissions)
- Hash generation for duplicate detection
- Error handling for inaccessible files
- Progress tracking for large scans

**Categorization Engine** (`categorizer.py`):
The categorization engine implements intelligent file classification using keyword matching, path analysis, and content inspection. It supports multiple categorization strategies and can be extended with machine learning models.

Classification methods:
- Keyword-based categorization using configurable dictionaries
- Path pattern recognition for folder-based organization
- File extension analysis for type-based categorization
- Content analysis for document classification

**Duplicate Detection System** (`duplicate_detector.py`):
The duplicate detection system employs multiple algorithms to identify potentially duplicate files with high accuracy and performance.

Detection algorithms:
- MD5 hash comparison for exact duplicates
- Size-based filtering for performance optimization
- Name similarity analysis using string matching
- Content comparison for near-duplicates

**Rule Engine** (`rule_engine.py`):
The rule engine provides a flexible framework for defining and executing file organization rules. It supports complex conditional logic and multiple action types.

Rule components:
- Condition evaluation with multiple operators
- Action execution with rollback capabilities
- Batch processing for efficiency
- Error handling and logging

**Recommendation Engine** (`recommendation_engine.py`):
The recommendation engine analyzes file patterns and user behavior to suggest optimization strategies and organization improvements.

Recommendation types:
- Category suggestions based on file analysis
- Rule recommendations based on usage patterns
- Cleanup suggestions for optimization
- Performance improvement recommendations

#### Web Interface Architecture

**Flask Application** (`src/main.py`):
The Flask application serves as the web server and API endpoint for the user interface. It implements RESTful API endpoints for all system functionality and serves the static web interface.

API endpoints:
- `/api/scan` - File scanning operations
- `/api/organize` - Rule application and organization
- `/api/duplicates` - Duplicate detection
- `/api/recommendations` - Recommendation generation
- `/api/config` - Configuration management

**Frontend Interface**:
The web interface is built using modern HTML5, CSS3, and JavaScript technologies. It provides a responsive, user-friendly interface that works across different devices and browsers.

Interface components:
- Tabbed navigation for different functions
- Real-time progress indicators
- Interactive rule builder
- Results visualization
- Configuration management

### Data Structures and Formats

#### File Metadata Structure
```python
{
    "name": "document.pdf",
    "path": "/full/path/to/document.pdf",
    "size": 1024000,
    "creation_time": "2025-01-01T12:00:00",
    "modification_time": "2025-01-02T15:30:00",
    "last_access_time": "2025-01-03T09:15:00",
    "extension": ".pdf",
    "hash_md5": "a1b2c3d4e5f6...",
    "category": ["work", "document"],
    "tags": ["important", "project-alpha"]
}
```

#### Rule Definition Format
```python
{
    "rule_id": "rule_001",
    "name": "Organize Work Documents",
    "conditions": [
        {
            "field": "path",
            "operator": "contains",
            "value": "work"
        },
        {
            "field": "extension",
            "operator": "equals",
            "value": ".docx"
        }
    ],
    "actions": [
        {
            "type": "move",
            "destination": "/organized/work/documents"
        },
        {
            "type": "add_tag",
            "tag": "work-document"
        }
    ],
    "enabled": true
}
```

#### Configuration Schema
```python
{
    "default_rules": {
        "work": ["work", "report", "project", "business"],
        "course": ["course", "lecture", "syllabus", "assignment"],
        "personal": ["personal", "vacation", "photo", "family"],
        "ski": ["ski", "snowboard", "mountain"]
    },
    "scan_settings": {
        "include_hidden": false,
        "max_depth": 10,
        "min_file_size": 0,
        "max_file_size": null
    }
}
```

### API Reference

#### Scan Endpoint
**POST /api/scan**

Initiates a file system scan of the specified directory.

Request body:
```json
{
    "directory": "/path/to/scan"
}
```

Response:
```json
{
    "files": [...],
    "count": 150
}
```

#### Organization Endpoint
**POST /api/organize**

Applies organization rules to the specified files.

Request body:
```json
{
    "files": [...],
    "rules": [...]
}
```

Response:
```json
{
    "files": [...],
    "applied_rules": 5,
    "processed_files": 150
}
```

#### Duplicate Detection Endpoint
**POST /api/duplicates**

Identifies duplicate files in the provided file list.

Request body:
```json
{
    "files": [...]
}
```

Response:
```json
{
    "duplicates": [
        {
            "hash": "a1b2c3d4...",
            "files": ["/path/1", "/path/2"],
            "size": 1024000
        }
    ]
}
```

#### Recommendations Endpoint
**POST /api/recommendations**

Generates organization recommendations based on file analysis.

Request body:
```json
{
    "files": [...],
    "rules": {...}
}
```

Response:
```json
{
    "recommendations": [
        {
            "type": "suggest_category",
            "file": "/path/to/file",
            "suggested_category": "work",
            "confidence": 0.85,
            "description": "File appears to be work-related based on content analysis"
        }
    ]
}
```

### Security Considerations

#### File System Access
The application requires read and write access to the file system for scanning and organizing files. Users should be aware of the following security considerations:

- **Permissions**: The application runs with the same permissions as the user account
- **File Access**: Only files accessible to the user account can be processed
- **Network Access**: The web interface is bound to localhost by default for security
- **Data Privacy**: File metadata is processed locally and not transmitted externally

#### Web Interface Security
- **Local Binding**: The web server binds to localhost (127.0.0.1) by default
- **No Authentication**: The interface assumes single-user local access
- **CORS Policy**: Cross-origin requests are restricted for security
- **Input Validation**: All user inputs are validated and sanitized

#### Recommended Security Practices
- Run the application with standard user privileges (not administrator)
- Regularly update Python and dependencies for security patches
- Monitor file system changes during organization operations
- Backup important files before running organization rules
- Review and test rules on small file sets before large-scale application

## Deployment and Maintenance

### Production Deployment

For production use, consider the following deployment strategies:

#### Standalone Application
Package the application as a standalone executable using tools like PyInstaller:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed src/main.py
```

#### Service Installation
Install the application as a Windows service for automatic startup:
1. Use tools like NSSM (Non-Sucking Service Manager)
2. Configure the service to start automatically
3. Set appropriate service account permissions

#### Docker Deployment
For containerized deployment:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "src/main.py"]
```

### Maintenance and Updates

#### Regular Maintenance Tasks
- **Log Review**: Monitor application logs for errors or performance issues
- **Dependency Updates**: Regularly update Python packages for security and features
- **Configuration Backup**: Backup configuration files and custom rules
- **Performance Monitoring**: Monitor system resource usage during operations

#### Update Procedures
1. **Backup**: Create backups of configuration and custom rules
2. **Test**: Test updates in a development environment first
3. **Deploy**: Apply updates during low-usage periods
4. **Verify**: Confirm functionality after updates
5. **Monitor**: Watch for issues in the first 24 hours after updates

#### Troubleshooting and Support
- **Log Files**: Check application logs for error messages
- **System Resources**: Monitor CPU, memory, and disk usage
- **Network Connectivity**: Verify web interface accessibility
- **File Permissions**: Ensure appropriate file system permissions
- **Dependency Issues**: Verify all required packages are installed correctly

This comprehensive documentation provides users and administrators with all the information needed to successfully install, configure, and operate the File Organization Agent. The system's modular design and extensive documentation ensure that it can be adapted to various use cases and environments while maintaining reliability and performance.

🙋‍♂️ Author
Ryan Dear
GitHub | LinkedIn | Email
