import os
import shutil

def apply_rule(file_info, rule):
    # Evaluate conditions
    conditions_met = True
    for condition in rule.get("conditions", []):
        field = condition["field"]
        operator = condition["operator"]
        value = condition["value"]

        file_value = file_info.get(field)

        if file_value is None:
            conditions_met = False
            break

        if operator == "equals":
            if file_value != value:
                conditions_met = False
                break
        elif operator == "contains":
            if value not in str(file_value):
                conditions_met = False
                break
        # Add more operators as needed (e.g., starts_with, ends_with, greater_than, less_than)

    if conditions_met:
        # Execute actions
        for action in rule.get("actions", []):
            action_type = action["type"]

            if action_type == "move":
                destination = action["destination"]
                try:
                    os.makedirs(destination, exist_ok=True)
                    shutil.move(file_info["path"], os.path.join(destination, file_info["name"]))
                    print(f"Moved {file_info['name']} to {destination}")
                    file_info["path"] = os.path.join(destination, file_info["name"]) # Update path in metadata
                except Exception as e:
                    print(f"Error moving {file_info['name']}: {e}")
            elif action_type == "rename":
                new_name = action["new_name"]
                try:
                    new_path = os.path.join(os.path.dirname(file_info["path"]), new_name)
                    os.rename(file_info["path"], new_path)
                    print(f"Renamed {file_info['name']} to {new_name}")
                    file_info["name"] = new_name # Update name in metadata
                    file_info["path"] = new_path # Update path in metadata
                except Exception as e:
                    print(f"Error renaming {file_info['name']}: {e}")
            elif action_type == "add_tag":
                tag = action["tag"]
                if "tags" not in file_info:
                    file_info["tags"] = []
                if tag not in file_info["tags"]:
                    file_info["tags"].append(tag)
                    print(f"Added tag \'{tag}\' to {file_info['name']}")
            elif action_type == "delete":
                try:
                    os.remove(file_info["path"])
                    print(f"Deleted {file_info['name']}")
                    file_info["path"] = "DELETED" # Mark as deleted
                except Exception as e:
                    print(f"Error deleting {file_info['name']}: {e}")
            # Add more actions as needed (e.g., copy)
    return file_info

def apply_rules_to_files(scanned_files, rules):
    processed_files = []
    for file_info in scanned_files:
        original_file_info = file_info.copy() # Keep a copy to detect changes
        for rule in rules:
            if rule.get("enabled", True):
                file_info = apply_rule(file_info, rule)
        processed_files.append(file_info)
    return processed_files

if __name__ == "__main__":
    # Dummy file data for testing
    dummy_files = [
        {"name": "document.pdf", "path": "./test_files/downloads/document.pdf", "extension": ".pdf", "size": 100},
        {"name": "image.jpg", "path": "./test_files/images/image.jpg", "extension": ".jpg", "size": 200},
        {"name": "report.docx", "path": "./test_files/work/report.docx", "extension": ".docx", "size": 150},
        {"name": "temp_file.txt", "path": "./test_files/temp_file.txt", "extension": ".txt", "size": 50}
    ]

    # Create dummy files and directories for testing
    for file_info in dummy_files:
        os.makedirs(os.path.dirname(file_info["path"]), exist_ok=True)
        with open(file_info["path"], "w") as f:
            f.write("dummy content")

    # Dummy rules
    rules = [
        {
            "rule_id": "rule_001",
            "name": "Move PDFs from Downloads to Documents",
            "conditions": [
                {"field": "path", "operator": "contains", "value": "downloads"},
                {"field": "extension", "operator": "equals", "value": ".pdf"}
            ],
            "actions": [
                {"type": "move", "destination": "./test_files/documents"}
            ],
            "enabled": True
        },
        {
            "rule_id": "rule_002",
            "name": "Rename Work Reports",
            "conditions": [
                {"field": "path", "operator": "contains", "value": "work"},
                {"field": "extension", "operator": "equals", "value": ".docx"}
            ],
            "actions": [
                {"type": "rename", "new_name": "processed_report.docx"}
            ],
            "enabled": True
        },
        {
            "rule_id": "rule_003",
            "name": "Tag Images",
            "conditions": [
                {"field": "extension", "operator": "equals", "value": ".jpg"}
            ],
            "actions": [
                {"type": "add_tag", "tag": "photo"}
            ],
            "enabled": True
        },
        {
            "rule_id": "rule_004",
            "name": "Delete Temp Files",
            "conditions": [
                {"field": "name", "operator": "contains", "value": "temp"},
                {"field": "extension", "operator": "equals", "value": ".txt"}
            ],
            "actions": [
                {"type": "delete"}
            ],
            "enabled": True
        }
    ]

    print("--- Applying Rules ---")
    processed_files = apply_rules_to_files(dummy_files, rules)

    print("\n--- Processed Files Status ---")
    for file_info in processed_files:
        print(f"File: {file_info['name']}\n  Path: {file_info['path']}\n  Tags: {file_info.get('tags', 'None')}\n")

    # Clean up dummy files and directories
    print("--- Cleaning up test files ---")
    for file_info in dummy_files:
        try:
            # Need to check the updated path for moved files
            if os.path.exists(file_info["path"]):
                os.remove(file_info["path"])
            elif os.path.exists(os.path.join("./test_files/documents", "document.pdf")):
                os.remove(os.path.join("./test_files/documents", "document.pdf"))
            elif os.path.exists(os.path.join("./test_files/work", "processed_report.docx")):
                os.remove(os.path.join("./test_files/work", "processed_report.docx"))
        except OSError as e:
            print(f"Error during cleanup: {e}")
    try:
        shutil.rmtree("./test_files")
    except OSError as e:
        print(f"Error removing test_files directory: {e}")


