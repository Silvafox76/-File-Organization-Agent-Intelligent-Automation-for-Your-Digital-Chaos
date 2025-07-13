import os
from collections import defaultdict

def find_duplicates(file_data):
    hash_map = defaultdict(list)
    for file_info in file_data:
        hash_map[file_info["hash_md5"]].append(file_info["path"])

    duplicates = {}
    for md5_hash, paths in hash_map.items():
        if len(paths) > 1:
            duplicates[md5_hash] = paths
    return duplicates

if __name__ == "__main__":
    # Example usage with dummy data
    dummy_file_data = [
        {"name": "file1.txt", "path": "/path/to/file1.txt", "hash_md5": "abc"},
        {"name": "file2.txt", "path": "/path/to/file2.txt", "hash_md5": "def"},
        {"name": "file3.txt", "path": "/path/to/file3.txt", "hash_md5": "abc"}, # Duplicate of file1.txt
        {"name": "file4.txt", "path": "/path/to/file4.txt", "hash_md5": "ghi"},
        {"name": "file5.txt", "path": "/path/to/file5.txt", "hash_md5": "def"}  # Duplicate of file2.txt
    ]

    found_duplicates = find_duplicates(dummy_file_data)

    if found_duplicates:
        print("Found duplicate files:")
        for md5_hash, paths in found_duplicates.items():
            print(f"  Hash: {md5_hash}")
            for path in paths:
                print(f"    - {path}")
    else:
        print("No duplicate files found.")

    # Test with actual files using file_scanner.py
    print("\n--- Testing with actual scanned files ---")
    # Assuming file_scanner.py is in the same directory and can be imported
    try:
        from file_scanner import scan_directory
        test_directory = "./test_files"
        # Create a duplicate file for testing
        with open(os.path.join(test_directory, "duplicate_test1.txt"), "w") as f:
            f.write("This is a test file for hashing.") # Same content as test1.txt

        scanned_files = scan_directory(test_directory)
        actual_duplicates = find_duplicates(scanned_files)

        if actual_duplicates:
            print("Found duplicate files in test_files directory:")
            for md5_hash, paths in actual_duplicates.items():
                print(f"  Hash: {md5_hash}")
                for path in paths:
                    print(f"    - {path}")
        else:
            print("No duplicate files found in test_files directory.")

    except ImportError:
        print("Could not import file_scanner.py. Please ensure it's in the same directory.")
    except Exception as e:
        print(f"An error occurred during actual file scanning and duplicate detection: {e}")


