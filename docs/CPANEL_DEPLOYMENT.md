# cPanel Production Deployment Guide

This guide provides step-by-step instructions for deploying the Franco Frescura Archive to cPanel hosting without Docker.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Initial Setup](#initial-setup)
- [Deployment Process](#deployment-process)
- [Troubleshooting](#troubleshooting)
- [Maintenance](#maintenance)

## Overview

The production deployment system consists of:

1. **Build Script** (`scripts/build-production.sh`) - Builds the Hugo site for production
2. **Deploy Script** (`scripts/deploy-cpanel.sh`) - Deploys built files to cPanel via SSH/rsync
3. **Configuration** (`deploy-config.sh`) - Server credentials and settings
4. **Generated Files**:
   - Static HTML, CSS, JS files
   - `.htaccess` for Apache configuration
   - `.deployment-info` with build metadata

## Prerequisites

### On Your Local Machine

- **Git** - For version control
- **Hugo** (optional) - For building locally (can use Docker instead)
- **Docker** (optional) - Alternative to local Hugo installation
- **SSH client** - For secure file transfer (usually pre-installed on Linux/Mac)
- **rsync** - For efficient file synchronization (usually pre-installed on Linux/Mac)

### On cPanel Server

- **SSH access enabled** - Must be enabled in cPanel
- **Document root configured** - Domain must point to correct directory
- **Apache mod_rewrite enabled** - For clean URLs (usually enabled by default)

## Initial Setup

### Step 1: Enable SSH Access in cPanel

1. Log into your cPanel account
2. Go to **Security > SSH Access**
3. Click **Manage SSH Keys**
4. Generate a new SSH key or import your existing public key
5. Authorize the key by clicking **Manage** next to it and selecting **Authorize**

### Step 2: Setup SSH Keys (One-time)

On your local machine:

```bash
# Generate SSH key (if you don't have one)
ssh-keygen -t ed25519 -C "deploy@francofrescura"

# Copy public key to server
ssh-copy-id -p 22 username@francofrescura.sahistory.org.za

# Test connection
ssh username@francofrescura.sahistory.org.za "echo 'Connected successfully'"
```

### Step 3: Configure Document Root in cPanel

1. Log into cPanel
2. Go to **Domains** (or **Addon Domains** / **Subdomains**)
3. Find `francofrescura.sahistory.org.za`
4. Note the **Document Root** path (e.g., `public_html` or `public_html/francofrescura`)
5. You'll use this path in your deployment configuration

### Step 4: Create Deployment Configuration

```bash
# In your local project directory
cd franco-frescura

# Copy example configuration
cp deploy-config.example.sh deploy-config.sh

# Edit with your server details
nano deploy-config.sh  # or use your preferred editor
```

Edit `deploy-config.sh`:

```bash
# Your cPanel username
CPANEL_USER="your-actual-username"

# Your server hostname
CPANEL_HOST="francofrescura.sahistory.org.za"

# SSH port (usually 22)
CPANEL_PORT="22"

# Document root from Step 3
CPANEL_PATH="public_html"  # or whatever path you noted

# Deployment method (rsync recommended)
DEPLOY_METHOD="rsync"

# Create backup before deployment
CREATE_BACKUP="true"

# Dry run (test mode) - set to false for actual deployment
DRY_RUN="false"
```

**IMPORTANT:** Never commit `deploy-config.sh` to git - it's automatically ignored.

## Deployment Process

### Quick Deploy (Standard)

```bash
# 1. Build the site
./scripts/build-production.sh

# 2. Deploy to cPanel
./scripts/deploy-cpanel.sh
```

### Detailed Steps

#### 1. Build for Production

```bash
./scripts/build-production.sh
```

This script will:
- Clean previous builds
- Build the Hugo site with minification
- Generate `.htaccess` for Apache
- Create deployment metadata
- Show build statistics

**Expected output:**
```
================================================
Franco Frescura Archive - Production Build
================================================

1. Cleaning previous build...
   ✓ Removed old public/ directory

2. Building with local Hugo...
   Using: hugo v0.111.3+extended

3. Verifying build...
   ✓ Build successful!
   - HTML files: 249
   - CSS files: 3
   - JS files: 2
   - Images: 102
   - Total size: 12M

4. Creating .htaccess for cPanel...
   ✓ .htaccess created

5. Creating deployment info...
   ✓ Deployment info created
```

#### 2. Test Build Locally (Optional)

```bash
cd hugo-site/public
python3 -m http.server 8000

# Visit http://localhost:8000 in your browser
```

#### 3. Deploy to cPanel

```bash
./scripts/deploy-cpanel.sh
```

The script will:
1. Load your configuration from `deploy-config.sh`
2. Test SSH connection
3. Create backup on server (if enabled)
4. Upload files via rsync or SCP
5. Set correct file permissions
6. Verify deployment

**Expected output:**
```
================================================
Franco Frescura Archive - cPanel Deployment
================================================

Deployment Configuration:
  User:     your-username
  Host:     francofrescura.sahistory.org.za
  Path:     public_html
  Port:     22
  Method:   rsync

Continue? (y/N) y

1. Testing SSH connection...
   ✓ SSH connection successful

2. Creating backup on server...
   ✓ Backup created: ~/backups/franco-frescura-20251012-101520

3. Deploying via rsync...
   sending incremental file list
   ./
   index.html
   ...
   ✓ Deployment complete

4. Setting permissions...
   ✓ Permissions set

5. Verifying deployment...
   Local files:  425
   Remote files: 425
   ✓ Deployment verified

================================================
✓ Deployment complete!
================================================

Site URL: https://francofrescura.sahistory.org.za
```

#### 4. Verify Deployment

Visit your site at: **https://francofrescura.sahistory.org.za**

Check:
- Homepage loads correctly
- Navigation works
- Images display properly
- Search functionality works
- URLs are clean (no `.html` extension)

## Troubleshooting

### Issue: Directory Listing Instead of Website

**Symptoms:** You see "Index of /" with file/folder listings instead of the website.

**Causes & Solutions:**

1. **Wrong Document Root:**
   ```bash
   # Check your cPanel Document Root setting
   # It should point to where the HTML files are, not the parent directory
   ```

   Fix in cPanel:
   - Go to **Domains** > Select your domain
   - Click **Manage** > **Document Root**
   - Ensure it points to the directory containing `index.html`

2. **Missing index.html:**
   ```bash
   # Verify on server
   ssh username@francofrescura.sahistory.org.za
   ls -la public_html/index.html
   ```

   If missing, redeploy:
   ```bash
   ./scripts/deploy-cpanel.sh
   ```

3. **Wrong DirectoryIndex:**
   Check `.htaccess` contains:
   ```apache
   DirectoryIndex index.html
   ```

### Issue: SSH Connection Failed

**Symptoms:** `SSH connection failed` during deployment

**Solutions:**

1. **Verify SSH is enabled:**
   - cPanel > Security > SSH Access
   - Should show "SSH access is enabled"

2. **Check SSH key:**
   ```bash
   # Test connection manually
   ssh -v username@francofrescura.sahistory.org.za

   # If prompted for password, key auth isn't working
   # Re-copy your key:
   ssh-copy-id username@francofrescura.sahistory.org.za
   ```

3. **Verify port:**
   ```bash
   # Some hosts use custom SSH ports
   # Try common alternatives:
   ssh -p 2222 username@francofrescura.sahistory.org.za
   ```

   Update `deploy-config.sh` if different port is needed.

### Issue: 404 Errors for Pages

**Symptoms:** Homepage works but other pages show 404 errors

**Causes & Solutions:**

1. **mod_rewrite not enabled:**
   - Contact hosting support to enable `mod_rewrite`
   - Required for clean URLs

2. **.htaccess not working:**
   ```bash
   # Verify .htaccess exists on server
   ssh username@francofrescura.sahistory.org.za
   cat public_html/.htaccess
   ```

   If missing or incorrect:
   ```bash
   # Rebuild and redeploy
   ./scripts/build-production.sh
   ./scripts/deploy-cpanel.sh
   ```

3. **AllowOverride not enabled:**
   - Contact hosting support
   - `.htaccess` requires `AllowOverride All` in Apache config

### Issue: Images Not Loading

**Symptoms:** Pages load but images show broken

**Solutions:**

1. **Check file permissions:**
   ```bash
   ssh username@francofrescura.sahistory.org.za
   find public_html -name "*.jpg" -exec ls -l {} \;
   ```

   Should show `644` permissions. Fix with:
   ```bash
   find public_html -type f -exec chmod 644 {} \;
   find public_html -type d -exec chmod 755 {} \;
   ```

2. **Verify images exist:**
   ```bash
   # Check if images were uploaded
   ssh username@francofrescura.sahistory.org.za
   ls -la public_html/images/
   ```

3. **Check image paths:**
   - Must be absolute paths starting with `/`
   - Example: `/images/photo.jpg` not `images/photo.jpg`

### Issue: Slow Deployment

**Symptoms:** rsync takes very long time

**Solutions:**

1. **Use compression:**
   Edit `deploy-config.sh`:
   ```bash
   RSYNC_EXTRA_OPTS="--compress-level=9"
   ```

2. **Skip unchanged files:**
   rsync does this by default, but ensure:
   ```bash
   # Don't delete and rebuild unnecessarily
   # Only rebuild when content changes
   ```

3. **Use SCP method for initial deploy:**
   Edit `deploy-config.sh`:
   ```bash
   DEPLOY_METHOD="scp"
   ```
   Then switch back to rsync for updates.

### Issue: "Permission Denied" Errors

**Symptoms:** Deployment fails with permission errors

**Solutions:**

1. **Check target directory ownership:**
   ```bash
   ssh username@francofrescura.sahistory.org.za
   ls -ld public_html
   ```

   Should show your username. If not:
   ```bash
   # In cPanel > File Manager
   # Right-click directory > Change Permissions
   # Or contact hosting support
   ```

2. **Verify you have write access:**
   ```bash
   ssh username@francofrescura.sahistory.org.za
   touch public_html/test.txt
   rm public_html/test.txt
   ```

## Maintenance

### Regular Deployment Workflow

```bash
# 1. Make content changes
# Edit files in hugo-site/content/

# 2. Test locally (optional)
cd hugo-site
hugo server
# Visit http://localhost:1313

# 3. Build for production
./scripts/build-production.sh

# 4. Deploy to cPanel
./scripts/deploy-cpanel.sh

# 5. Verify deployment
# Visit https://francofrescura.sahistory.org.za
```

### Restoring from Backup

If deployment creates backups (default), restore with:

```bash
# SSH to server
ssh username@francofrescura.sahistory.org.za

# List backups
ls -la ~/backups/

# Restore a backup
cd public_html
rm -rf *
cp -r ~/backups/franco-frescura-20251012-101520/* .

# Fix permissions
find . -type f -exec chmod 644 {} \;
find . -type d -exec chmod 755 {} \;
```

### Updating Hugo Version

To use a newer Hugo version:

1. **Local Hugo:**
   ```bash
   # Linux (Arch)
   sudo pacman -S hugo

   # Ubuntu/Debian
   snap install hugo --channel=extended
   ```

2. **Docker:**
   Edit `scripts/build-production.sh`:
   ```bash
   # Change this line:
   docker run --rm -v "$(pwd):/src" klakegg/hugo:0.111.3-ext-alpine --minify
   # To newer version:
   docker run --rm -v "$(pwd):/src" klakegg/hugo:0.120.0-ext-alpine --minify
   ```

### Monitoring

**Check deployment history:**
```bash
ssh username@francofrescura.sahistory.org.za
cat public_html/.deployment-info
```

**View backups:**
```bash
ssh username@francofrescura.sahistory.org.za
ls -lh ~/backups/
```

**Test site health:**
```bash
# Check HTTP status
curl -I https://francofrescura.sahistory.org.za

# Should return: HTTP/2 200
```

## Security Notes

1. **Never commit credentials:**
   - `deploy-config.sh` is in `.gitignore`
   - Never add credentials to version control

2. **Use SSH keys:**
   - More secure than passwords
   - Enable 2FA on cPanel if available

3. **Regular backups:**
   - Deployment script creates automatic backups
   - Also maintain cPanel backups (cPanel > Backup Wizard)

4. **HTTPS enforcement:**
   - Ensure SSL certificate is installed in cPanel
   - Uncomment HTTPS redirect in `.htaccess` if needed

5. **File permissions:**
   - Files: `644` (readable by all, writable by owner)
   - Directories: `755` (executable/searchable by all)
   - Never use `777`

## Advanced: Manual Deployment

If scripts don't work, manual deployment via cPanel File Manager:

1. **Build locally:**
   ```bash
   cd hugo-site
   hugo --minify
   ```

2. **Create archive:**
   ```bash
   cd public
   zip -r franco-frescura.zip .
   ```

3. **Upload via cPanel:**
   - Log into cPanel
   - Go to **File Manager**
   - Navigate to document root
   - Click **Upload**
   - Select `franco-frescura.zip`
   - Right-click > **Extract**

4. **Cleanup:**
   - Delete the zip file
   - Verify files are in correct location

## Support

**For deployment issues:**
- Check this guide's [Troubleshooting](#troubleshooting) section
- Review script output for error messages
- Verify cPanel settings match configuration

**For cPanel-specific issues:**
- Contact your hosting provider's support
- Reference: "Static site deployment" or "HTML upload"

**For content/Hugo issues:**
- See main [README.md](README.md)
- Check [HUGO_SETUP.md](HUGO_SETUP.md)

## Quick Reference

**Build site:**
```bash
./scripts/build-production.sh
```

**Deploy to cPanel:**
```bash
./scripts/deploy-cpanel.sh
```

**Test deployment (dry run):**
```bash
# Set DRY_RUN="true" in deploy-config.sh first
./scripts/deploy-cpanel.sh
```

**Manual rsync:**
```bash
rsync -avz -e "ssh -p 22" \
  hugo-site/public/ \
  username@francofrescura.sahistory.org.za:public_html/
```

**Quick SSH commands:**
```bash
# Connect to server
ssh username@francofrescura.sahistory.org.za

# List files
ls -la public_html/

# Check deployment info
cat public_html/.deployment-info

# View .htaccess
cat public_html/.htaccess

# Check permissions
find public_html -type f -ls | head -20
```

---

**Documentation Version:** 1.0
**Last Updated:** October 2025
**Compatible with:** Hugo 0.111.3+, cPanel 108+
