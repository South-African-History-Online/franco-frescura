#!/usr/bin/env python3
"""
Comprehensive link analysis for Hugo markdown files.
Finds all internal links and checks if they resolve correctly.
Hugo-aware: understands Hugo's URL routing and static file handling.
"""

import os
import re
from pathlib import Path
from collections import defaultdict
import urllib.parse

HUGO_CONTENT_DIR = Path('hugo-site/content')
HUGO_STATIC_DIR = Path('hugo-site/static')

def extract_links(content, filepath):
    """Extract all markdown links from content"""
    links = []

    # Match markdown links: [text](url)
    md_pattern = r'\[([^\]]*)\]\(([^)]+)\)'

    for match in re.finditer(md_pattern, content):
        link_text = match.group(1)
        link_url = match.group(2)

        # Skip external links and anchors
        if link_url.startswith(('http://', 'https://', 'mailto:', '#', '//')):
            continue

        links.append({
            'text': link_text,
            'url': link_url,
            'file': filepath,
            'type': 'markdown'
        })

    # Match HTML links: <a href="url">
    html_pattern = r'<a[^>]+href=["\']([^"\']+)["\']'

    for match in re.finditer(html_pattern, content):
        link_url = match.group(1)

        # Skip external links and anchors
        if link_url.startswith(('http://', 'https://', 'mailto:', '#', '//')):
            continue

        links.append({
            'text': '',
            'url': link_url,
            'file': filepath,
            'type': 'html'
        })

    return links

def resolve_link(link_url, source_file):
    """
    Try to resolve a link to an actual file.
    Hugo-aware: understands Hugo's URL routing patterns.
    """

    # Parse URL to remove query strings and anchors
    parsed = urllib.parse.urlparse(link_url)
    clean_url = parsed.path

    if not clean_url:
        return None, False

    # Remove leading slash for path operations
    clean_path = clean_url.lstrip('/')

    # === STATIC FILES (images, graphics, etc.) ===
    # Hugo serves static/ files at root level
    if clean_url.startswith('/images/') or clean_url.startswith('/graphics/'):
        static_file = HUGO_STATIC_DIR / clean_path
        if static_file.exists():
            return str(static_file), True

    # === HTML EXTENSION LINKS (legacy) ===
    # These should be converted to Hugo-style paths, but check anyway
    if clean_url.endswith('.html') or clean_url.endswith('.htm'):
        # Strip extension and try to find markdown file
        base = clean_path.replace('.html', '').replace('.htm', '')

        # Try common locations
        checks = [
            HUGO_CONTENT_DIR / f"{base}.md",
            HUGO_CONTENT_DIR / base / '_index.md',
        ]

        # Try in subdirectories
        for subdir in ['architecture', 'urban-issues', 'graphic-work', 'postal-history',
                       'lectures', 'glossary', 'biography', 'pages']:
            checks.append(HUGO_CONTENT_DIR / subdir / f"{base}.md")

        # Try in nested subdirectories
        checks.extend([
            HUGO_CONTENT_DIR / 'architecture' / 'indigenous' / f"{base}.md",
            HUGO_CONTENT_DIR / 'architecture' / 'conservation' / f"{base}.md",
            HUGO_CONTENT_DIR / 'architecture' / 'mission-stations' / f"{base}.md",
            HUGO_CONTENT_DIR / 'architecture' / 'colonial' / f"{base}.md",
        ])

        for check_path in checks:
            if check_path.exists():
                return str(check_path.relative_to(HUGO_CONTENT_DIR)), True

        return None, False

    # === HUGO-STYLE PATHS ===
    # Hugo generates URLs from content structure
    # Hugo serves both /path and /path/ for the same content

    # Normalize: remove trailing slash for checking
    normalized_path = clean_path.rstrip('/')

    # Pattern 1: Direct file - /biography/franco-full-biography(.md)
    md_file = HUGO_CONTENT_DIR / f"{normalized_path}.md"
    if md_file.exists():
        return str(md_file.relative_to(HUGO_CONTENT_DIR)), True

    # Pattern 2: Section index - /biography/ -> /biography/_index.md
    index_file = HUGO_CONTENT_DIR / normalized_path / '_index.md'
    if index_file.exists():
        return str(index_file.relative_to(HUGO_CONTENT_DIR)), True

    # Pattern 3: Alternative index - /biography/ -> /biography/index.md
    alt_index = HUGO_CONTENT_DIR / normalized_path / 'index.md'
    if alt_index.exists():
        return str(alt_index.relative_to(HUGO_CONTENT_DIR)), True

    # Not found
    return None, False

