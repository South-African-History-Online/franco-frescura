#!/usr/bin/env python3
"""
Fix remaining HTML links that were missed by the initial fix.
Specifically targets image thumbnail links in graphic-work section.
"""

import re
from pathlib import Path

HUGO_CONTENT_DIR = Path('hugo-site/content')

# HTML to Hugo path mapping
HTML_TO_HUGO = {
    'indigenous-architecture-index.html': '/architecture/indigenous/',
    'graphic-work-complete-burger.html': '/graphic-work/graphic-work-complete-burger/',
    'graphic-work-collection.html': '/graphic-work/graphic-work-collection/',
    'graphic-work-sagap1.html': '/graphic-work/graphic-work-sagap1/',
    'graphic-work-saga-p2.html': '/graphic-work/graphic-work-saga-p2/',
    'graphic-work-money.html': '/graphic-work/graphic-work-money/',
    'graphic-work-travelogue.html': '/graphic-work/graphic-work-travelogue/',
    'graphic-work-police.html': '/graphic-work/graphic-work-police/',
    'graphic-work-saga-festival.html': '/graphic-work/graphic-work-saga-festival/',
    'graphic-work-saga-closelook.html': '/graphic-work/graphic-work-saga-closelook/',
    'graphic-work-enzymes.html': '/graphic-work/graphic-work-enzymes/',
    'graphic-work-master-beer.html': '/graphic-work/graphic-work-master-beer/',
    'graphic-work-craft-cars.html': '/graphic-work/graphic-work-craft-cars/',
    'graphic-work-crunch.html': '/graphic-work/graphic-work-crunch/',
    'graphic-work-patagornia.html': '/graphic-work/graphic-work-patagornia/',
    'graphic-work-clean-up-issue.html': '/graphic-work/graphic-work-clean-up-issue/',
    'graphic-work-mad-bomber.html': '/graphic-work/graphic-work-mad-bomber/',
    'graphic-work-plot.html': '/graphic-work/graphic-work-plot/',
    'graphic-work-broeders-grim.html': '/graphic-work/graphic-work-broeders-grim/',
    'graphic-work-boys-meat.html': '/graphic-work/graphic-work-boys-meat/',
    'graphic-work-sec-crunch.html': '/graphic-work/graphic-work-sec-crunch/',
    'historical-conservation-keiskammahoek.html': '/architecture/conservation/historical-conservation-keiskammahoek/',
}

def fix_file(filepath):
    """Fix HTML links in a file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = 0

    # Fix all HTML extension links
    for html_file, hugo_path in HTML_TO_HUGO.items():
        old_content = content
        # Match in markdown links
        content = content.replace(f']({html_file})', f']({hugo_path})')
        # Match in HTML href attributes
        content = content.replace(f'href="{html_file}"', f'href="{hugo_path}"')
        content = content.replace(f"href='{html_file}'", f"href='{hugo_path}'")
        if content != old_content:
            changes += 1

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    """Main function"""
    print("=" * 70)
    print("Fixing Remaining HTML Links")
    print("=" * 70)
    print()

    fixed_count = 0
    total_checked = 0

    # Check all markdown files
    for md_file in HUGO_CONTENT_DIR.rglob('*.md'):
        total_checked += 1
        if fix_file(md_file):
            fixed_count += 1
            rel_path = md_file.relative_to(HUGO_CONTENT_DIR)
            print(f"  ✅ Fixed: {rel_path}")

    print()
    print("=" * 70)
    print(f"Fixed {fixed_count} of {total_checked} files")
    print("=" * 70)

if __name__ == '__main__':
    main()
