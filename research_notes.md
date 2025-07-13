
## Research Notes: Automated File Organization Tools for Windows

### Overview of Tools:

**1. Easy File Organizer:**
- Simple GUI with color-coded charts.
- Organizes files by type, size, date, etc.
- Easy rule creation with dropdown menus (no coding required).
- Can export/import rules.
- Free version limits transfers to 30 files; paid version offers unlimited transfers and additional tools (Smart File Renamer).

**2. File Juggler:**
- Monitors folders at set durations.
- Organizes files based on user-defined rules (size, type, name, attributes).
- Can rename files, send to recycle bin, change extensions.
- User-friendly interface with dropdown menus for variables and locations.
- 30-day free trial; paid version available.

**3. DropIT:**
- Runs in the background with a tiny icon for drag-and-drop.
- Organizes files based on 'associations' (rules).
- Supports various functions: join, split, upload, create galleries, move files.
- Easy association creation; can use preset profiles (e.g., Eraser, Gallery Maker).

**4. Digital Janitor:**
- Offers manual, automated, and scheduled organization.
- Sorts files by extension, keywords, size.
- 'Sort Music' feature to organize by artist/album.
- Scheduler for daily/weekly sorting.
- 'Automate' feature groups files by type, extension, name.
- Free, but basic functionality.

**5. WatchDirectory:**
- Feature-packed with automated file-sorting functions.
- Rules for copying, deleting, renaming, sorting files.
- Quick access to Windows utilities (Control Panel, Event Viewer, Windows Services).
- Plugins for file compression, thumbnail creation.
- 30-day free trial; paid professional license.

### Key Takeaways for System Design:
- **Rule-based Automation:** Most effective tools rely on user-defined rules for file organization. Our system should have a robust and flexible rule engine.
- **Metadata and Content Analysis:** Tools leverage file attributes (type, size, date, name) and some content (music tags, keywords). For images and videos, deeper analysis (themes, metadata, content) will be crucial.
- **User Interface:** A user-friendly interface for rule creation, monitoring, and configuration is essential.
- **Scheduling and Monitoring:** The ability to schedule tasks and monitor progress is a common and valuable feature.
- **Duplicate Detection:** Mentioned as a feature in some tools (e.g., File Juggler, tfeldmann/organize GitHub project).
- **Categorization:** The ability to categorize content (work, course, personal) will require a flexible tagging or rule system.

Next, I will research best practices for file organization and delve deeper into image and video analysis techniques.


## System Architecture Design for File Organization Agent

### High-Level Architecture

The file organization agent will follow a modular architecture to ensure scalability, maintainability, and extensibility. The core components will include:

1.  **File System Scanner:** Responsible for traversing the file system, identifying new or modified files, and extracting basic file system metadata.
2.  **Metadata Extractor:** A module dedicated to extracting rich metadata from various file types, including images (EXIF data, themes, content), videos (keyframes, duration, content), and documents.
3.  **Content Analyzer:** This module will perform deeper analysis on file content, such as text extraction from documents, visual content analysis for images, and scene detection for videos. It will also be responsible for generating content hashes for duplicate detection.
4.  **Duplicate Detector:** Compares file hashes and other metadata to identify and report duplicate files.
5.  **Categorization Engine:** Applies user-defined rules and potentially machine learning models to categorize files into predefined categories (e.g., work, course, personal) and suggest new categories.
6.  **Rule Engine & Automation:** Interprets and executes user-defined rules for file organization (moving, renaming, deleting, tagging). This module will also handle scheduled tasks.
7.  **Recommendation Engine:** Based on user behavior and categorization patterns, this module will suggest optimal organization strategies and rule refinements.
8.  **User Interface (UI) & Configuration:** Provides a graphical interface for users to configure rules, view scan results, manage categories, and initiate organization tasks.
9.  **Database/Storage:** A persistent layer to store file metadata, categorization rules, user preferences, and historical data.

### Data Structures

To effectively manage and organize files, several key data structures will be required:

#### 1. File Metadata Object

Each file processed by the agent will have an associated metadata object. This object will store comprehensive information about the file.

