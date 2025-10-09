#!/usr/bin/env python3
"""
Franco Frescura Archive - HTML to Hugo Markdown Migration Script

This script converts the legacy HTML site to Hugo-compatible Markdown files
with proper frontmatter and content organization.
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
import html2text
from datetime import datetime
import yaml

# Configuration
SOURCE_DIR = Path('.')
HUGO_CONTENT_DIR = Path('./hugo-v2/content')
HUGO_STATIC_DIR = Path('./hugo-v2/static')

# Content categorization based on filename patterns
CATEGORIES = {
    'architecture': {
        'patterns': ['architecture-', 'indiginous-'],
        'section': 'architecture',
        'category': 'Architecture'
    },
    'indigenous': {
        'patterns': ['indiginous-'],
        'section': 'architecture/indigenous',
        'category': 'Indigenous Architecture'
    },
    'historical': {
        'patterns': ['historical-conservation-'],
        'section': 'architecture/conservation',
        'category': 'Historical Conservation'
    },
    'mission': {
        'patterns': ['mission-'],
        'section': 'architecture/mission-stations',
        'category': 'Mission Stations'
    },
    'colonial': {
        'patterns': ['colonial-'],
        'section': 'architecture/colonial',
        'category': 'Colonial Settlement'
    },
    'urban': {
        'patterns': ['urban-'],
        'section': 'urban-issues',
        'category': 'Urban Issues'
    },
    'graphic': {
        'patterns': ['graphic-work-'],
        'section': 'graphic-work',
        'category': 'Graphic Work'
    },
    'postal': {
        'patterns': ['postal-history-'],
        'section': 'postal-history',
        'category': 'Postal History'
    },
    'lectures': {
        'patterns': ['lectures-'],
        'section': 'lectures',
        'category': 'Lectures'
    },
    'glossary': {
        'patterns': ['glossary-'],
        'section': 'glossary',
        'category': 'Glossary'
    },
    'franco': {
        'patterns': ['franco-'],
        'section': 'biography',
        'category': 'Biography'
    }
}

def extract_metadata(soup, filename):
    """Extract metadata from HTML file"""

    # Extract title
    title_tag = soup.find('title')
    if title_tag:
        title = title_tag.text.strip()
        # Clean up title
        title = title.replace('francofrescura.co.za |', '').strip()
        title = title.replace('francofrescura.co.za', '').strip()
        title = title.strip('|').strip()
    else:
        title = filename.replace('-', ' ').replace('.html', '').title()

    # Extract meta description
    meta_desc = soup.find('meta', {'name': 'description'})
    description = ''
    if meta_desc and meta_desc.get('content'):
        description = meta_desc.get('content', '').strip()

    # Extract keywords
    meta_keywords = soup.find('meta', {'name': 'keywords'})
    keywords = []
    if meta_keywords and meta_keywords.get('content'):
        keywords = [k.strip() for k in meta_keywords.get('content', '').split(',') if k.strip()]
        keywords = keywords[:10]  # Limit to 10 tags

    return {
        'title': title,
        'description': description,
        'tags': keywords
    }

def categorize_file(filename):
    """Determine section and category based on filename"""

    for cat_name, cat_info in CATEGORIES.items():
        for pattern in cat_info['patterns']:
            if filename.startswith(pattern):
                return cat_info['section'], cat_info['category']

    # Default category
    return 'pages', 'General'

def extract_content(soup):
    """Extract main content from HTML, trying multiple selectors"""

    # Try different content containers in order of preference
    content = None
    selectors = [
        ('div', {'id': 'contents'}),
        ('div', {'id': 'ffcontent'}),
        ('div', {'id': 'left_menu'}),
        ('body', {})
    ]

    for tag, attrs in selectors:
        content = soup.find(tag, attrs)
        if content:
            break

    if not content:
        return ""

    # Remove navigation and menu elements
    for unwanted in content.find_all(['nav', 'div'], class_=['menu', 'location_bar', 'side_nav']):
        unwanted.decompose()

    # Remove location bar div
    for div in content.find_all('div', id='location_bar'):
        div.decompose()

    return str(content)

def html_to_markdown(html_content):
    """Convert HTML to clean Markdown"""

    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # Don't wrap lines
    h.unicode_snob = True
    h.skip_internal_links = False

    markdown = h.handle(html_content)

    # Clean up common issues
    markdown = markdown.replace('\n\n\n\n', '\n\n')  # Remove excessive newlines
    markdown = markdown.replace('\n\n\n', '\n\n')

    # Fix image paths
    markdown = re.sub(r'!\[(.*?)\]\((images/|graphics/)', r'![\\1](/\\2', markdown)

    return markdown.strip()

def create_frontmatter(metadata, section, category):
    """Create Hugo frontmatter"""

    frontmatter = {
        'title': metadata['title'],
        'date': '2025-01-01',
        'draft': False,
        'categories': [category],
    }

    if metadata['description']:
        frontmatter['description'] = metadata['description'][:300]

    if metadata['tags']:
        frontmatter['tags'] = metadata['tags']

    # Add section-specific metadata
    frontmatter['type'] = 'docs'

    return frontmatter

def convert_file(html_file):
    """Convert single HTML file to Hugo Markdown"""

    filename = html_file.name
    print(f"Converting {filename}...")

    # Skip index files for now
    if filename in ['index.html']:
        print(f"  ⊘ Skipping {filename}")
        return

    try:
        # Read HTML file
        with open(html_file, 'r', encoding='iso-8859-1', errors='ignore') as f:
            html = f.read()

        # Parse HTML
        soup = BeautifulSoup(html, 'html.parser')

        # Extract metadata
        metadata = extract_metadata(soup, filename)

        # Categorize
        section, category = categorize_file(filename)

        # Extract content
        content_html = extract_content(soup)
        if not content_html:
            print(f"  ⚠️  No content found in {filename}")
            return

        # Convert to Markdown
        markdown = html_to_markdown(content_html)

        # Create frontmatter
        frontmatter = create_frontmatter(metadata, section, category)

        # Create output directory
        output_dir = HUGO_CONTENT_DIR / section
        output_dir.mkdir(parents=True, exist_ok=True)

        # Generate output filename
        output_filename = filename.replace('.html', '.md').replace('.htm', '.md')
        # Clean up filename
        output_filename = output_filename.replace(' ', '-').lower()

        output_file = output_dir / output_filename

        # Write file
        with open(output_file, 'w', encoding='utf-8') as f:
            # Write frontmatter
            f.write('---\n')
            f.write(yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False))
            f.write('---\n\n')
            # Write content
            f.write(markdown)

        print(f"  ✅ Created {output_file}")

    except Exception as e:
        print(f"  ❌ Error converting {filename}: {e}")

def copy_images():
    """Copy images and graphics to Hugo static directory"""

    import shutil

    print("\nCopying images and graphics...")

    # Copy images directory
    src_images = SOURCE_DIR / 'images'
    dst_images = HUGO_STATIC_DIR / 'images'
    if src_images.exists():
        if dst_images.exists():
            shutil.rmtree(dst_images)
        shutil.copytree(src_images, dst_images)
        print(f"  ✅ Copied images/ to {dst_images}")

    # Copy graphics directory
    src_graphics = SOURCE_DIR / 'graphics'
    dst_graphics = HUGO_STATIC_DIR / 'graphics'
    if src_graphics.exists():
        if dst_graphics.exists():
            shutil.rmtree(dst_graphics)
        shutil.copytree(src_graphics, dst_graphics)
        print(f"  ✅ Copied graphics/ to {dst_graphics}")

def create_section_indexes():
    """Create _index.md files for each section"""

    print("\nCreating section index files...")

    sections = {
        'urban-issues': {
            'title': 'Urban Issues & Housing',
            'description': 'Research on apartheid cities, housing policy, and urban development in South Africa.',
            'weight': 30
        },
        'graphic-work': {
            'title': 'Graphic Work',
            'description': 'Political cartoons, the John Burger Saga, and satirical artwork from the anti-apartheid era.',
            'weight': 50
        },
        'postal-history': {
            'title': 'Postal History',
            'description': 'Research on the Cape colonial Post Office and South African postal services.',
            'weight': 60
        },
        'lectures': {
            'title': 'Lectures & Papers',
            'description': 'Conference papers, public lectures, and academic teaching materials.',
            'weight': 40
        },
        'glossary': {
            'title': 'Glossary',
            'description': 'Comprehensive glossary of architectural and cultural terms, including indigenous language terminology.',
            'weight': 70
        },
        'architecture/indigenous': {
            'title': 'Indigenous Architecture',
            'description': 'Traditional architecture of Xhosa, Zulu, Tswana, Venda, Pedi, and Ndebele peoples.',
            'weight': 10
        },
        'architecture/conservation': {
            'title': 'Historical Conservation',
            'description': 'Conservation studies of colonial towns and heritage sites in the Eastern Cape.',
            'weight': 30
        },
        'architecture/mission-stations': {
            'title': 'Mission Stations',
            'description': 'Comprehensive documentation of mission stations across southern Africa.',
            'weight': 20
        },
        'architecture/colonial': {
            'title': 'Colonial Settlement',
            'description': 'Settlement patterns and architectural development during the colonial period.',
            'weight': 15
        },
    }

    for section_path, info in sections.items():
        section_dir = HUGO_CONTENT_DIR / section_path
        section_dir.mkdir(parents=True, exist_ok=True)

        index_file = section_dir / '_index.md'

        # Don't overwrite if exists
        if index_file.exists():
            print(f"  ⊘ Skipping existing {index_file}")
            continue

        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(f"""---
