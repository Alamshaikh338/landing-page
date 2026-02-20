from flask import Flask, request, jsonify, send_from_directory
import json
import os
from datetime import datetime

app = Flask(__name__)

# Ensure data directory exists relative to this file
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
DATA_FILE = os.path.join(DATA_DIR, 'submissions.json')

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

@app.route('/')
def index():
    return send_from_directory('..', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('..', path)

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.json
        if not data:
            return jsonify({"success": False, "error": "No data provided"}), 400
        
        # Validation
        if not data.get('name') or not data.get('email') or not data.get('message'):
            return jsonify({"success": False, "error": "Missing required fields"}), 400
        
        # Load existing submissions
        submissions = []
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                try:
                    submissions = json.load(f)
                except (json.JSONDecodeError, FileNotFoundError):
                    submissions = []
        
        # Add new submission
        data['timestamp'] = datetime.now().isoformat()
        submissions.append(data)
        
        # Save submissions
        with open(DATA_FILE, 'w') as f:
            json.dump(submissions, f, indent=4)
            
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/health')
def health():
    return jsonify({
        "status": "healthy",
        "time": datetime.now().isoformat()
    })

if __name__ == '__main__':
    # When running locally, Flask needs to be told where the static folder is if it's not the default
    app.run(debug=True, port=5000)
