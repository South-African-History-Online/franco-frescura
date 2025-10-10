#!/usr/bin/env python3
"""
Comprehensive link fixing for Hugo markdown files.
- Converts .html/.htm links to Hugo-style paths
- Fixes relative section links to absolute
- Ensures image links work properly
"""

import os
import re
from pathlib import Path
import urllib.parse

HUGO_CONTENT_DIR = Path('hugo-site/content')
HUGO_STATIC_DIR = Path('hugo-site/static')

# Mapping of HTML files to their Hugo paths
HTML_TO_HUGO_MAP = {}

def build_html_mapping():
    """Build a mapping from HTML filenames to Hugo paths"""
    global HTML_TO_HUGO_MAP

    for md_file in HUGO_CONTENT_DIR.rglob('*.md'):
        if md_file.name in ['_index.md', 'index.md']:
            continue

        # Get the base filename without extension
        base_name = md_file.stem

        # Get the Hugo URL path
        rel_path = md_file.relative_to(HUGO_CONTENT_DIR)
        parent_dir = rel_path.parent

        # Create Hugo-style URL
        if parent_dir == Path('.'):
            hugo_url = f"/{base_name}/"
        else:
            hugo_url = f"/{parent_dir}/{base_name}/"

        # Map HTML extensions to this path
        HTML_TO_HUGO_MAP[f"{base_name}.html"] = hugo_url
        HTML_TO_HUGO_MAP[f"{base_name}.htm"] = hugo_url

    # Add special cases for section indexes
    HTML_TO_HUGO_MAP['architecture-index.html'] = '/architecture/'
    HTML_TO_HUGO_MAP['urban-issues-index.html'] = '/urban-issues/'
    HTML_TO_HUGO_MAP['urbanisation-housing-index.html'] = '/urban-issues/'
    HTML_TO_HUGO_MAP['graphic-work-index.html'] = '/graphic-work/'
    HTML_TO_HUGO_MAP['postal-history-index.html'] = '/postal-history/'
    HTML_TO_HUGO_MAP['lectures-index.html'] = '/lectures/'
    HTML_TO_HUGO_MAP['lectures-main-index.html'] = '/lectures/'
    HTML_TO_HUGO_MAP['glossary-index.html'] = '/glossary/'
    HTML_TO_HUGO_MAP['franco-frescura-index.html'] = '/biography/'
    HTML_TO_HUGO_MAP['franco-full-biography.html'] = '/biography/franco-full-biography/'
    HTML_TO_HUGO_MAP['indigenous-architecture-index.html'] = '/architecture/indigenous/'
    HTML_TO_HUGO_MAP['indiginous-architecture-index.html'] = '/architecture/indigenous/'
    HTML_TO_HUGO_MAP['index.html'] = '/'

def convert_html_link(url):
    """Convert an HTML link to Hugo-style path"""
    # Parse URL
    parsed = urllib.parse.urlparse(url)
    path = parsed.path
    anchor = f"#{parsed.fragment}" if parsed.fragment else ""

    # Extract just the filename
    filename = Path(path).name

    if filename in HTML_TO_HUGO_MAP:
        return HTML_TO_HUGO_MAP[filename] + anchor

    # Try without extension
    base = filename.replace('.html', '').replace('.htm', '')
    if f"{base}.html" in HTML_TO_HUGO_MAP:
        return HTML_TO_HUGO_MAP[f"{base}.html"] + anchor

    # Fallback: try to construct path
    # Remove extension and create path
    if path.endswith('.html') or path.endswith('.htm'):
        clean_path = path.replace('.html', '').replace('.htm', '')
        return f"{clean_path}/" + anchor

    return url  # Return as-is if can't convert