title: "{info['title']}"
weight: {info['weight']}
bookFlatSection: false
bookToc: true
description: "{info['description']}"
---

# {info['title']}

{info['description']}
""")

        print(f"  ✅ Created {index_file}")

def main():
    """Main migration function"""

    print("=" * 70)
    print("Franco Frescura Archive - Content Migration")
    print("=" * 70)
    print()

    # Create output directories
    HUGO_CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    HUGO_STATIC_DIR.mkdir(parents=True, exist_ok=True)

    # Create section indexes
    create_section_indexes()

    # Get all HTML files
    html_files = list(SOURCE_DIR.glob('*.html')) + list(SOURCE_DIR.glob('*.htm'))
    html_files = [f for f in html_files if f.is_file()]

    print(f"\nFound {len(html_files)} HTML files to convert\n")

    # Convert each file
    for html_file in sorted(html_files):
        convert_file(html_file)

    # Copy images
    copy_images()

    print("\n" + "=" * 70)
    print("✅ Migration Complete!")
    print("=" * 70)
    print(f"\nContent migrated to: {HUGO_CONTENT_DIR}")
    print(f"Images copied to: {HUGO_STATIC_DIR}")
    print("\nNext steps:")
    print("1. Review converted content in hugo-v2/content/")
    print("2. Check Hugo site at http://localhost:1313")
    print("3. Make any necessary adjustments")
    print()

if __name__ == '__main__':
    main()