def analyze_all_links():
    """Analyze all links in all markdown files"""

    print("=" * 70)
    print("HUGO-AWARE LINK ANALYSIS")
    print("=" * 70)
    print()
    print("✨ This analyzer understands Hugo URL routing")
    print("✅ Checks both content files and static assets")
    print()

    all_links = []
    file_count = 0

    # Scan all markdown files
    for md_file in HUGO_CONTENT_DIR.rglob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            links = extract_links(content, md_file)
            if links:
                file_count += 1
                all_links.extend(links)
        except Exception as e:
            print(f"Error reading {md_file}: {e}")

    print(f"📊 Scanned {file_count} files with links")
    print(f"📊 Found {len(all_links)} internal links")
    print()

    # Categorize links
    broken_links = []
    working_links = []
    html_extension_links = []

    print("🔍 Analyzing links with Hugo routing...")
    print()

    for link in all_links:
        target, exists = resolve_link(link['url'], link['file'])

        if exists:
            working_links.append(link)
        else:
            broken_links.append(link)

        # Check for HTML extensions
        if link['url'].endswith('.html') or link['url'].endswith('.htm'):
            html_extension_links.append(link)

    # Report broken links
    print(f"{'='*70}")
    print(f"BROKEN LINKS REPORT")
    print(f"{'='*70}")
    print()

    if broken_links:
        print(f"❌ Found {len(broken_links)} broken links:\n")

        # Group by source file
        by_file = defaultdict(list)
        for link in broken_links:
            rel_path = link['file'].relative_to(HUGO_CONTENT_DIR)
            by_file[rel_path].append(link['url'])

        for filepath, urls in sorted(by_file.items()):
            print(f"📄 {filepath}")
            for url in urls:
                print(f"   ❌ {url}")
            print()
    else:
        print("✅ No broken links found!")
        print()

    # Report HTML extension links
    print(f"{'='*70}")
    print(f"HTML EXTENSION LINKS (should be converted)")
    print(f"{'='*70}")
    print()

    if html_extension_links:
        print(f"⚠️  Found {len(html_extension_links)} links with .html/.htm extensions")
        print("   These should be converted to Hugo-style paths\n")

        # Group by source file
        by_file = defaultdict(list)
        for link in html_extension_links:
            rel_path = link['file'].relative_to(HUGO_CONTENT_DIR)
            by_file[rel_path].append(link['url'])

        count = 0
        for filepath, urls in sorted(by_file.items()):
            if count < 10:  # Show first 10 files
                print(f"📄 {filepath}")
                for url in urls[:3]:  # Show first 3 URLs per file
                    print(f"   🔗 {url}")
                if len(urls) > 3:
                    print(f"   ... and {len(urls) - 3} more")
                print()
                count += 1

        if len(by_file) > 10:
            print(f"   ... and {len(by_file) - 10} more files")
        print()
    else:
        print("✅ No legacy HTML links found")
        print()

    # Summary
    print(f"{'='*70}")
    print(f"SUMMARY")
    print(f"{'='*70}")
    print()
    print(f"Total internal links: {len(all_links)}")
    print(f"✅ Working links: {len(working_links)}")
    print(f"❌ Broken links: {len(broken_links)}")
    print(f"⚠️  HTML extension links: {len(html_extension_links)}")
    print()

    if len(broken_links) == 0:
        print("🎉 All links are valid!")
    else:
        print(f"⚠️  {len(broken_links)} links need attention")
    print()

    return {
        'all_links': all_links,
        'broken': broken_links,
        'working': working_links,
        'html_extension': html_extension_links
    }

if __name__ == '__main__':
    results = analyze_all_links()