def fix_relative_links(content, current_file):
    """Fix relative section links to absolute"""
    rel_path = current_file.relative_to(HUGO_CONTENT_DIR)
    parent_dir = rel_path.parent

    # Patterns to fix
    fixes = [
        (r'\[([^\]]+)\]\(indigenous/\)', r'[\1](/architecture/indigenous/)'),
        (r'\[([^\]]+)\]\(colonial/\)', r'[\1](/architecture/colonial/)'),
        (r'\[([^\]]+)\]\(mission-stations/\)', r'[\1](/architecture/mission-stations/)'),
        (r'\[([^\]]+)\]\(conservation/\)', r'[\1](/architecture/conservation/)'),
        (r'\[([^\]]+)\]\(full-biography/\)', r'[\1](/biography/franco-full-biography/)'),
        (r'\[([^\]]+)\]\(brief-biography/\)', r'[\1](/biography/franco-brief-biography/)'),
        (r'\[([^\]]+)\]\(curriculum-vitae/\)', r'[\1](/biography/franco-executive-cv/)'),
        (r'\[([^\]]+)\]\(publications/\)', r'[\1](/biography/franco-publication-cv/)'),
    ]

    for pattern, replacement in fixes:
        content = re.sub(pattern, replacement, content)

    return content

def fix_links_in_file(md_file):
    """Fix all links in a markdown file"""

    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e:
        print(f"❌ Error reading {md_file}: {e}")
        return False

    content = original_content
    changes = 0

    # 1. Fix HTML extension links
    def replace_html_link(match):
        nonlocal changes
        full_match = match.group(0)
        link_text = match.group(1)
        link_url = match.group(2)

        # Skip external links
        if link_url.startswith(('http://', 'https://', 'mailto:', '//', '#')):
            return full_match

        # Check if it's an HTML link
        if link_url.endswith('.html') or link_url.endswith('.htm'):
            new_url = convert_html_link(link_url)
            if new_url != link_url:
                changes += 1
                return f'[{link_text}]({new_url})'

        return full_match

    # Replace markdown links with HTML extensions
    content = re.sub(r'\[([^\]]*)\]\(([^)]+)\)', replace_html_link, content)

    # 2. Fix HTML <a> tags with HTML extensions
    def replace_html_tag(match):
        nonlocal changes
        full_match = match.group(0)
        link_url = match.group(1)

        # Skip external links
        if link_url.startswith(('http://', 'https://', 'mailto:', '//', '#')):
            return full_match

        # Check if it's an HTML link
        if link_url.endswith('.html') or link_url.endswith('.htm'):
            new_url = convert_html_link(link_url)
            if new_url != link_url:
                changes += 1
                return full_match.replace(link_url, new_url)

        return full_match

    content = re.sub(r'<a[^>]+href=["\']([^"\']+)["\']', replace_html_tag, content)

    # 3. Fix relative section links
    content = fix_relative_links(content, md_file)

    # 4. Count changes from relative link fixes
    if content != original_content:
        changes_from_relative = len(re.findall(r'\(/architecture/', content)) - len(re.findall(r'\(/architecture/', original_content))
        changes_from_relative += len(re.findall(r'\(/biography/', content)) - len(re.findall(r'\(/biography/', original_content))
        if changes_from_relative > 0:
            changes += changes_from_relative

    # Write back if changed
    if content != original_content:
        try:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)

            rel_path = md_file.relative_to(HUGO_CONTENT_DIR)
            print(f"  ✅ {rel_path} ({changes} links fixed)")
            return True
        except Exception as e:
            print(f"  ❌ Error writing {md_file}: {e}")
            return False

    return False

def main():
    """Main function"""
    print("=" * 70)
    print("COMPREHENSIVE LINK FIXING")
    print("=" * 70)
    print()

    # Build mapping
    print("📋 Building HTML to Hugo path mapping...")
    build_html_mapping()
    print(f"   Found {len(HTML_TO_HUGO_MAP)} HTML files")
    print()

    # Fix links in all files
    print("🔧 Fixing links in markdown files...")
    print()

    fixed_count = 0
    total_count = 0

    for md_file in HUGO_CONTENT_DIR.rglob('*.md'):
        total_count += 1
        if fix_links_in_file(md_file):
            fixed_count += 1

    print()
    print("=" * 70)
    print(f"✅ Fixed links in {fixed_count} of {total_count} files")
    print("=" * 70)

if __name__ == '__main__':
    main()
