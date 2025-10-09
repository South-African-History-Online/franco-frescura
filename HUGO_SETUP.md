# Hugo Modernization - Setup Complete ✅

## What's Running

You now have **TWO versions** of the Franco Frescura website running side-by-side:

### 1. Original HTML Site (Legacy)
- **URL:** http://localhost:8888
- **Location:** `legacy-site/` directory (all `*.html` files)
- **Purpose:** Keep the original site accessible for reference
- **Status:** ✅ Running in Docker (nginx)

### 2. Modern Hugo Site (New)
- **URL:** http://localhost:1313
- **Location:** `hugo-site/` directory
- **Purpose:** Modern, responsive, searchable archive
- **Status:** ✅ Running in Docker (Hugo development server)

---

## Project Structure

```
franco-frescura/
├── legacy-site/              # Original HTML site
│   ├── *.html               # ~168 HTML files
│   ├── *.css                # Original stylesheets
│   ├── images/              # Original images
│   └── graphics/            # Original graphics
│
├── hugo-site/                # NEW HUGO SITE
│   ├── hugo.toml            # Hugo configuration
│   ├── content/             # Markdown content
│   │   ├── _index.md        # Homepage
│   │   ├── biography/       # Biography section
│   │   └── architecture/    # Architecture section
│   ├── themes/
│   │   └── frescura-academic/  # Custom theme
│   ├── static/              # Static assets (images, etc.)
│   ├── layouts/             # Custom templates (if needed)
│   └── archetypes/          # Content templates
│
├── docker-compose.yml        # Original HTML site only
├── docker-compose.dev.yml    # BOTH sites (HTML + Hugo)
└── HUGO_SETUP.md            # This file
```

---

## Quick Commands

### Start Both Sites
```bash
cd /home/mno/Code/franco-frescura
docker-compose -f docker-compose.dev.yml up -d
```

### Stop Both Sites
```bash
docker-compose -f docker-compose.dev.yml down
```

### View Logs
```bash
# Hugo site logs
docker logs franco-hugo -f

# HTML site logs
docker logs franco-html -f
```

### Restart Hugo (after making changes)
```bash
docker restart franco-hugo
```

### Access Sites in Browser
- **Original HTML Site:** http://localhost:8888
- **New Hugo Site:** http://localhost:1313

---

## Hugo Site Features

### ✅ What's Working Now

1. **Custom Academic Theme**
   - Clean, professional design
   - Responsive layout (works on mobile)
   - Navigation menu
   - Content sections

2. **Content Structure**
   - Homepage with overview
   - Biography section
   - Architecture section
   - (Ready for more content)

3. **Development Environment**
   - Live reload (changes appear instantly)
   - Docker-based (no local installation needed)
   - Runs alongside old site

### 🚧 Next Steps (Not Yet Implemented)

1. **Search Functionality** (Pagefind)
   - Full-text search
   - Filters by category/tag
   - Will add in next phase

2. **Content Migration**
   - Convert HTML → Markdown
   - Import all articles
   - Migrate images
   - Add metadata

3. **Enhanced Features**
   - Image galleries
   - Timeline visualization
   - Map integration
   - Citation tools

---

## Working with Hugo

### Adding New Content

**Create a new page:**
```bash
# In hugo-site directory
docker run --rm -v $(pwd):/src klakegg/hugo:ext-alpine new content/architecture/indigenous/xhosa-architecture.md
```

Or manually create a file:

`hugo-site/content/architecture/indigenous/xhosa-architecture.md`:
```markdown
---
title: "Xhosa Architecture"
date: 2025-10-08
categories:
  - Architecture
  - Indigenous
tags:
  - Xhosa
  - Eastern Cape
description: "Traditional Xhosa architectural practices"
---

## Introduction

Your content here...
```

### Viewing Changes

Hugo has **live reload** - just save your file and the browser refreshes automatically!

1. Edit any file in `hugo-site/content/`
2. Save
3. Browser at http://localhost:1313 updates instantly

### Theme Customization

The custom theme is in `hugo-site/themes/frescura-academic/`

**Templates:**
- `layouts/_default/baseof.html` - Base template
- `layouts/_default/single.html` - Individual pages
- `layouts/_default/list.html` - Section listings
- `layouts/index.html` - Homepage

**Styles:**
- `static/css/style.css` - All CSS

**Colors (CSS variables):**
```css
--primary: #8B4513;        /* Saddle Brown */
--primary-dark: #5C2E0B;
--primary-light: #CD853F;
--accent: #E07040;
```

---

## Hugo Configuration

All configuration is in `hugo-site/hugo.toml`:

```toml
baseURL = 'https://francofrescura.org/'
title = 'Franco Frescura Archive'
theme = 'frescura-academic'

# Menu items
[[menus.main]]
  name = "Biography"
  url = "/biography/"
  weight = 10
```

### Key Settings

