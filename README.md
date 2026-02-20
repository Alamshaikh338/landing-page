# Professional Landing Page (Python & SEO)

Enterprise-grade portfolio website showcasing Python automation, SEO expertise, and digital marketing services.

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.8+
- pip

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/Alamshaikh338/landing-page.git
cd landing-page

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Running the Application
```bash
python backend/app.py
```
The application will be available at `http://127.0.0.1:5000`.

## 📁 Project Structure
- `index.html`: Main landing page
- `frontend/`: CSS, JS, and Assets
- `backend/`: Flask API and server logic
- `automation/`: Python SEO analyzer and other scripts
- `data/`: Local JSON storage for form submissions

## 🛠️ Features
- **Modern UI**: Dark mode, glassmorphism, and responsive design.
- **Python Backend**: Robust Flask API for handling contact forms.
- **SEO Tool**: Built-in script for analyzing website SEO performance.
- **Performance**: Optimized for < 2s load times.

## 🔍 SEO Analyzer
Run the SEO audit tool from the command line:
```bash
python automation/seo/analyzer.py --url https://outreachdeskpro.com/ --export
```

## 📄 License
MIT License. Created by [Alam Shaikh](https://github.com/Alamshaikh338).