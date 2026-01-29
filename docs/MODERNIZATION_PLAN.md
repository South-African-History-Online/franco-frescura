# Franco Frescura Archive - Modernization Plan

> **📌 STATUS UPDATE (October 2025):**
> **Phase 1 (Foundation) and Phase 2 (Content Migration) are COMPLETE! ✅**
> This document remains as a roadmap for future enhancements (Phases 3-6).
> See `MIGRATION_COMPLETE.md` for details on completed work.

---

## Vision: A 2025 Digital Research Archive

Transform the Franco Frescura archive into a modern, accessible, mobile-friendly digital research platform that serves academics, students, architects, historians, and the general public interested in South African architectural history and cultural heritage.

---

## Table of Contents

1. [Current Problems & Goals](#current-problems--goals)
2. [Design Philosophy](#design-philosophy)
3. [Technical Approach](#technical-approach)
4. [Phase-by-Phase Implementation](#phase-by-phase-implementation)
5. [User Experience Improvements](#user-experience-improvements)
6. [Content Strategy](#content-strategy)
7. [Success Metrics](#success-metrics)

---

## Current Problems & Goals

### Problems with Current Site

**Usability Issues:**
- ❌ Fixed 779px width (unusable on mobile phones)
- ❌ Table-based layout from 2000s era
- ❌ Poor navigation (hard to find content)
- ❌ No search functionality
- ❌ No content categorization or filtering
- ❌ Small text, poor readability
- ❌ Images not optimized for web

**Accessibility Issues:**
- ❌ Non-semantic HTML
- ❌ Poor contrast ratios
- ❌ No keyboard navigation support
- ❌ Missing alt text on images
- ❌ Not screen-reader friendly

**Research/Academic Issues:**
- ❌ No citation tools
- ❌ No content cross-referencing
- ❌ Hard to find related articles
- ❌ No glossary integration
- ❌ Can't save/bookmark research
- ❌ No PDF export for articles

### Goals for Modern Site

**For Researchers & Academics:**
- ✅ Fast, powerful search (full-text + filters)
- ✅ Citation export (BibTeX, APA, Chicago)
- ✅ Related content suggestions
- ✅ Glossary tooltips inline
- ✅ Downloadable articles (PDF)
- ✅ Proper metadata for academic indexing
- ✅ Timeline visualization of Franco's work
- ✅ Geographic mapping of architectural sites

**For General Public:**
- ✅ Mobile-first responsive design
- ✅ Clear, intuitive navigation
- ✅ Beautiful image galleries
- ✅ Easy-to-read typography
- ✅ Story-driven presentation
- ✅ Share on social media
- ✅ Print-friendly versions

**For Archivists/Administrators:**
- ✅ Easy content updates (Markdown)
- ✅ Version control (Git)
- ✅ Automated deployments
- ✅ Analytics and insights
- ✅ SEO optimization
- ✅ Fast, reliable hosting

---

## Design Philosophy

### 1. **Academic + Accessible**

Balance scholarly rigor with public accessibility:
- Clean, professional aesthetic (not flashy)
- Content-first design
- Clear typography for long-form reading
- Visual hierarchy for scanning
- Progressive disclosure (don't overwhelm)

### 2. **Mobile-First Responsive**

Design for smallest screens first:
- Touch-friendly navigation
- Readable text without zooming
- Optimized images for mobile bandwidth
- Fast loading on slow connections
- Progressive Web App (PWA) capabilities

### 3. **Content Discovery**

Make finding content intuitive:
- Powerful search with faceted filters
- Topic-based browsing
- Timeline/chronological view
- Geographic/map-based exploration
- Related content algorithms
- Tag clouds and taxonomy

### 4. **Digital Preservation**

Ensure longevity:
- Open standards (HTML5, CSS3)
- Semantic markup
- Proper metadata (Dublin Core, Schema.org)
- Version control
- Export/archive capabilities
- Future-proof architecture

---

## Technical Approach

### Recommended Stack: Hugo + Modern Theme

**Why Hugo?**
- ⚡ Blazing fast builds (< 1 second for 150 pages)
- 📝 Markdown content (easy to edit)
- 🏷️ Built-in taxonomy system
- 🔍 Search integration ready
- 📱 Mobile-responsive themes
- 🌐 Multilingual support (future: Afrikaans, Xhosa)
- 🚀 Deploys anywhere (cPanel, Netlify, Vercel)

### Alternative: Eleventy (11ty)

**Why Eleventy?**
- 🎨 More flexible templating
- 🔧 JavaScript-based (easier for web devs)
- 📦 Smaller ecosystem, simpler
- 🎯 Great for custom designs

### Architecture Overview

```
┌─────────────────────────────────────────────────┐
│                  Content (Markdown)              │
│  - Easy to edit, version control, future-proof  │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│          Static Site Generator (Hugo)            │
│  - Converts Markdown → HTML                      │
│  - Applies templates, styles                     │
│  - Optimizes images                              │
│  - Generates search index                        │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│              Static HTML/CSS/JS                  │
│  - Fast, secure, scalable                        │
│  - Works on any web server                       │
│  - No databases or backends                      │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│           Hosting (cPanel/Netlify)               │
│  - CDN for global speed                          │
│  - SSL/HTTPS                                     │
│  - 99.9% uptime                                  │
└─────────────────────────────────────────────────┘
```

---

## Phase-by-Phase Implementation

### Phase 1: Foundation (Week 1-2) 🏗️

**Goal:** Set up Hugo project with basic structure

**Tasks:**
1. Install Hugo locally
2. Choose/customize academic theme
3. Set up project structure
4. Create content templates
5. Configure Hugo settings

**Deliverables:**
- Working Hugo site skeleton
- Basic homepage
- Sample content pages
- Local development environment

**Theme Recommendations:**
- **Hugo Research Group** - Perfect for academic content
- **Hugo Book** - Documentation-style layout
- **PaperMod** - Clean, fast, minimalist
- **Custom Theme** - Built specifically for Franco Frescura

**Commands:**
```bash
# Install Hugo (Arch Linux)
sudo pacman -S hugo

# Create new site
hugo new site franco-frescura-v2
cd franco-frescura-v2

# Install theme (example: Hugo Book)
git init
git submodule add https://github.com/alex-shpak/hugo-book themes/hugo-book

# Configure
echo "theme = 'hugo-book'" >> hugo.toml

# Test
hugo server
```

---

### Phase 2: Content Migration (Week 2-4) 📝

**Goal:** Convert HTML content to Markdown

**Tasks:**
1. Write HTML-to-Markdown converter script
2. Extract content from current HTML files
3. Add frontmatter metadata (title, date, tags, categories)
4. Organize into logical folder structure
5. Clean up formatting
6. Add alt text to images
7. Optimize images (WebP format)

**Content Structure:**
```
content/
├── biography/
│   ├── _index.md                 # Biography section home
│   ├── full-biography.md
│   └── curriculum-vitae.md
│
├── architecture/
│   ├── _index.md
│   ├── indigenous/
│   │   ├── _index.md
│   │   ├── xhosa-architecture.md
│   │   ├── tswana-architecture.md
│   │   └── zulu-highveld.md
│   ├── colonial/
│   │   ├── _index.md
│   │   └── colonial-settlement.md
│   ├── conservation/
│   │   ├── _index.md
│   │   ├── uitenhage-study.md
│   │   └── keiskamahoek.md
│   └── mission-stations/
│       ├── _index.md
│       ├── a-f.md
│       └── botshabelo.md
│
├── urban-issues/
│   ├── _index.md
│   ├── apartheid-city.md
│   ├── johannesburg.md
│   └── housing-development.md
│
├── graphic-work/
│   ├── _index.md
│   ├── john-burger-saga/
│   │   ├── _index.md
│   │   └── [individual pages]
│   └── political-graphics.md
│
├── postal-history/
│   ├── _index.md
│   ├── cape-colonial-post.md
│   └── telegraphy.md
│
├── lectures/
│   ├── _index.md
│   └── [lecture pages]
│
└── glossary/
    ├── _index.md
    ├── architectural-terms.md
    ├── xhosa-terms.md
    ├── zulu-terms.md
    └── [other glossaries]
```

**Markdown Example:**
```markdown
---
title: "Xhosa Architecture and the Colonial Encounter"
date: 1989-01-01
lastmod: 2025-10-08
author: "Franco Frescura"
categories:
  - Architecture
  - Indigenous Architecture
tags:
  - Xhosa
  - Eastern Cape
  - Colonial Impact
  - Traditional Architecture
description: "An examination of Xhosa architectural traditions and their transformation during the colonial period."
weight: 10
toc: true
images:
  - /images/arch/xhosa-homestead.jpg
---

## Introduction

The Xhosa people of the Eastern Cape developed sophisticated...

{{< figure src="/images/arch/xhosa-homestead.jpg"
           alt="Traditional Xhosa homestead circa 1890"
           caption="Traditional Xhosa homestead, Eastern Cape, c.1890" >}}

## Historical Context

During the 19th century...

{{< glossary term="indlu" >}}The main dwelling structure{{< /glossary >}}

## References

1. Frescura, F. (1981). *Rural Shelter in Southern Africa*...
```

**Migration Script (Python):**
```python
#!/usr/bin/env python3
"""
Convert Franco Frescura HTML files to Hugo Markdown
"""

import os
import re
from bs4 import BeautifulSoup
import html2text
from pathlib import Path

def extract_metadata(soup):
    """Extract metadata from HTML"""
    title = soup.find('title')
    title_text = title.text if title else "Untitled"

    # Clean up title
    title_text = title_text.replace('francofrescura.co.za |', '').strip()

    # Extract keywords
    meta_keywords = soup.find('meta', {'name': 'keywords'})
    keywords = []
    if meta_keywords:
        keywords = [k.strip() for k in meta_keywords.get('content', '').split(',')]

    # Extract description
    meta_desc = soup.find('meta', {'name': 'description'})
    description = meta_desc.get('content', '') if meta_desc else ''

    return {
        'title': title_text,
        'keywords': keywords[:10],  # Limit to 10
        'description': description
    }

def extract_content(soup):
    """Extract main content from HTML"""
    # Try different content containers
    content = (soup.find('div', id='contents') or
               soup.find('div', id='ffcontent') or
               soup.find('div', id='left_menu'))

    if content:
        # Remove navigation elements
        for nav in content.find_all(['nav', 'div'], class_=['menu', 'location_bar']):
            nav.decompose()

        return str(content)

    return ""

def html_to_markdown(html_content):
    """Convert HTML to Markdown"""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # Don't wrap lines
    return h.handle(html_content)

def categorize_file(filename):
    """Determine category based on filename"""
    if filename.startswith('architecture'):
        return 'architecture', 'Architecture'
    elif filename.startswith('indiginous'):
        return 'architecture/indigenous', 'Indigenous Architecture'
    elif filename.startswith('historical'):
        return 'architecture/conservation', 'Historical Conservation'
    elif filename.startswith('mission'):
        return 'architecture/mission-stations', 'Mission Stations'
    elif filename.startswith('urban'):
        return 'urban-issues', 'Urban Issues'
    elif filename.startswith('graphic'):
        return 'graphic-work', 'Graphic Work'
    elif filename.startswith('postal'):
        return 'postal-history', 'Postal History'
    elif filename.startswith('lectures'):
        return 'lectures', 'Lectures'
    elif filename.startswith('glossary'):
        return 'glossary', 'Glossary'
    elif filename.startswith('franco'):
        return 'biography', 'Biography'
    else:
        return 'pages', 'Pages'

def convert_file(html_file, output_dir):
    """Convert single HTML file to Markdown"""
    print(f"Converting {html_file}...")

    with open(html_file, 'r', encoding='iso-8859-1') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Extract metadata
    metadata = extract_metadata(soup)

    # Extract content
    content_html = extract_content(soup)
    if not content_html:
        print(f"  ⚠️  No content found in {html_file}")
        return

    # Convert to Markdown
    markdown = html_to_markdown(content_html)

    # Determine category
    filename = Path(html_file).stem
    category_path, category_name = categorize_file(filename)

    # Create frontmatter
    frontmatter = f"""---
title: "{metadata['title']}"
date: 2025-01-01
draft: false
categories:
  - {category_name}
tags:
{chr(10).join(f'  - {tag}' for tag in metadata['keywords'][:5]) if metadata['keywords'] else '  - uncategorized'}
description: "{metadata['description'][:200]}"
---

"""

    # Combine
    full_content = frontmatter + markdown

    # Create output directory
    output_path = Path(output_dir) / category_path
    output_path.mkdir(parents=True, exist_ok=True)

    # Write file
    output_file = output_path / f"{filename}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_content)

    print(f"  ✅ Created {output_file}")

def main():
    """Main conversion function"""
    html_dir = '.'
    output_dir = './content'

    # Create output directory
    Path(output_dir).mkdir(exist_ok=True)

    # Convert all HTML files
    html_files = Path(html_dir).glob('*.html')
    for html_file in html_files:
        if html_file.name != 'index.html':  # Skip main index for now
            try:
                convert_file(str(html_file), output_dir)
            except Exception as e:
                print(f"  ❌ Error converting {html_file}: {e}")

    print("\n✅ Conversion complete!")
    print(f"📁 Content saved to: {output_dir}")

if __name__ == '__main__':
    main()
```

**Run Migration:**
```bash
# Install dependencies
pip install beautifulsoup4 html2text

# Run conversion
python3 scripts/html_to_markdown.py

# Review converted files
ls -R content/
```

---

### Phase 3: Design & Theme Customization (Week 4-6) 🎨

**Goal:** Create beautiful, accessible design

**Design Principles:**
1. **Typography**
   - Readable font size (18-20px body text)
   - Clear hierarchy (H1-H6)
   - Good line height (1.6-1.8)
   - Web fonts: Inter (sans), Merriweather (serif)

2. **Color Palette**
   ```css
   /* Primary - Earth tones for SA heritage */
   --primary: #8B4513;        /* Saddle Brown */
   --primary-dark: #5C2E0B;
   --primary-light: #CD853F;

   /* Accent - Warm terracotta */
   --accent: #E07040;

   /* Neutrals */
   --text: #1A1A1A;
   --text-light: #4A4A4A;
   --background: #FFFFFF;
   --background-alt: #F5F5F0;

   /* Borders */
   --border: #E0E0D0;
   ```

3. **Layout**
   - Max content width: 1200px
   - Side margins: 20px mobile, 40px desktop
   - Grid system: 12 columns
   - Card-based content blocks
   - Sticky header navigation

4. **Components**
   - Hero section with featured image
   - Article cards with thumbnails
   - Timeline visualization
   - Photo galleries with lightbox
   - Glossary tooltips
   - Citation boxes
   - Related content sidebar
   - Breadcrumb navigation
   - Search bar (prominent)
   - Footer with sitemap

**Custom Hugo Templates:**

`layouts/_default/baseof.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ .Title }} | Franco Frescura Archive</title>
    <meta name="description" content="{{ .Description }}">

    <!-- Open Graph / Social Media -->
    <meta property="og:title" content="{{ .Title }}">
    <meta property="og:description" content="{{ .Description }}">
    <meta property="og:image" content="{{ .Params.image | absURL }}">
    <meta property="og:type" content="article">

    <!-- Schema.org for Google -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "ScholarlyArticle",
      "headline": "{{ .Title }}",
      "author": {
        "@type": "Person",
        "name": "Franco Frescura"
      },
      "datePublished": "{{ .Date.Format "2006-01-02" }}"
    }
    </script>

    <!-- Styles -->
    {{ $style := resources.Get "scss/main.scss" | toCSS | minify | fingerprint }}
    <link rel="stylesheet" href="{{ $style.RelPermalink }}">
</head>
<body>
    {{ partial "header.html" . }}

    <main>
        {{ block "main" . }}{{ end }}
    </main>

    {{ partial "footer.html" . }}

    <!-- Search -->
    <script src="{{ "js/search.js" | relURL }}"></script>
</body>
</html>
```

`layouts/_default/single.html`:
```html
{{ define "main" }}
<article class="article">
    <header class="article-header">
        <nav class="breadcrumb">
            <a href="/">Home</a>
            {{ range .Ancestors.Reverse }}
                » <a href="{{ .RelPermalink }}">{{ .Title }}</a>
            {{ end }}
        </nav>

        <h1>{{ .Title }}</h1>

        <div class="article-meta">
            {{ if .Params.author }}
            <span class="author">{{ .Params.author }}</span>
            {{ end }}
            {{ if .Date }}
            <span class="date">{{ .Date.Format "January 2, 2006" }}</span>
            {{ end }}
            {{ if .ReadingTime }}
            <span class="reading-time">{{ .ReadingTime }} min read</span>
            {{ end }}
        </div>

        {{ if .Params.tags }}
        <div class="tags">
            {{ range .Params.tags }}
            <a href="/tags/{{ . | urlize }}" class="tag">{{ . }}</a>
            {{ end }}
        </div>
        {{ end }}
    </header>

    {{ if .Params.toc }}
    <aside class="toc">
        <h2>Table of Contents</h2>
        {{ .TableOfContents }}
    </aside>
    {{ end }}

    <div class="article-content">
        {{ .Content }}
    </div>

    <footer class="article-footer">
        <!-- Citation -->
        <div class="citation">
            <h3>Cite This Article</h3>
            <button onclick="copyCitation('apa')">APA</button>
            <button onclick="copyCitation('chicago')">Chicago</button>
            <button onclick="copyCitation('bibtex')">BibTeX</button>
            <pre id="citation-text">
Frescura, F. ({{ .Date.Format "2006" }}). {{ .Title }}.
Franco Frescura Archive. Retrieved from {{ .Permalink }}
            </pre>
        </div>

        <!-- Related Articles -->
        {{ $related := .Site.RegularPages.Related . | first 3 }}
        {{ with $related }}
        <div class="related">
            <h3>Related Articles</h3>
            <div class="related-grid">
                {{ range . }}
                <a href="{{ .RelPermalink }}" class="related-card">
                    {{ if .Params.image }}
                    <img src="{{ .Params.image }}" alt="{{ .Title }}">
                    {{ end }}
                    <h4>{{ .Title }}</h4>
                </a>
                {{ end }}
            </div>
        </div>
        {{ end }}
    </footer>
</article>
{{ end }}
```

---

### Phase 4: Enhanced Features (Week 6-8) 🚀

**Goal:** Add modern functionality

#### 4.1 Search (Algolia or Pagefind)

**Option A: Pagefind (Free, Self-hosted)**
```bash
# Install pagefind
npm install -D pagefind

# Add to Hugo build
hugo --minify
npx pagefind --site public
```

**Search Interface:**
```html
<!-- layouts/partials/search.html -->
<div class="search">
    <input type="text"
           id="search-input"
           placeholder="Search articles, topics, glossary..."
           aria-label="Search">
    <div id="search-results"></div>
</div>

<script>
    new PagefindUI({
        element: "#search-results",
        showSubResults: true,
        excerptLength: 30
    });
</script>
```

#### 4.2 Interactive Glossary

**Glossary Shortcode:**
```html
<!-- layouts/shortcodes/glossary.html -->
<span class="glossary-term"
      data-term="{{ .Get 0 }}"
      aria-describedby="glossary-{{ .Get 0 | urlize }}">
    {{ .Inner }}
    <span class="glossary-tooltip"
          id="glossary-{{ .Get 0 | urlize }}"
          role="tooltip">
        Loading definition...
    </span>
</span>
```

**Usage in content:**
```markdown
The {{< glossary "indlu" >}}main dwelling{{< /glossary >}} was typically circular.
```

#### 4.3 Image Galleries

**Hugo Image Processing:**
```html
<!-- layouts/shortcodes/gallery.html -->
<div class="gallery" role="region" aria-label="Image gallery">
    {{ range .Page.Resources.ByType "image" }}
    {{ $thumb := .Fill "300x200" }}
    {{ $large := .Fit "1200x800" }}
    <a href="{{ $large.RelPermalink }}"
       class="gallery-item"
       data-lightbox="gallery">
        <img src="{{ $thumb.RelPermalink }}"
             alt="{{ .Title }}"
             loading="lazy">
        <span class="caption">{{ .Title }}</span>
    </a>
    {{ end }}
</div>
```

#### 4.4 Timeline Visualization

**Using Timeline.js or custom CSS:**
```html
<!-- layouts/shortcodes/timeline.html -->
<div class="timeline">
    <div class="timeline-item" data-year="1946">
        <div class="timeline-marker"></div>
        <div class="timeline-content">
            <h3>1946: Born in Trieste, Italy</h3>
            <p>Franco Frescura was born...</p>
        </div>
    </div>
    <!-- More items -->
</div>
```

#### 4.5 Map Integration

**For architectural sites:**
```html
<!-- layouts/shortcodes/map.html -->
<div id="map" class="architecture-map"></div>
<script>
    // Using Leaflet.js
    const map = L.map('map').setView([-33.9249, 18.4241], 6);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

    // Add markers for sites
    L.marker([-33.9249, 18.4241])
        .bindPopup('Cape Town Colonial Buildings')
        .addTo(map);
</script>
```

---

### Phase 5: Accessibility & Performance (Week 8-10) ♿

**Goal:** WCAG 2.1 AA compliance + fast performance

#### 5.1 Accessibility Checklist

- [ ] Semantic HTML5 elements (`<article>`, `<nav>`, `<aside>`)
- [ ] Proper heading hierarchy (H1 → H2 → H3)
- [ ] Alt text on all images
- [ ] ARIA labels where needed
- [ ] Keyboard navigation works everywhere
- [ ] Focus indicators visible
- [ ] Color contrast ratio ≥ 4.5:1 for text
- [ ] Skip to content link
- [ ] Form labels and error messages
- [ ] Screen reader testing
- [ ] Captions for videos

**Accessibility Testing:**
```bash
# Install pa11y
npm install -g pa11y

# Test pages
pa11y http://localhost:1313
pa11y http://localhost:1313/architecture/

# Generate report
pa11y-ci --sitemap http://localhost:1313/sitemap.xml
```

#### 5.2 Performance Optimization

**Image Optimization:**
```toml
# hugo.toml
[imaging]
  quality = 85
  resampleFilter = "Lanczos"

  [imaging.exif]
    disableDate = false
    disableLatLong = true
```

**Asset Pipeline:**
```html
<!-- Minify and fingerprint CSS -->
{{ $style := resources.Get "scss/main.scss"
    | toCSS
    | minify
    | fingerprint }}
<link rel="stylesheet" href="{{ $style.RelPermalink }}">

<!-- Minify JavaScript -->
{{ $js := resources.Get "js/main.js"
    | minify
    | fingerprint }}
<script src="{{ $js.RelPermalink }}" defer></script>
```

**Lazy Loading:**
```html
<img src="placeholder.jpg"
     data-src="actual-image.jpg"
     loading="lazy"
     alt="Description">
```

**Performance Targets:**
- Lighthouse Score: 90+
- First Contentful Paint: < 1.5s
- Time to Interactive: < 3s
- Page Size: < 1MB
- Image optimization: WebP format

---

### Phase 6: Testing & Launch (Week 10-12) 🚢

**Goal:** Bug-free, production-ready site

#### 6.1 Testing Checklist

**Browser Testing:**
- [ ] Chrome (desktop + mobile)
- [ ] Firefox (desktop + mobile)
- [ ] Safari (desktop + iOS)
- [ ] Edge
- [ ] Samsung Internet

**Device Testing:**
- [ ] Desktop (1920x1080, 1366x768)
- [ ] Laptop (1440x900)
- [ ] Tablet (iPad, Android)
- [ ] Mobile (iPhone, Android phones)
- [ ] Small phones (< 375px width)

**Content Testing:**
- [ ] All images load correctly
- [ ] All links work (no 404s)
- [ ] Search returns relevant results
- [ ] Glossary tooltips work
- [ ] Citations format correctly
- [ ] Print stylesheets work
- [ ] PDFs export correctly

**Performance Testing:**
```bash
# Lighthouse CI
npm install -g @lhci/cli
lhci autorun --collect.url=http://localhost:1313

# WebPageTest
# Use https://www.webpagetest.org/

# Load testing
ab -n 1000 -c 10 http://localhost:1313/
```

#### 6.2 Deployment

**Build Production Site:**
```bash
# Build with Hugo
hugo --minify --gc

# Run Pagefind for search
npx pagefind --site public

# Test build locally
cd public && python3 -m http.server 8000
```

**Deploy to cPanel:**
```bash
# Method 1: FTP upload
lftp -u username ftp.yoursite.com
cd public_html
mirror -R public/ ./
quit

# Method 2: SSH + rsync
rsync -avz --delete public/ user@yoursite.com:~/public_html/

# Method 3: Git deployment
git add public/
git commit -m "Deploy site"
git push production main
```

**Deploy to Netlify (Recommended):**
```toml
# netlify.toml
[build]
  command = "hugo --minify && npx pagefind --site public"
  publish = "public"

[[redirects]]
  from = "/old-page.html"
  to = "/new-page/"
  status = 301
```

Push to GitHub → Netlify auto-deploys

#### 6.3 Post-Launch

**Monitoring:**
- Set up Google Analytics 4
- Add search tracking
- Monitor Core Web Vitals
- Set up uptime monitoring (UptimeRobot)
- Enable error tracking (Sentry)

**SEO:**
```xml
<!-- sitemap.xml is auto-generated by Hugo -->
<!-- Submit to Google Search Console -->
```

**Social Media:**
- Share launch announcement
- Create Twitter/Facebook pages
- Submit to academic directories
- Share with architecture/history communities

---

## User Experience Improvements

### Navigation Design

**Header Navigation:**
```
┌────────────────────────────────────────────────────────┐
│  [Logo] Franco Frescura Archive                   [🔍]  │
│                                                          │
│  Biography | Architecture | Urban | Lectures | Glossary│
└────────────────────────────────────────────────────────┘
```

**Mega Menu (on hover):**
```
Architecture ▼
┌─────────────────────────────────────────┐
│ Indigenous Architecture                 │
│   • Xhosa Architecture                  │
│   • Tswana Architecture                 │
│   • Zulu Architecture                   │
│                                         │
│ Colonial Settlement                     │
│ Mission Stations                        │
│ Historical Conservation                 │
└─────────────────────────────────────────┘
```

**Mobile Navigation:**
```
☰ [Hamburger Menu]
  ↓
[Full-screen overlay]
• Home
• Biography
• Architecture →
  • Indigenous
  • Colonial
  • Conservation
• Urban Issues
• [Search bar]
```

### Homepage Design

**Hero Section:**
```
┌────────────────────────────────────────────┐
│  [Large hero image: Franco in field]       │
│                                            │
│  Franco Frescura Archive                   │
│  Exploring South African Architectural     │
│  Heritage, b. 1946                         │
│                                            │
│  [Explore Archive →]                       │
└────────────────────────────────────────────┘
```

**Featured Sections:**
```
┌──────────┐ ┌──────────┐ ┌──────────┐
│[Image]   │ │[Image]   │ │[Image]   │
│Indigenous│ │Urban     │ │Graphic   │
│Arch      │ │Issues    │ │Work      │
└──────────┘ └──────────┘ └──────────┘
```

**Recent Articles:**
```
Latest Research
─────────────────────────────────────────
[Image] Xhosa Architecture and...
        5 min read • Architecture

[Image] The Apartheid City: A...
        12 min read • Urban Issues

[View All Articles →]
```

### Search Interface

**Search Results Page:**
```
┌────────────────────────────────────────────┐
│ [Search: "xhosa architecture"]        [×]  │
└────────────────────────────────────────────┘

Filters:
☐ Architecture (12)
☐ Indigenous (8)
☑ Xhosa (6)
☐ Eastern Cape (4)

Results (6):
───────────────────────────────────────────
[Thumbnail] Xhosa Architecture and Colonial...
            "...traditional Xhosa architecture
            incorporated circular dwelling..."
            Architecture • 1989

[Thumbnail] Pre-Industrial Architecture in...
            "...Xhosa settlements in the Eastern
            Cape region..."
            Architecture • 1985
```

### Article Page Layout

**Desktop:**
```
┌─────────────────────────────────────────────┐
│ Breadcrumb: Home > Architecture > Indigenous│
├─────────────────────────────────────────────┤
│                                             │
│  Xhosa Architecture and the Colonial        │
│  Encounter                                  │
│                                             │
│  Franco Frescura • 1989 • 15 min read      │
│  [Share] [Print] [Cite] [PDF]             │
├──────────────────┬──────────────────────────┤
│                  │  Table of Contents       │
│  Article Content │  • Introduction          │
│                  │  • Historical Context    │
│  [Main text]     │  • Architecture Forms    │
│                  │  • Colonial Impact       │
│  [Images]        │  • Conclusion            │
│                  │                          │
│  [More text]     │  ───────────────────     │
│                  │  Related Articles        │
│                  │  • Tswana Arch...        │
│                  │  • Colonial...           │
└──────────────────┴──────────────────────────┘
```

**Mobile:**
```
┌─────────────────────┐
│ < Back              │
├─────────────────────┤
│ Xhosa Architecture  │
│ and the Colonial    │
│ Encounter           │
│                     │
│ Franco Frescura     │
│ 1989 • 15 min read │
│ [📤] [🖨] [📄]      │
├─────────────────────┤
│ [Article content]   │
│                     │
│ [Full width]        │
│                     │
│ [Images expand]     │
│                     │
└─────────────────────┘
```

---

## Content Strategy

### Content Categorization

**Primary Categories:**
1. **Biography** - Franco's life and work
2. **Architecture** - All architectural research
   - Indigenous Architecture
   - Colonial Settlement
   - Mission Stations
   - Historical Conservation
3. **Urban Issues** - City planning, housing, apartheid
4. **Graphic Work** - Political cartoons and art
5. **Postal History** - Post office research
6. **Lectures** - Academic papers and presentations
7. **Glossary** - Terms and definitions

**Tags (Cross-cutting themes):**
- Geographic: Xhosa, Zulu, Tswana, Eastern Cape, Transvaal
- Topics: Colonialism, Apartheid, Traditional Architecture
- Types: Research Paper, Essay, Report, Lecture
- Time Periods: Pre-colonial, Colonial, Apartheid, Post-apartheid

### Metadata Standards

**Every article should have:**
```yaml
---
title: "Article Title"
date: 1989-01-01
author: "Franco Frescura"
categories: [Architecture, Indigenous]
tags: [Xhosa, Eastern Cape, Traditional]
description: "Brief summary for SEO and previews"
image: /images/featured/article-thumb.jpg
toc: true
citation: |
  Frescura, F. (1989). Article Title...
weight: 10  # For ordering within section
---
```

### Content Enhancements

**Add to Each Article:**
1. **Context Box** - When/where written, significance
2. **Key Points** - Bullet summary at top
3. **Related Terms** - Link to glossary
4. **Further Reading** - Related articles
5. **Download** - PDF version
6. **Cite** - Citation in multiple formats

**Example Context Box:**
```markdown
> **About This Article**
>
> Originally published in *South African Journal of
> Cultural History*, Vol. 3, No. 2, 1989.
>
> This groundbreaking study was the first comprehensive
> documentation of Xhosa architectural traditions and their
> transformation during colonialism.
>
> Part of Franco Frescura's doctoral research (1982-1986).
```

---

## Success Metrics

### Key Performance Indicators (KPIs)

**Traffic:**
- Monthly visitors: 5,000+ (Year 1)
- Pages per session: 3+
- Bounce rate: < 60%
- Average session: 3+ minutes

**Engagement:**
- Search usage: 30%+ of visitors
- Article completion rate: 60%+
- PDF downloads: 500+/month
- Social shares: 100+/month

**Technical:**
- Page load time: < 2 seconds
- Lighthouse score: 90+
- Mobile traffic: 50%+
- Zero critical accessibility issues

**Academic Impact:**
- Citations from other researchers
- Featured in academic databases
- Links from universities
- Used in coursework

---

## Budget Estimate

### One-Time Costs

| Item | Cost (USD) | Notes |
|------|------------|-------|
| Domain (.org) | $15/year | francofrescura.org |
| SSL Certificate | Free | Let's Encrypt |
| Theme/Design | $0-500 | Custom or premium theme |
| Initial Development | $0-2000 | DIY or hire developer |
| **Total** | **$15-2515** | |

### Ongoing Costs (Annual)

| Item | Cost (USD) | Notes |
|------|------------|-------|
| Hosting (cPanel) | $50-150 | Basic shared hosting |
| Domain renewal | $15 | |
| Backups | $0 | Git version control |
| Maintenance | $0-500 | Updates, fixes |
| **Total** | **$65-665/year** | |

### Free Hosting Options

**Netlify Free Tier:**
- 100GB bandwidth/month
- Unlimited sites
- Continuous deployment
- Free SSL
- **Cost: $0**

**Cloudflare Pages:**
- Unlimited bandwidth
- Unlimited sites
- Free SSL
- **Cost: $0**

**Recommendation:** Start with Netlify (free), migrate to cPanel if needed later.

---

## Timeline Summary

| Phase | Duration | Status |
|-------|----------|--------|
| 1. Foundation | 1-2 weeks | 🟡 Ready to start |
| 2. Content Migration | 2-4 weeks | 🟡 Scripts ready |
| 3. Design | 2-4 weeks | 🟡 Planning |
| 4. Features | 2-3 weeks | 🟡 Planning |
| 5. Accessibility | 1-2 weeks | 🟡 Planning |
| 6. Testing & Launch | 1-2 weeks | 🟡 Planning |
| **Total** | **9-15 weeks** | **~3 months** |

---

## Next Steps

### Immediate Actions (This Week)

1. **Decision: Choose Static Site Generator**
   - ✅ Hugo (recommended)
   - ⬜ Eleventy
   - ⬜ Other

2. **Set Up Development Environment**
   ```bash
   sudo pacman -S hugo
   hugo new site franco-frescura-v2
   cd franco-frescura-v2
   hugo server
   ```

3. **Pick/Customize Theme**
   - Review Hugo themes: https://themes.gohugo.io/
   - Or design custom theme

4. **Create Content Structure**
   - Plan folder hierarchy
   - Define frontmatter schema
   - Create content templates

### Week 1 Deliverables

- ✅ Hugo installed and configured
- ✅ Theme selected/installed
- ✅ Sample pages created
- ✅ Navigation structure defined
- ✅ Local dev environment working

---

## Resources

### Learning Hugo
- Official Docs: https://gohugo.io/documentation/
- Hugo Tutorial: https://gohugo.io/getting-started/quick-start/
- Video Course: https://www.youtube.com/watch?v=qtIqKaDlqXo

### Design Inspiration
- Academic Archives: https://artsandculture.google.com/
- MIT Architecture: https://architecture.mit.edu/
- SAHANZ: https://www.sahanz.net/

### Tools
- Hugo: https://gohugo.io/
- Pagefind (search): https://pagefind.app/
- Netlify (hosting): https://www.netlify.com/
- Figma (design): https://www.figma.com/

### Accessibility
- WCAG Guidelines: https://www.w3.org/WAI/WCAG21/quickref/
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- Pa11y Testing: https://pa11y.org/

---

## Questions?

Before starting, consider:

1. **Who will maintain the site long-term?**
   - Need to train someone on Hugo/Markdown

2. **Budget constraints?**
   - Free hosting or paid?

3. **Timeline flexibility?**
   - Can we take 3 months or need faster?

4. **Design preferences?**
   - Conservative academic or modern?
   - Color scheme preferences?

5. **Feature priorities?**
   - What's must-have vs. nice-to-have?

---

**Ready to modernize Franco Frescura's legacy?** 🚀

Let's start with Phase 1: Foundation. Say the word and we'll begin!
