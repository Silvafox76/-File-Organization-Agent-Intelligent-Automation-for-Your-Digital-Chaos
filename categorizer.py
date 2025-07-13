import os

def categorize_file(file_info, rules):
    category = []
    file_path = file_info["path"].lower()
    file_name = file_info["name"].lower()

    for cat, keywords in rules.items():
        for keyword in keywords:
            if keyword in file_path or keyword in file_name:
                category.append(cat)
                break
    
    if not category:
        category.append("uncategorized")

    return list(set(category)) # Return unique categories

def apply_categorization(scanned_files, categorization_rules):
    for file_info in scanned_files:
        file_info["category"] = categorize_file(file_info, categorization_rules)
    return scanned_files

if __name__ == "__main__":
    # Dummy data for testing
    dummy_files = [
        {"name": "report_q3.docx", "path": "C:\\Users\\User\\Documents\\Work\\Reports\\report_q3.docx", "extension": ".docx"},
        {"name": "lecture_notes_math.pdf", "path": "C:\\Users\\User\\Documents\\Courses\\Math\\lecture_notes_math.pdf", "extension": ".pdf"},
        {"name": "vacation_pics_2024.jpg", "path": "C:\\Users\\User\\Pictures\\Personal\\Vacation\\vacation_pics_2024.jpg", "extension": ".jpg"},
        {"name": "random_download.zip", "path": "C:\\Users\\User\\Downloads\\random_download.zip", "extension": ".zip"},
        {"name": "project_plan.pptx", "path": "C:\\Users\\User\\Documents\\Work\\project_plan.pptx", "extension": ".pptx"},
        {"name": "course_syllabus.pdf", "path": "C:\\Users\\User\\Downloads\\course_syllabus.pdf", "extension": ".pdf"}
    ]

    categorization_rules = {
        "work": ["work", "report", "project", "business"],
        "course": ["course", "lecture", "syllabus", "assignment"],
        "personal": ["personal", "vacation", "photo", "family"]
    }

    categorized_files = apply_categorization(dummy_files, categorization_rules)

    print("--- Categorized Files ---")
    for file_info in categorized_files:
        print(f"File: {file_info['name']}\n  Path: {file_info['path']}\n  Category: {file_info['category']}\n")

    # Test with actual files using file_scanner.py (assuming it's available)
    print("\n--- Testing with actual scanned files and categorization ---")
    try:
        from file_scanner import scan_directory
        from duplicate_detector import find_duplicates # Not directly used here, but good to have for context

        test_directory = "./test_files"
        # Create some files for categorization testing
        with open(os.path.join(test_directory, "work_document.docx"), "w") as f:
            f.write("This is a work related document.")
        with open(os.path.join(test_directory, "course_material.pdf"), "w") as f:
            f.write("This is course material.")
        with open(os.path.join(test_directory, "personal_photo.jpg"), "w") as f:
            f.write("This is a personal photo.")

        scanned_files_for_categorization = scan_directory(test_directory)
        categorized_actual_files = apply_categorization(scanned_files_for_categorization, categorization_rules)

        print("\n--- Actual Scanned and Categorized Files ---")
        for file_info in categorized_actual_files:
            print(f"File: {file_info['name']}\n  Path: {file_info['path']}\n  Category: {file_info['category']}\n")

    except ImportError:
        print("Could not import file_scanner.py or duplicate_detector.py. Please ensure they are in the same directory.")
    except Exception as e:
        print(f"An error occurred during actual file scanning and categorization: {e}")


