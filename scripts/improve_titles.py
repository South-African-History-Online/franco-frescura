#!/usr/bin/env python3
"""
Improve titles in Hugo markdown files by extracting from original HTML content.
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
import yaml

LEGACY_DIR = Path('legacy-site')
HUGO_CONTENT_DIR = Path('hugo-site/content')

def clean_title(title):
    """Clean and normalize a title string"""
    if not title:
        return ""

    # Remove extra whitespace
    title = ' '.join(title.split())

    # Remove trailing/leading punctuation
    title = title.strip(' :-|')

    # Title case for better readability, but preserve all-caps acronyms
    words = title.split()
    cleaned_words = []
    for word in words:
        # Keep all-caps words (acronyms) as-is if 2-5 chars
        if word.isupper() and 2 <= len(word) <= 5:
            cleaned_words.append(word)
        # Keep words that are already mixed case
        elif any(c.islower() for c in word) and any(c.isupper() for c in word):
            cleaned_words.append(word)
        # Title case others
        else:
            cleaned_words.append(word.capitalize())

    title = ' '.join(cleaned_words)

    # Handle common patterns
    title = title.replace('Pe ', 'PE ')
    title = title.replace(' Ec', ' EC')
    title = title.replace(' Sa ', ' SA ')
    title = title.replace('Jhb', 'JHB')

    return title

def extract_title_from_html(html_file):
    """Extract the best title from an HTML file"""

    try:
        with open(html_file, 'r', encoding='iso-8859-1', errors='ignore') as f:
            html = f.read()
    except FileNotFoundError:
        return None

    soup = BeautifulSoup(html, 'html.parser')

    # Strategy 1: Look for the current page indicator in side nav (non-link item)
    side_nav = soup.find('div', id='side_nav')
    if side_nav:
        # Find li without an <a> tag (current page)
        for li in side_nav.find_all('li'):
            if not li.find('a'):
                title = li.get_text(strip=True)
                if title and len(title) > 3:
                    return clean_title(title)

    # Strategy 2: First H5 heading in content
    content = soup.find('div', id='ffcontent')
    if not content:
        content = soup.find('div', id='contents')

    if content:
        h5 = content.find('h5')
        if h5:
            title = h5.get_text(strip=True)
            # Remove common prefixes
            title = re.sub(r'^(INTRODUCTION|PRELIMINARY REPORT|APPENDIX [A-Z])\s*:?\s*', '', title, flags=re.IGNORECASE)
            if title and len(title) > 3:
                return clean_title(title)

    # Strategy 3: First H4 heading in content
    if content:
        h4 = content.find('h4')
        if h4:
            title = h4.get_text(strip=True)
            if title and len(title) > 3:
                return clean_title(title)

    # Strategy 4: First H3 heading
    if content:
        h3 = content.find('h3')
        if h3:
            title = h3.get_text(strip=True)
            if title and len(title) > 3:
                return clean_title(title)

    # Strategy 5: Clean up the <title> tag
    title_tag = soup.find('title')
    if title_tag:
        title = title_tag.text.strip()
        # Remove site name prefix
        title = title.replace('francofrescura.co.za |', '').strip()
        title = title.replace('francofrescura.co.za', '').strip()
        title = title.strip('|').strip()

        # Only use if it's not too generic
        if title and len(title) > 3 and title.lower() not in ['architecture', 'urban issues', 'graphic work', 'postal history', 'lectures', 'glossary']:
            return clean_title(title)

    return None

def update_markdown_title(md_file):
    """Update title in a markdown file's frontmatter"""

    # Derive HTML filename from markdown filename
    md_filename = md_file.stem

    # Try to find corresponding HTML file
    html_candidates = [
        LEGACY_DIR / f"{md_filename}.html",
        LEGACY_DIR / f"{md_filename}.htm",
    ]

    html_file = None
    for candidate in html_candidates:
        if candidate.exists():
            html_file = candidate
            break

    if not html_file:
        return False

    # Extract better title from HTML
    new_title = extract_title_from_html(html_file)

    if not new_title:
        return False

    # Read current markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse frontmatter
    if not content.startswith('---'):
        return False

    # Split frontmatter and content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False

    frontmatter_str = parts[1]
    body = parts[2]

    # Parse YAML
    try:
        frontmatter = yaml.safe_load(frontmatter_str)
    except:
        return False

    # Get old title
    old_title = frontmatter.get('title', '')

    # Check if title is generic or needs improvement
    generic_titles = ['architecture', 'urban issues', 'housing issues', 'development issues',
                     'graphic work', 'postal history', 'lectures', 'glossary', 'general']

    needs_update = (
        old_title.lower() in generic_titles or
        old_title.startswith('Architecture |') or
        old_title.startswith('Postal History |') or
        len(old_title) < 5
    )

    if not needs_update:
        return False

    # Update title
    frontmatter['title'] = new_title

    # Write back
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write('---\n')
        f.write(yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False))
        f.write('---')
        f.write(body)

    print(f"  ✅ {md_file.name}")
    print(f"     Old: {old_title}")
    print(f"     New: {new_title}")

    return True

def main():
    """Main function"""
    print("=" * 70)
    print("Improving Titles in Hugo Content")
    print("=" * 70)
    print()

    if not HUGO_CONTENT_DIR.exists():
        print(f"❌ Hugo content directory not found: {HUGO_CONTENT_DIR}")
        return

    if not LEGACY_DIR.exists():
        print(f"❌ Legacy directory not found: {LEGACY_DIR}")
        return

    updated = 0
    total = 0

    # Process all markdown files except _index.md
    for md_file in HUGO_CONTENT_DIR.rglob('*.md'):
        if md_file.name == '_index.md':
            continue

        total += 1
        if update_markdown_title(md_file):
            updated += 1

    print()
    print("=" * 70)
    print(f"✅ Updated {updated} of {total} files")
    print("=" * 70)

if __name__ == '__main__':
    main()