```json
{
  "file_id": "unique_identifier",
  "path": "C:\\Users\\User\\Downloads\\document.pdf",
  "name": "document.pdf",
  "extension": ".pdf",
  "size": 102400, // in bytes
  "creation_time": "2023-07-13T10:00:00Z",
  "modification_time": "2023-07-13T11:30:00Z",
  "last_access_time": "2023-07-13T12:00:00Z",
  "hash_md5": "abcdef1234567890abcdef1234567890", // for duplicate detection
  "category": ["personal", "documents"], // e.g., work, course, personal, documents, images, videos
  "tags": ["invoice", "2023", "important"], // user-defined tags
  "image_metadata": {
    "make": "Canon",
    "model": "EOS 5D Mark IV",
    "date_taken": "2023-06-15T14:20:00Z",
    "resolution": "6000x4000",
    "keywords": ["landscape", "mountain", "sunset"], // extracted from image content/AI
    "dominant_colors": ["#FF0000", "#00FF00"],
    "themes": ["nature", "travel"]
  },
  "video_metadata": {
    "duration": 3600, // in seconds
    "codec": "H.264",
    "resolution": "1920x1080",
    "keyframes": ["path/to/keyframe1.jpg", "path/to/keyframe2.jpg"],
    "scenes": ["skiing_downhill", "ski_jump"], // e.g., for ski videos
    "audio_track_info": ""
  },
  "document_metadata": {
    "author": "John Doe",
    "title": "Project Proposal",
    "word_count": 5000,
    "summary": "Brief summary of document content."
  },
  "recommendations": [
    "Move to C:\\Users\\User\\Documents\\Invoices",
    "Rename to 2023_Invoice_ABC.pdf"
  ]
}
```

#### 2. Categorization Rule Object

Rules will define how files are categorized and organized. These rules will be user-configurable.

```json
{
  "rule_id": "rule_001",
  "name": "Organize Downloads",
  "description": "Moves PDF files from Downloads to Documents/PDFs",
  "conditions": [
    {"field": "path", "operator": "contains", "value": "Downloads"},
    {"field": "extension", "operator": "equals", "value": ".pdf"}
  ],
  "actions": [
    {"type": "move", "destination": "C:\\Users\\User\\Documents\\PDFs"},
    {"type": "add_tag", "tag": "processed_download"}
  ],
  "priority": 10,
  "enabled": true
}
```

#### 3. User Preferences & Configuration

This will store global settings and user-specific configurations.

```json
{
  "scan_directories": ["C:\\Users\\User\\Downloads", "C:\\Users\\User\\Pictures"],
  "exclude_directories": ["C:\\Windows", "C:\\Program Files"],
  "duplicate_action": "report_only", // or "move_to_quarantine", "delete_oldest"
  "default_categories": {
    "images": "C:\\Users\\User\\Pictures\\Organized",
    "videos": "C:\\Users\\User\\Videos\\Organized",
    "documents": "C:\\Users\\User\\Documents\\Organized"
  },
  "custom_categories": [
    {"name": "Work", "path": "C:\\Users\\User\\Documents\\Work"},
    {"name": "Course", "path": "C:\\Users\\User\\Documents\\Courses"},
    {"name": "Personal", "path": "C:\\Users\\User\\Documents\\Personal"}
  ],
  "scheduling": {
    "enabled": true,
    "frequency": "daily",
    "time": "03:00"
  }
}
```

This detailed design provides a solid foundation for developing the file organization agent. The next step will be to develop the core file scanning and analysis modules.


### Image and Video Analysis Libraries

**Image Analysis:**

*   **Pillow (PIL Fork):** Excellent for basic image manipulation and, crucially, for extracting EXIF metadata from images. This will be the primary library for reading image metadata.
*   **OpenCV (cv2):** A comprehensive computer vision library. It can be used for more advanced image analysis, such as identifying dominant colors, and potentially for object detection to identify themes (e.g., detecting a 'mountain' or 'sunset').
*   **ImageAI:** A high-level library built on top of TensorFlow and Keras, which could be used for more complex image content analysis and theme detection if required. It offers pre-trained models for object detection and image prediction.

**Video Analysis:**

*   **PySceneDetect:** A dedicated library for scene detection in videos. This will be perfect for breaking down ski videos into individual scenes or runs.
*   **Katna:** A library for keyframe extraction. This will be useful for creating representative thumbnails for video files and for analyzing the content of the video without processing every single frame.
*   **OpenCV (cv2):** Can also be used for video processing, including frame-by-frame analysis, which could be useful for more detailed analysis of ski videos if needed.

Based on this research, I will proceed with integrating Pillow for image metadata extraction and PySceneDetect for video scene detection into the file scanner. I will also use OpenCV for more advanced image and video analysis if required.

