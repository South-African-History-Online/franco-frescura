# Franco Frescura Archive

A comprehensive digital archive dedicated to the life, work, and legacy of **Franco Frescura** (1946-2015) - architect, academic, graphic artist, and authority on South African indigenous architecture, urban development, and cultural heritage.

[![Link Check](https://img.shields.io/badge/links-100%25%20working-brightgreen)]()
[![Search](https://img.shields.io/badge/search-174%20pages-blue)]()
[![Hugo](https://img.shields.io/badge/hugo-0.111.3-ff4088)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()

## Features

### Content & Search
- Full-text search across 174 pages with intelligent scoring
- 100% internal link health with automated CI/CD validation
- 102 verified images and graphics
- GitHub Actions CI/CD with 3 validation workflows

### Modern Design (October 2025)
- **Responsive Design**: Fully responsive layout for all devices (mobile, tablet, desktop)
- **Modern Navigation**: Dropdown submenus for Architecture section (Indigenous, Colonial, Mission Stations, Conservation)
- **Mobile Menu**: Hamburger menu with smooth slide-in animation
- **Sticky Header**: Fixed navigation bar for better user experience
- **Card-Based Layout**: Modern grid system with hover effects
- **Contemporary Styling**: CSS Grid, Flexbox, smooth transitions, and modern typography
- **Original Color Palette**: Terracotta and earth tones inspired by the original site

### SEO & Performance
- **Comprehensive SEO**: Open Graph meta tags, Twitter Cards, structured data
- **Search Engine Optimization**: robots.txt, XML sitemap, canonical URLs
- **Fast Loading**: Minified CSS/HTML, optimized assets
- **Accessibility**: WCAG 2.1 AA compliant, keyboard navigation, reduced motion support
- **Performance**: Modern CSS with efficient rendering

**Current Status:** Production ready - Fully migrated to modern Hugo static site (October 2025)

## Quick Start

```bash
# Start development environment
docker-compose -f docker-compose.dev.yml up -d

# Access sites
# Modern Hugo site: http://localhost:1313
# Legacy HTML site: http://localhost:8888

# Stop services
docker-compose -f docker-compose.dev.yml down
```

## Table of Contents

- [Project Overview](#project-overview)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Development Guide](#development-guide)
- [Content Management](#content-management)
- [CI/CD & Validation](#cicd--validation)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Project Overview

### About the Archive

This project preserves and presents Franco Frescura's extensive body of work:

- **Indigenous Architecture** - Documentation of traditional South African architecture (Xhosa, Tswana, Zulu, Venda, Pedi, Ndebele)
- **Urban Issues & Housing** - Research on apartheid cities and housing policy
- **Historical Conservation** - Studies of colonial towns and heritage sites
- **Graphic Work** - Political cartoons including the "John Burger Saga"
- **Postal History** - Research on South African postal services
- **Academic Lectures** - Conference papers and teaching materials
- **Glossary** - Comprehensive architectural and cultural terminology

### Project History

- **Original Site:** Legacy HTML (2000s-2010s) at sahistory.org.za/francofrescura
- **Migration:** October 2025 - Fully migrated to Hugo static site
- **Funding:** National Lotteries Commission via South African History Online

### Content Statistics

- 249 pages generated from 185 markdown files
- 102 image assets verified and accessible
- 8 major content sections
- 100% internal link health
- Build time: ~127ms

## Technology Stack

**Frontend:**
- Hugo 0.111.3+ (Static Site Generator)
- Custom "Frescura Academic" theme
- Responsive HTML5/CSS3
- Client-side search with JSON index

**Development:**
- Docker-based workflow
- Live reload development server
- Python migration scripts
- Git version control

**CI/CD:**
- GitHub Actions workflows
- Automated link validation
- Hugo build verification
- Content update audits

**Hosting:**
- Static files (deployable anywhere)
- Compatible with: cPanel, Netlify, Vercel, GitHub Pages

## Project Structure

```
franco-frescura/
├── hugo-site/                   # Modern Hugo site
│   ├── hugo.toml               # Hugo configuration
│   ├── content/                # Markdown content
│   │   ├── biography/
│   │   ├── architecture/
│   │   │   ├── indigenous/
│   │   │   ├── conservation/
│   │   │   ├── mission-stations/
│   │   │   └── colonial/
│   │   ├── urban-issues/
│   │   ├── graphic-work/
│   │   ├── lectures/
│   │   ├── postal-history/
│   │   └── glossary/
│   ├── static/                 # Static assets
│   │   ├── images/
│   │   ├── robots.txt          # SEO optimization
│   │   └── js/search.js        # Search functionality
│   ├── themes/frescura-academic/
│   │   ├── static/
│   │   │   ├── css/style.css   # Modern responsive design
│   │   │   └── js/menu.js      # Mobile menu functionality
│   ├── layouts/                # Custom layouts
│   └── public/                 # Built site (generated)
│
├── legacy-site/                # Original HTML site (preserved)
│
├── scripts/                    # Utility scripts
│   ├── analyze_links.py       # Link analysis (preliminary)
│   ├── fix_all_links.py       # Automated link fixing
│   ├── test_hugo_links.py     # HTTP link testing
│   ├── improve_titles.py      # Title extraction
│   └── verify_images.py       # Image verification
│
├── .github/workflows/          # CI/CD workflows
│   ├── link-check.yml         # Weekly + PR link checks
│   ├── hugo-build-validate.yml # Authoritative validation
│   └── content-update-audit.yml # Content change audits
│
├── docker-compose.dev.yml      # Development environment
└── README.md                  # This file
```

## Development Guide

### Prerequisites

- Docker & Docker Compose (recommended)
- Git for version control
- Optional: Hugo CLI for local development

### Local Development

**Using Docker (Recommended):**

```bash
# Clone repository
git clone <repository-url>
cd franco-frescura

# Start development servers
docker-compose -f docker-compose.dev.yml up -d

# View logs
docker-compose -f docker-compose.dev.yml logs -f

# Access at http://localhost:1313 (auto-reloads on changes)
```

**Using Local Hugo:**

```bash
# Install Hugo
sudo pacman -S hugo          # Arch Linux
snap install hugo --channel=extended  # Other Linux

# Start server
cd hugo-site
hugo server -D

# Access at http://localhost:1313
```

### Making Changes

**Editing Content:**

Content files use Markdown with YAML frontmatter:

```markdown
---
title: "Article Title"
date: 2025-01-01
categories:
  - Architecture
tags:
  - Xhosa
description: "Brief description"
type: docs
draft: false
---

# Article Title

Your content here...
```

**Creating New Content:**

```bash
# Using Docker
docker run --rm -v $(pwd)/hugo-site:/src klakegg/hugo:ext-alpine \
  new content/architecture/new-article.md

# Using local Hugo
cd hugo-site
hugo new content/architecture/new-article.md
```

**Editing Theme:**

- Templates: `hugo-site/themes/frescura-academic/layouts/`
- Styles: `hugo-site/themes/frescura-academic/static/css/style.css`
- JavaScript: `hugo-site/themes/frescura-academic/static/js/menu.js`

**Modern Color Scheme:**
```css
--primary: #D2691E;           /* Chocolate/Terracotta */
--primary-dark: #A0522D;      /* Sienna */
--primary-light: #E89765;     /* Sandy Brown */
--accent: #CD5C5C;            /* Indian Red */
--accent-light: #F4A460;      /* Sandy Brown */
--text-primary: #2C2C2C;
--text-secondary: #5A5A5A;
--bg-primary: #FFFFFF;
--bg-secondary: #FAFAF8;
--bg-accent: #FFF8F0;
```

### Building for Production

```bash
# Build static site
cd hugo-site
docker run --rm -v $(pwd):/src klakegg/hugo:ext-alpine --minify

# Output in public/ directory
```

## Content Management

### Content Locations

- Biography: `hugo-site/content/biography/`
- Architecture: `hugo-site/content/architecture/`
- Urban Issues: `hugo-site/content/urban-issues/`
- Graphic Work: `hugo-site/content/graphic-work/`
- Lectures: `hugo-site/content/lectures/`
- Postal History: `hugo-site/content/postal-history/`
- Glossary: `hugo-site/content/glossary/`

### Frontmatter Reference

**Required:**
```yaml
title: "Page Title"
date: 2025-01-01
draft: false
```

**Recommended:**
```yaml
categories: [Category Name]
tags: [tag1, tag2]
description: "SEO description"
weight: 10              # For ordering
type: docs             # Page type
```

### Search Functionality

The site includes full-text search:

- **Index:** Auto-generated at `/index.json`
- **Search Page:** `/search/`
- **Implementation:** Client-side JavaScript (no server required)
- **Scoring:** Title +10, Tags +5, Categories +5, Content +1

## CI/CD & Validation

### GitHub Actions Workflows

**1. Link Check (`link-check.yml`):**
- Runs: Weekly, on PRs, manual trigger
- Purpose: Preliminary markdown analysis
- Status: Informational (does not block)

**2. Hugo Build Validation (`hugo-build-validate.yml`):**
- Runs: On changes to `hugo-site/**`
- Purpose: Authoritative link validation
- Tests: Built HTML files for broken links
- Status: Blocks merge if links broken

**3. Content Update Audit (`content-update-audit.yml`):**
- Runs: On content file changes in PRs
- Purpose: Link audit for updated content
- Status: Informational with detailed report

### Validation Scripts

**analyze_links.py:**
- Checks markdown files directly
- Reports potential issues (may have false positives)
- Used by link-check.yml and content-update-audit.yml

**test_hugo_links.py:**
- Tests against running Hugo server
- HTTP-based validation (accurate)
- Used for local testing

**Hugo Build Validation:**
- Tests actual built HTML
- Most accurate validation method
- Authoritative for CI/CD pass/fail

### Running Validation Locally

```bash
# Preliminary markdown analysis
python3 scripts/analyze_links.py

# Accurate HTTP testing (requires Hugo running)
cd hugo-site
hugo server &
cd ..
python3 scripts/test_hugo_links.py
```

## Deployment

### Pre-Deployment Checklist

- Build completes without errors
- All images load correctly
- Internal links validated (100%)
- Mobile responsive
- SEO metadata present

### Deployment Options

**Option 1: Netlify (Recommended) ⭐**

The simplest deployment method - just push to GitHub and Netlify handles everything:

```bash
# Push to GitHub
git push origin main

# Netlify automatically:
# - Builds the site
# - Deploys to production
# - Updates in ~30 seconds
```

**Setup (5 minutes):**
1. Connect GitHub repo to [Netlify](https://app.netlify.com)
2. Netlify auto-detects `netlify.toml` configuration
3. Deploy automatically on every push

**Complete guide:** See [NETLIFY_DEPLOYMENT.md](NETLIFY_DEPLOYMENT.md) for:
- Step-by-step setup
- Custom domain configuration
- Automatic SSL
- Deploy previews for PRs

**Benefits:** Zero server management, free SSL, global CDN, instant rollbacks, automatic builds

---

**Option 2: cPanel Hosting (Manual)**

For traditional cPanel hosting with manual deployment:

```bash
# 1. Build for production
./scripts/build-production.sh

# 2. Deploy to cPanel
./scripts/deploy-cpanel.sh
```

**Complete guide:** See [CPANEL_DEPLOYMENT.md](CPANEL_DEPLOYMENT.md)

---

**Option 3: Vercel / GitHub Pages**

Similar to Netlify - connect repository for auto-deployment.

## Troubleshooting

### Hugo Won't Build

```bash
# Check logs
docker logs franco-hugo

# Common issues:
# - TOML syntax error in hugo.toml
# - Invalid frontmatter in .md files
# - Missing theme files
```

### Images Not Loading

```bash
# Verify all images
python3 scripts/verify_images.py

# Image paths must start with /
![Alt text](/images/photo.jpg)  # Correct
![Alt text](images/photo.jpg)   # Wrong
```

### Container Won't Start

```bash
# Check port conflicts
lsof -i :1313
lsof -i :8888

# Stop and restart
docker-compose -f docker-compose.dev.yml down
docker-compose -f docker-compose.dev.yml up -d

# Remove old containers
docker container prune
```

### Changes Not Appearing

```bash
# Restart Hugo container
docker restart franco-hugo

# Hard refresh browser (Ctrl+Shift+R)
```

### Link Validation Failing

If CI/CD reports broken links:

1. Check Hugo Build Validation workflow (authoritative)
2. Test locally with `test_hugo_links.py`
3. Run `python3 scripts/fix_all_links.py` to auto-fix
4. Verify changes and commit

## Contributing

### Development Workflow

1. Fork the repository
2. Create feature branch: `git checkout -b feature/name`
3. Make changes and test locally
4. Run validation: `python3 scripts/test_hugo_links.py`
5. Commit with meaningful messages (no AI attribution)
6. Push and create Pull Request

### Code Standards

- Clean commit messages describing logical changes
- Test all changes locally before pushing
- Ensure CI/CD workflows pass
- Update documentation if adding features

### For AI Agents

Key files for understanding the project:
- `README.md` - Complete project overview
- `hugo-site/hugo.toml` - Configuration
- `hugo-site/content/` - All content files
- `hugo-site/themes/frescura-academic/layouts/` - Templates

Common tasks:
- Add content: Create `.md` in appropriate `content/` subdirectory
- Edit theme: Modify `themes/frescura-academic/`
- Update config: Edit `hugo-site/hugo.toml`
- Build site: Run `hugo --minify` in `hugo-site/`

## Migration Status

### Completed (October 2025)

**Migration & Content:**
- Hugo static site generator configured
- Custom "Frescura Academic" theme created
- All 168 HTML pages converted to 185 Markdown files
- All 102 images migrated and verified
- Docker development environment
- Full-text search functionality (174 pages indexed)
- All internal links fixed and validated (100%)
- CI/CD workflows with automated validation
- Comprehensive documentation

**Modern Design & UX (October 2025):**
- Modern responsive design with CSS Grid and Flexbox
- Dropdown navigation menus with smooth animations
- Mobile-friendly hamburger menu
- Sticky header navigation
- Card-based homepage layout with hover effects
- Contemporary typography with fluid responsive sizing
- Enhanced color scheme matching original site
- Mobile menu with slide-in animation

**SEO & Performance (October 2025):**
- Comprehensive Open Graph and Twitter Card meta tags
- robots.txt and XML sitemap configuration
- Canonical URLs and structured metadata
- Performance optimizations (minified assets, preconnect hints)
- WCAG 2.1 AA accessibility features (keyboard navigation, reduced motion)
- Semantic HTML5 structure

### Future Enhancements

- Image optimization (WebP conversion, lazy loading)
- Advanced features (galleries, timelines, tooltips)
- Progressive Web App (PWA) support

## Resources

### Documentation

- **Hugo:** https://gohugo.io/documentation/
- **Markdown:** https://www.markdownguide.org/
- **Docker:** https://docs.docker.com/

### Project Files

- `README.md` - Main documentation (this file)
- `MIGRATION_COMPLETE.md` - Migration details
- `HUGO_SETUP.md` - Hugo-specific setup
- `QUICKSTART.md` - Quick commands
- `IMAGE_ASSETS_REPORT.md` - Image verification report

## Credits

**Content:** © Franco Frescura Estate - All Rights Reserved

**Website Development:** South African History Online

**Funding:** National Lotteries Commission

**Migration:** October 2025 (Hugo modernization)

**Technology:** Hugo, Docker, Python (BeautifulSoup, html2text)

## License

- **Content:** © Franco Frescura Estate - All Rights Reserved
- **Code:** MIT (theme and tooling)

## Contact

**South African History Online**
- Website: https://www.sahistory.org.za/
- Original Archive: Previously at sahistory.org.za/francofrescura

## Status

**Version:** 2.0 (Hugo Static Site)
**Last Updated:** October 2025
**Build Status:** Passing
**Link Health:** 100%
**Production:** Ready for deployment
