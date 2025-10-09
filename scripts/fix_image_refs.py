#!/usr/bin/env python3
"""
Fix broken image references in Hugo markdown files.
Replaces patterns like ![\1](/\2image.jpg) with proper markdown.
"""

import os
import re
from pathlib import Path

# Check which images exist in which directories
hugo_static = Path('hugo-site/static')
images_dir = hugo_static / 'images'
graphics_dir = hugo_static / 'graphics'

# Build dictionaries of available images with their paths
# Key: filename, Value: relative path from static/
available_images = {}
available_graphics = {}

if images_dir.exists():
    for f in images_dir.rglob('*'):
        if f.is_file():
            # Store as: 'filename.jpg' -> 'images/path/filename.jpg'
            rel_path = f.relative_to(hugo_static)
            available_images[f.name] = str(rel_path)
            # Also store full relative path as key
            full_rel = f.relative_to(hugo_static)
            available_images[str(full_rel)] = str(rel_path)

if graphics_dir.exists():
    for f in graphics_dir.rglob('*'):
        if f.is_file():
            rel_path = f.relative_to(hugo_static)
            available_graphics[f.name] = str(rel_path)
            full_rel = f.relative_to(hugo_static)
            available_graphics[str(full_rel)] = str(rel_path)

print(f"Found {len(set(available_images.values()))} images and {len(set(available_graphics.values()))} graphics")

def fix_image_reference(match):
    """Fix a broken image reference"""
    # Extract the filename from the broken reference
    # Pattern: ![\1](/\2filename.ext)
    full_match = match.group(0)

    # Extract filename - it's everything after /\2
    # Look for pattern: ![\1](/\2FILENAME)
    filename_match = re.search(r'/\\2(.+?)\)', full_match)
    if not filename_match:
        return full_match  # Can't fix, return as-is

    filename = filename_match.group(1)

    # Determine if it's in images or graphics - check with and without 'arch/' prefix
    basename = Path(filename).name

    # Check various possible paths
    if filename in available_images:
        img_path = available_images[filename]
        return f'![{Path(basename).stem}](/{img_path})'
    elif filename in available_graphics:
        img_path = available_graphics[filename]
        return f'![{Path(basename).stem}](/{img_path})'
    elif basename in available_images:
        img_path = available_images[basename]
        return f'![{Path(basename).stem}](/{img_path})'
    elif basename in available_graphics:
        img_path = available_graphics[basename]
        return f'![{Path(basename).stem}](/{img_path})'
    elif f'images/{filename}' in available_images:
        img_path = available_images[f'images/{filename}']
        return f'![{Path(basename).stem}](/{img_path})'
    else:
        print(f"  ⚠️  Image not found: {filename}")
        return f'![{Path(basename).stem}](/images/{filename})'

def fix_file(filepath):
    """Fix image references in a markdown file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find broken references
    original_content = content

    # Pattern: ![\1](/\2filename.ext)
    pattern = r'!\[\\1\]\(/\\2[^)]+\)'

    matches = re.findall(pattern, content)
    if matches:
        print(f"\n📄 {filepath}")
        print(f"   Found {len(matches)} broken image references")

        # Fix all references
        content = re.sub(pattern, fix_image_reference, content)

        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"   ✅ Fixed")
        return len(matches)

    return 0

def main():
    """Main function"""
    content_dir = Path('hugo-site/content')

    if not content_dir.exists():
        print(f"❌ Content directory not found: {content_dir}")
        return

    print(f"🔍 Scanning {content_dir} for broken image references...\n")

    total_fixed = 0
    files_fixed = 0

    # Find all markdown files
    for md_file in content_dir.rglob('*.md'):
        fixed = fix_file(md_file)
        if fixed > 0:
            total_fixed += fixed
            files_fixed += 1

    print(f"\n{'='*60}")
    print(f"✅ Fixed {total_fixed} image references in {files_fixed} files")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