- **baseURL:** Final production URL
- **theme:** Which theme to use
- **menus.main:** Navigation menu items
- **taxonomies:** Categories, tags, etc.
- **outputs:** HTML, RSS, etc.

---

## Building for Production

When ready to deploy the Hugo site:

```bash
cd hugo-site

# Build static site
docker run --rm -v $(pwd):/src klakegg/hugo:ext-alpine --minify

# Output goes to hugo-site/public/
# Upload public/ folder to web server
```

---

## Content Migration Plan

### Phase 1: Prepare Structure ✅ DONE
- [x] Set up Hugo project
- [x] Create custom theme
- [x] Configure menus and navigation
- [x] Create initial content sections

### Phase 2: Migrate Content (NEXT)
- [ ] Write HTML → Markdown conversion script
- [ ] Convert biography pages
- [ ] Convert architecture articles
- [ ] Convert urban issues content
- [ ] Convert lectures and papers
- [ ] Convert glossary entries

### Phase 3: Add Search
- [ ] Integrate Pagefind
- [ ] Create search interface
- [ ] Test search functionality

### Phase 4: Enhanced Features
- [ ] Image galleries
- [ ] Timeline component
- [ ] Citation tools
- [ ] PDF export

### Phase 5: Polish & Deploy
- [ ] Optimize images
- [ ] SEO metadata
- [ ] Accessibility testing
- [ ] Deploy to production

---

## Troubleshooting

### Hugo container keeps restarting
```bash
# Check logs
docker logs franco-hugo

# Common issues:
# - TOML syntax error in hugo.toml
# - Theme not found
# - Invalid template syntax
```

### Changes not appearing
```bash
# Restart Hugo container
docker restart franco-hugo

# Or restart everything
docker-compose -f docker-compose.dev.yml restart
```

### Port already in use
```bash
# Check what's using the port
lsof -i :1313
lsof -i :8888

# Stop containers
docker-compose -f docker-compose.dev.yml down
```

### Cannot access site in browser
```bash
# Make sure containers are running
docker ps | grep franco

# Check if ports are mapped correctly
# Should see: 0.0.0.0:1313->1313/tcp
```

---

## Development Workflow

### Typical Session

1. **Start services:**
   ```bash
   docker-compose -f docker-compose.dev.yml up -d
   ```

2. **Open in browser:**
   - Hugo site: http://localhost:1313
   - Original site: http://localhost:8888 (for reference)

3. **Edit content:**
   - Files in `hugo-site/content/`
   - Hugo auto-reloads browser

4. **Edit theme/styles:**
   - Files in `hugo-site/themes/frescura-academic/`
   - Hugo auto-reloads

5. **Stop when done:**
   ```bash
   docker-compose -f docker-compose.dev.yml down
   ```

### Quick Edits

**Edit homepage:**
```bash
nano hugo-site/content/_index.md
```

**Edit styles:**
```bash
nano hugo-site/themes/frescura-academic/static/css/style.css
```

**Edit navigation menu:**
```bash
nano hugo-site/hugo.toml
# Look for [[menus.main]] sections
```

---

## Next Immediate Steps

1. **Review the Hugo site** at http://localhost:1313
   - Check navigation
   - Look at homepage
   - Browse sections

2. **Decide on content migration approach:**
   - Automated script (faster, might need cleanup)
   - Manual conversion (slower, more control)
   - Hybrid (script + manual cleanup)

3. **Plan search integration:**
   - Pagefind (recommended - free, local)
   - Algolia (paid, powerful)
   - Lunr.js (basic, built-in)

4. **Customize theme colors/styles** to match preferred aesthetic

5. **Start migrating content** section by section

---

## Resources

### Hugo Documentation
- Official Docs: https://gohugo.io/documentation/
- Quick Start: https://gohugo.io/getting-started/quick-start/
- Content Management: https://gohugo.io/content-management/
- Templates: https://gohugo.io/templates/

### Theme Development
- Template Lookup Order: https://gohugo.io/templates/lookup-order/
- Shortcodes: https://gohugo.io/content-management/shortcodes/
- Menus: https://gohugo.io/content-management/menus/

### Search Integration
- Pagefind: https://pagefind.app/
- Hugo Search: https://gohugo.io/tools/search/

### Deployment
- cPanel: Upload `public/` folder
- Netlify: https://www.netlify.com/
- Vercel: https://vercel.com/
- GitHub Pages: https://pages.github.com/

---

## Status Summary

✅ **Hugo project initialized**
✅ **Custom academic theme created**
✅ **Docker development environment running**
✅ **Initial content structure in place**
✅ **Both sites running side-by-side**

🚧 **Content migration** - Ready to begin
🚧 **Search functionality** - Next major feature
🚧 **Enhanced features** - Timeline, galleries, etc.

---

**Last Updated:** October 8, 2025
**Hugo Version:** v0.111.3 (via Docker)
**Status:** Development environment ready for content migration
