import argparse
import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

def analyze_url(url):
    print(f"Analyzing: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        
        results = {
            "url": url,
            "timestamp": datetime.now().isoformat(),
            "metrics": {}
        }
        
        # Title analysis
        title = soup.find('title')
        results['metrics']['title'] = {
            "text": title.text if title else "Missing",
            "length": len(title.text) if title else 0,
            "status": "OK" if title and 50 <= len(title.text) <= 60 else "Warning"
        }
        
        # Meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        results['metrics']['description'] = {
            "text": meta_desc['content'] if meta_desc else "Missing",
            "length": len(meta_desc['content']) if meta_desc else 0,
            "status": "OK" if meta_desc and 150 <= len(meta_desc['content']) <= 160 else "Warning"
        }
        
        # Heading structure
        headings = {}
        for i in range(1, 7):
            h_tags = soup.find_all(f'h{i}')
            headings[f'h{i}'] = len(h_tags)
        results['metrics']['headings'] = headings
        
        # Images alt text
        images = soup.find_all('img')
        images_without_alt = [img.get('src') for img in images if not img.get('alt')]
        results['metrics']['images'] = {
            "total": len(images),
            "missing_alt": len(images_without_alt),
            "missing_alt_sources": images_without_alt
        }
        
        # Score calculation (simple)
        score = 100
        if not title: score -= 20
        if not meta_desc: score -= 20
        if headings.get('h1', 0) != 1: score -= 10
        if len(images_without_alt) > 0: score -= 5
        
        results['score'] = max(0, score)
        
        return results
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Professional SEO Analyzer")
    parser.add_argument("--url", required=True, help="URL to analyze")
    parser.add_argument("--export", action="store_true", help="Export to JSON")
    
    args = parser.parse_args()
    
    results = analyze_url(args.url)
    print(json.dumps(results, indent=2))
    
    if args.export:
        filename = f"seo_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Report exported to {filename}")
