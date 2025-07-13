import os

def generate_recommendations(scanned_files, categorization_rules):
    recommendations = []

    # Recommendation 1: Suggest moving uncategorized files to a review folder
    uncategorized_files = [f for f in scanned_files if "uncategorized" in f.get("category", [])]
    if uncategorized_files:
        recommendations.append({
            "type": "move_to_review",
            "description": "Consider moving these files to a \'Review\' folder for manual categorization.",
            "files": [f["path"] for f in uncategorized_files]
        })

    # Recommendation 2: Suggest refining categorization rules based on existing categories and file types
    # This is a simplified example; a real recommendation engine would use more advanced logic
    for file_info in scanned_files:
        if file_info["extension"] in [".jpg", ".png"] and "personal" not in file_info.get("category", []):
            recommendations.append({
                "type": "suggest_category_image",
                "description": f"Image file {file_info['name']} might be personal. Consider adding a rule for images.",
                "file": file_info["path"],
                "suggested_category": "personal"
            })
        elif file_info["extension"] in [".docx", ".pptx", ".xlsx"] and "work" not in file_info.get("category", []):
            recommendations.append({
                "type": "suggest_category_document",
                "description": f"Document file {file_info['name']} might be work-related. Consider adding a rule for documents.",
                "file": file_info["path"],
                "suggested_category": "work"
            })
        elif file_info["extension"] in [".mp4", ".mov"] and "ski" not in file_info.get("category", []) and "video_metadata" in file_info:
            # This is a very basic check, more advanced content analysis would be needed for \'ski\' theme
            recommendations.append({
                "type": "suggest_category_video",
                "description": f"Video file {file_info['name']} might be a ski video. Consider adding a rule for ski videos.",
                "file": file_info["path"],
                "suggested_category": "ski"
            })

    return recommendations

if __name__ == "__main__":
    # Dummy data for testing
    dummy_files = [
        {"name": "report_q3.docx", "path": "C:\\Users\\User\\Documents\\Work\\Reports\\report_q3.docx", "extension": ".docx", "category": ["work"]},
        {"name": "lecture_notes_math.pdf", "path": "C:\\Users\\User\\Documents\\Courses\\Math\\lecture_notes_math.pdf", "extension": ".pdf", "category": ["course"]},
        {"name": "vacation_pics_2024.jpg", "path": "C:\\Users\\User\\Pictures\\Personal\\Vacation\\vacation_pics_2024.jpg", "extension": ".jpg", "category": ["personal"]},
        {"name": "random_download.zip", "path": "C:\\Users\\User\\Downloads\\random_download.zip", "extension": ".zip", "category": ["uncategorized"]},
        {"name": "project_plan.pptx", "path": "C:\\Users\\User\\Documents\\Work\\project_plan.pptx", "extension": ".pptx", "category": ["work"]},
        {"name": "my_ski_trip.mp4", "path": "C:\\Users\\User\\Videos\\my_ski_trip.mp4", "extension": ".mp4", "category": ["uncategorized"], "video_metadata": {"duration": 120}},
        {"name": "another_image.png", "path": "C:\\Users\\User\\Pictures\\another_image.png", "extension": ".png", "category": ["uncategorized"]}
    ]

    categorization_rules = {
        "work": ["work", "report", "project", "business"],
        "course": ["course", "lecture", "syllabus", "assignment"],
        "personal": ["personal", "vacation", "photo", "family"],
        "ski": ["ski", "snowboard", "mountain"]
    }

    recommendations = generate_recommendations(dummy_files, categorization_rules)

    print("--- Generated Recommendations ---")
    if recommendations:
        for rec in recommendations:
            print(f"Type: {rec['type']}\n  Description: {rec['description']}")
            if "files" in rec: print(f"  Files: {rec['files']}")
            if "file" in rec: print(f"  File: {rec['file']}")
            if "suggested_category" in rec: print(f"  Suggested Category: {rec['suggested_category']}")
            print("\n")
    else:
        print("No recommendations generated.")

    # Test with actual files using file_scanner.py and categorizer.py
    print("\n--- Testing with actual scanned, categorized files and recommendations ---")
    try:
        from file_scanner import scan_directory
        from categorizer import apply_categorization

        test_directory = "./test_files"
        # Ensure test files are present from previous steps

        scanned_files_for_rec = scan_directory(test_directory)
        categorized_actual_files_for_rec = apply_categorization(scanned_files_for_rec, categorization_rules)
        actual_recommendations = generate_recommendations(categorized_actual_files_for_rec, categorization_rules)

        print("\n--- Actual Recommendations ---")
        if actual_recommendations:
            for rec in actual_recommendations:
                print(f"Type: {rec['type']}\n  Description: {rec['description']}")
                if "files" in rec: print(f"  Files: {rec['files']}")
                if "file" in rec: print(f"  File: {rec['file']}")
                if "suggested_category" in rec: print(f"  Suggested Category: {rec['suggested_category']}")
                print("\n")
        else:
            print("No recommendations generated for actual files.")

    except ImportError:
        print("Could not import file_scanner.py or categorizer.py. Please ensure they are in the same directory.")
    except Exception as e:
        print(f"An error occurred during actual file scanning, categorization, and recommendation: {e}")


