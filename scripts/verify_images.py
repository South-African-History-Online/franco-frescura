#!/usr/bin/env python3
"""
Verify all image references in Hugo markdown files are accessible.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

def extract_image_refs(content):
    """Extract all image references from markdown content"""
    # Match both markdown images and HTML img tags
    md_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    html_pattern = r'<img[^>]+src=["\']([^"\']+)["\']'

    md_refs = re.findall(md_pattern, content)
    html_refs = re.findall(html_pattern, content)

    # Return list of image URLs
    images = [url for alt, url in md_refs]
    images.extend(html_refs)

    return images

def verify_images():
    """Main verification function"""
    content_dir = Path('hugo-site/content')
    static_dir = Path('hugo-site/static')

    if not content_dir.exists():
        print(f"❌ Content directory not found: {content_dir}")
        return

    print("🔍 Scanning Hugo content for image references...\n")

    all_images = []
    files_with_images = 0
    file_image_map = defaultdict(list)

    # Scan all markdown files
    for md_file in content_dir.rglob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        images = extract_image_refs(content)
        if images:
            files_with_images += 1
            file_image_map[md_file] = images
            all_images.extend(images)

    unique_images = set(all_images)

    print(f"📊 Statistics:")
    print(f"   Files with images: {files_with_images}")
    print(f"   Total image references: {len(all_images)}")
    print(f"   Unique images: {len(unique_images)}")
    print()

    # Verify each unique image exists
    print("🔎 Verifying image files exist...\n")

    missing = []
    found = []

    for img_url in sorted(unique_images):
        # Skip external URLs
        if img_url.startswith(('http://', 'https://', '//')):
            continue

        # Remove leading slash
        img_path = img_url.lstrip('/')

        # Check if file exists in static directory
        full_path = static_dir / img_path

        if full_path.exists():
            found.append(img_url)
        else:
            missing.append(img_url)
            print(f"   ❌ Missing: {img_url}")
            # Show which files reference this image
            for file_path, images in file_image_map.items():
                if img_url in images:
                    print(f"      Referenced in: {file_path.relative_to(content_dir)}")

    print()
    print(f"{'='*60}")
    if missing:
        print(f"⚠️  {len(missing)} missing images out of {len(unique_images)}")
        print(f"✅  {len(found)} images found")
    else:
        print(f"✅ All {len(unique_images)} images found!")
    print(f"{'='*60}")

    # Show breakdown by directory
    print("\n📁 Images by directory:")
    by_dir = defaultdict(int)
    for img in found:
        dir_name = Path(img).parent or Path('/')
        by_dir[str(dir_name)] = by_dir.get(str(dir_name), 0) + 1

    for dir_name in sorted(by_dir.keys()):
        print(f"   {dir_name}: {by_dir[dir_name]} images")

    return len(missing) == 0

if __name__ == '__main__':
    success = verify_images()
    exit(0 if success else 1)
