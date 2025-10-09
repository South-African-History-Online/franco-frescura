# Quick Start Guide

Get the Franco Frescura Archive running locally in under 2 minutes.

---

## ⚡ Fastest Start (Both Sites)

Run both the legacy HTML site and modern Hugo site simultaneously:

```bash
cd /home/mno/Code/franco-frescura
docker-compose -f docker-compose.dev.yml up -d
```

**Access the sites:**
- **Legacy HTML:** http://localhost:8888
- **Modern Hugo:** http://localhost:1313

**Stop when done:**
```bash
docker-compose -f docker-compose.dev.yml down
```

---

## 🎯 Choose What to Run

### Option 1: Both Sites (Recommended)

**Use when:** Developing or comparing both versions

```bash
docker-compose -f docker-compose.dev.yml up -d
```

- Legacy site at :8888
- Hugo site at :1313
- Both with live reload

### Option 2: Hugo Site Only

**Use when:** Working on the modern site

```bash
cd /home/mno/Code/franco-frescura/hugo-site
docker run --rm -it -v $(pwd):/src -p 1313:1313 \
  klakegg/hugo:ext-alpine server --bind 0.0.0.0
```

Access: http://localhost:1313

### Option 3: Legacy Site Only

**Use when:** Viewing the original HTML version

```bash
cd /home/mno/Code/franco-frescura
docker run -d -p 8888:80 \
  -v $(pwd)/legacy-site:/usr/share/nginx/html:ro \
  --name franco-html nginx:alpine
```

Access: http://localhost:8888

**Stop:** `docker stop franco-html && docker rm franco-html`

### Option 4: No Docker (Python HTTP Server)

**Use when:** Quick preview without Docker

**Legacy site:**
```bash
cd /home/mno/Code/franco-frescura/legacy-site
python3 -m http.server 8000
```

**Hugo built site:**
```bash
cd /home/mno/Code/franco-frescura/hugo-site
hugo --minify
cd public
python3 -m http.server 8000
```

---

## 🔧 First Time Setup

### Prerequisites

**Docker (Recommended):**
```bash
# Arch Linux
sudo pacman -S docker docker-compose

# Start Docker service
sudo systemctl enable docker
sudo systemctl start docker

# Add user to docker group
sudo usermod -aG docker $USER
# Log out and back in

# Test
docker run hello-world
```

**Alternative - Hugo Locally:**
```bash
# Arch Linux
sudo pacman -S hugo

# Verify
hugo version
```

---

## 📋 Common Commands

### View Logs

```bash
# Hugo site logs
docker logs franco-hugo -f

# Legacy site logs
docker logs franco-html -f

# Both sites
docker-compose -f docker-compose.dev.yml logs -f
```

### Restart Services

```bash
# Restart Hugo (after config changes)
docker restart franco-hugo

# Restart both
docker-compose -f docker-compose.dev.yml restart
```

### Check Status

```bash
# See running containers
docker ps --filter "name=franco"

# Check ports
lsof -i :1313
lsof -i :8888
```

### Build Static Site

```bash
# Build Hugo site for deployment
cd hugo-site
docker run --rm -v $(pwd):/src \
  klakegg/hugo:ext-alpine --minify

# Output in: hugo-site/public/
```

---

## 🚀 Development Workflow

### Typical Session

1. **Start services:**
   ```bash
   docker-compose -f docker-compose.dev.yml up -d
   ```

2. **Edit content:**
   - Files: `hugo-site/content/**/*.md`
   - Browser auto-reloads at http://localhost:1313

3. **Edit theme:**
   - Files: `hugo-site/themes/frescura-academic/`
   - Changes appear immediately

4. **Stop when done:**
   ```bash
   docker-compose -f docker-compose.dev.yml down
   ```

### Quick Edits

```bash
# Edit homepage
nano hugo-site/content/_index.md

# Edit theme styles
nano hugo-site/themes/frescura-academic/static/css/style.css

# Edit configuration
nano hugo-site/hugo.toml
```

---

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Check what's using the ports
lsof -i :1313
lsof -i :8888

# Stop existing containers
docker-compose -f docker-compose.dev.yml down

# Or kill specific process
kill -9 <PID>
```

### Hugo Won't Start

```bash
# Check Hugo logs
docker logs franco-hugo

# Common issues:
# - Syntax error in hugo.toml
# - Invalid frontmatter in .md files
# - Missing theme

# Restart Hugo
docker restart franco-hugo
```

### Changes Not Appearing

```bash
# Force rebuild
docker-compose -f docker-compose.dev.yml restart

# Clear Hugo cache
rm -rf hugo-site/resources/

# Hard refresh browser
# Ctrl+Shift+R (Linux/Windows)
# Cmd+Shift+R (Mac)
```

### Images Not Loading

```bash
# Verify all images
python3 scripts/verify_images.py

# Fix broken references
python3 scripts/fix_image_refs.py
```

---

## 📚 What's Next?

After getting the site running:

1. **Read the full README:** `README.md`
2. **Hugo-specific setup:** `HUGO_SETUP.md`
3. **Migration details:** `MIGRATION_COMPLETE.md`
4. **Image assets info:** `IMAGE_ASSETS_REPORT.md`

---

## 💡 Pro Tips

### Auto-start on Boot

```bash
# Make containers start on boot
docker-compose -f docker-compose.dev.yml up -d
docker update --restart=unless-stopped franco-hugo franco-html
```

### VS Code Integration

Open the project in VS Code for syntax highlighting and preview:

```bash
code /home/mno/Code/franco-frescura
```

Install recommended extensions:
- Hugo Language and Syntax Support
- Markdown All in One
- Docker

### Keyboard Shortcuts

When Hugo dev server is running:
- **Ctrl+C** - Stop server (if running in foreground)
- **Ctrl+Shift+R** - Hard refresh browser
- **F12** - Open browser DevTools

---

## 🎯 Quick Reference

| Task | Command |
|------|---------|
| Start both sites | `docker-compose -f docker-compose.dev.yml up -d` |
| Stop both sites | `docker-compose -f docker-compose.dev.yml down` |
| View Hugo logs | `docker logs franco-hugo -f` |
| Restart Hugo | `docker restart franco-hugo` |
| Build production | `cd hugo-site && hugo --minify` |
| Check images | `python3 scripts/verify_images.py` |

---

**Need help?** Check the troubleshooting section above or see the full README.md for detailed documentation.
