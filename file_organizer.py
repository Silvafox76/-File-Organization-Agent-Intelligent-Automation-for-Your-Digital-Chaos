from flask import Blueprint, request, jsonify
import os
import sys
import json

# Add the Flask app root directory to the path to import our modules
flask_app_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, flask_app_root)

# Import our file organization modules
try:
    from file_scanner import scan_directory
    from categorizer import apply_categorization
    from duplicate_detector import find_duplicates
    from recommendation_engine import generate_recommendations
    from rule_engine import apply_rules_to_files
    print("Successfully imported file organization modules")
except ImportError as e:
    print(f"Import error: {e}")
    # If modules are not found, we'll create dummy functions
    def scan_directory(directory):
        print(f"Dummy scan_directory called with: {directory}")
        return []
    
    def apply_categorization(files, rules):
        return files
    
    def find_duplicates(files):
        return []
    
    def generate_recommendations(files, rules):
        return []
    
    def apply_rules_to_files(files, rules):
        return files

file_organizer_bp = Blueprint('file_organizer', __name__)

@file_organizer_bp.route('/scan', methods=['POST'])
def scan_files():
    """Scan a directory for files"""
    data = request.get_json()
    directory = data.get('directory', '')
    
    print(f"Scan request received for directory: {directory}")
    
    if not directory or not os.path.exists(directory):
        print(f"Invalid directory: {directory}")
        return jsonify({'error': 'Invalid directory path'}), 400
    
    try:
        files = scan_directory(directory)
        print(f"Scan completed, found {len(files)} files")
        return jsonify({'files': files, 'count': len(files)})
    except Exception as e:
        print(f"Scan error: {e}")
        return jsonify({'error': str(e)}), 500

@file_organizer_bp.route('/categorize', methods=['POST'])
def categorize_files():
    """Categorize files based on rules"""
    data = request.get_json()
    files = data.get('files', [])
    rules = data.get('rules', {})
    
    try:
        categorized_files = apply_categorization(files, rules)
        return jsonify({'files': categorized_files})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@file_organizer_bp.route('/duplicates', methods=['POST'])
def find_duplicate_files():
    """Find duplicate files"""
    data = request.get_json()
    files = data.get('files', [])
    
    try:
        duplicates = find_duplicates(files)
        return jsonify({'duplicates': duplicates})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@file_organizer_bp.route('/recommendations', methods=['POST'])
def get_recommendations():
    """Get organization recommendations"""
    data = request.get_json()
    files = data.get('files', [])
    rules = data.get('rules', {})
    
    try:
        recommendations = generate_recommendations(files, rules)
        return jsonify({'recommendations': recommendations})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@file_organizer_bp.route('/organize', methods=['POST'])
def organize_files():
    """Apply organization rules to files"""
    data = request.get_json()
    files = data.get('files', [])
    rules = data.get('rules', [])
    
    try:
        organized_files = apply_rules_to_files(files, rules)
        return jsonify({'files': organized_files})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@file_organizer_bp.route('/config', methods=['GET', 'POST'])
def handle_config():
    """Handle configuration settings"""
    config_file = os.path.join(os.path.dirname(__file__), '..', 'config.json')
    
    if request.method == 'GET':
        # Return current configuration
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    config = json.load(f)
            else:
                config = {
                    'default_rules': {
                        'work': ['work', 'report', 'project', 'business'],
                        'course': ['course', 'lecture', 'syllabus', 'assignment'],
                        'personal': ['personal', 'vacation', 'photo', 'family'],
                        'ski': ['ski', 'snowboard', 'mountain']
                    },
                    'scan_settings': {
                        'include_hidden': False,
                        'max_depth': 10
                    }
                }
            return jsonify(config)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    elif request.method == 'POST':
        # Save new configuration
        try:
            config = request.get_json()
            with open(config_file, 'w') as f:
                json.dump(config, f, indent=2)
            return jsonify({'message': 'Configuration saved successfully'})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

