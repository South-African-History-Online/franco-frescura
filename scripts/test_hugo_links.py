#!/usr/bin/env python3
"""
Test links by crawling the actual Hugo site.
This gives us real-world link checking.
"""

import re
import urllib.request
import urllib.parse
from pathlib import Path
from collections import defaultdict

HUGO_BASE_URL = "http://localhost:1313"
HUGO_CONTENT_DIR = Path('hugo-site/content')

def extract_links_from_content(content):
    """Extract internal links from markdown content"""
    links = []

    # Markdown links
    md_pattern = r'\[([^\]]*)\]\(([^)]+)\)'
    for match in re.finditer(md_pattern, content):
        url = match.group(2)
        if not url.startswith(('http://', 'https://', 'mailto:', '#', '//')):
            links.append(url)

    # HTML links
    html_pattern = r'<a[^>]+href=["\']([^"\']+)["\']'
    for match in re.finditer(html_pattern, content):
        url = match.group(1)
        if not url.startswith(('http://', 'https://', 'mailto:', '#', '//')):
            links.append(url)

    return links

def check_url(url):
    """Check if a URL is accessible"""
    try:
        req = urllib.request.Request(url, method='HEAD')
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.status == 200
    except:
        return False

def test_links():
    """Test all internal links in markdown files"""

    print("=" * 70)
    print("HUGO SITE LINK TESTING")
    print("=" * 70)
    print()

    all_links = []
    broken_links = []
    working_links = []

    # Collect all internal links
    for md_file in HUGO_CONTENT_DIR.rglob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            links = extract_links_from_content(content)
            for link in links:
                all_links.append({
                    'url': link,
                    'file': md_file.relative_to(HUGO_CONTENT_DIR)
                })
        except Exception as e:
            print(f"Error reading {md_file}: {e}")

    print(f"Found {len(all_links)} internal links to test")
    print()

    # Test each unique URL
    unique_urls = set(link['url'] for link in all_links)
    print(f"Testing {len(unique_urls)} unique URLs...")
    print()

    url_status = {}

    for url in sorted(unique_urls):
        # Construct full URL
        if url.startswith('/'):
            full_url = HUGO_BASE_URL + url
        else:
            # Relative URL - skip for now
            continue

        # Test URL
        is_working = check_url(full_url)
        url_status[url] = is_working

        if not is_working:
            print(f"❌ {url}")

    # Generate report
    print()
    print("=" * 70)
    print("BROKEN LINKS BY FILE")
    print("=" * 70)
    print()

    by_file = defaultdict(list)
    for link in all_links:
        if link['url'] in url_status and not url_status[link['url']]:
            by_file[link['file']].append(link['url'])

    if by_file:
        for filepath, urls in sorted(by_file.items()):
            print(f"📄 {filepath}")
            for url in sorted(set(urls)):
                print(f"   ❌ {url}")
            print()
    else:
        print("✅ No broken links found!")
        print()

    # Summary
    working_count = sum(1 for status in url_status.values() if status)
    broken_count = sum(1 for status in url_status.values() if not status)

    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print(f"Total unique URLs tested: {len(url_status)}")
    print(f"✅ Working links: {working_count}")
    print(f"❌ Broken links: {broken_count}")
    print()

if __name__ == '__main__':
    test_links()
