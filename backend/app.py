from flask import Flask, request, jsonify, send_from_directory
import json
import os
import sys
from datetime import datetime

# Setup absolute paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(BASE_DIR, 'data')
DATA_FILE = os.path.join(DATA_DIR, 'submissions.json')

# Add BASE_DIR to sys.path to allow importing from automation
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from automation.seo.analyzer import analyze_url

app = Flask(__name__, 
            static_folder=os.path.join(BASE_DIR, 'frontend'),
            static_url_path='/frontend')

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/seo-analyzer')
def seo_analyzer():
    return send_from_directory(os.path.join(BASE_DIR, 'frontend'), 'seo.html')

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.json
        if not data:
            return jsonify({"success": False, "error": "No data provided"}), 400
        
        if not data.get('name') or not data.get('email') or not data.get('message'):
            return jsonify({"success": False, "error": "Missing required fields"}), 400
        
        submissions = []
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as f:
                    submissions = json.load(f)
            except:
                submissions = []
        
        data['timestamp'] = datetime.now().isoformat()
        submissions.append(data)
        
        with open(DATA_FILE, 'w') as f:
            json.dump(submissions, f, indent=4)
            
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        url = data.get('url')
        if not url:
            return jsonify({"success": False, "error": "URL is required"}), 400
        
        if not url.startswith('http'):
            url = 'https://' + url
            
        results = analyze_url(url)
        if "error" in results:
            return jsonify({"success": False, "error": results["error"]}), 500
            
        return jsonify({"success": True, "data": results})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/health')
def health():
    return jsonify({
        "status": "healthy",
        "time": datetime.now().isoformat()
    })

if __name__ == '__main__':
    print(f"Server starting at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
