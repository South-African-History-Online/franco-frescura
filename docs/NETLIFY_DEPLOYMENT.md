# Netlify Deployment Guide

The simplest way to deploy the Franco Frescura Archive to production.

## Quick Setup (5 minutes)

### Step 1: Push to GitHub

```bash
# Make sure your code is pushed to GitHub
git push origin main
```

### Step 2: Connect to Netlify

1. Go to [https://app.netlify.com](https://app.netlify.com)
2. Click **"Add new site"** → **"Import an existing project"**
3. Choose **"GitHub"** (authorize if needed)
4. Select your repository: `franco-frescura`
5. Netlify will auto-detect the `netlify.toml` configuration
6. Click **"Deploy site"**

**That's it!** Netlify will:
- Build your site automatically
- Deploy to a URL like `random-name-123.netlify.app`
- Give you a free SSL certificate
- Auto-deploy on every push to main

### Step 3: Configure Custom Domain (Optional)

To use `francofrescura.sahistory.org.za`:

1. In Netlify dashboard → **Site settings** → **Domain management**
2. Click **"Add custom domain"**
3. Enter: `francofrescura.sahistory.org.za`
4. Netlify will show DNS records to add

**Add these DNS records in your domain provider:**

```
Type: CNAME
Name: francofrescura
Value: <your-site-name>.netlify.app
```

Or for apex domain:
```
Type: A
Name: @
Value: 75.2.60.5  (Netlify's load balancer)
```

5. Wait for DNS propagation (5-30 minutes)
6. Netlify will automatically provision SSL

## What Gets Deployed

The `netlify.toml` file (already in the repo) configures everything:

```toml
[build]
  command = "cd hugo-site && hugo --minify"
  publish = "hugo-site/public"

[build.environment]
  HUGO_VERSION = "0.111.3"
```

## Automatic Deployments

**Production (main branch):**
- Every push to `main` → automatic deployment
- Build time: ~30 seconds
- URL: `francofrescura.sahistory.org.za` (after DNS setup)

**Preview Deployments (PRs):**
- Every pull request → automatic preview
- Test changes before merging
- Gets unique URL like `deploy-preview-123--site.netlify.app`

**Branch Deployments:**
- Any branch can have its own deploy URL
- Enable in: **Site settings** → **Build & deploy** → **Branch deploys**

## Deployment Workflow

```bash
# 1. Make changes locally
# Edit content in hugo-site/content/

# 2. Test locally
cd hugo-site
hugo server

# 3. Commit and push
git add .
git commit -m "Update content"
git push origin main

# 4. Netlify automatically:
#    - Detects the push
#    - Runs: cd hugo-site && hugo --minify
#    - Deploys to production
#    - Takes ~30 seconds total
```

## Monitoring

**View Builds:**
- Netlify dashboard → **Deploys**
- See build logs, errors, and status
- Rollback to any previous deploy with one click

**Check Site:**
- Visit your site URL
- Netlify shows deploy time in dashboard
- Build badge: `[![Netlify Status](https://api.netlify.com/api/v1/badges/YOUR-SITE-ID/deploy-status)](https://app.netlify.com/sites/YOUR-SITE-NAME/deploys)`

## Benefits of Netlify

✅ **Zero server management** - No SSH, no cPanel, no manual uploads
✅ **Automatic builds** - Push to git, site updates automatically
✅ **Free SSL** - HTTPS enabled by default
✅ **Global CDN** - Fast loading worldwide
✅ **Instant rollbacks** - One-click revert to any version
✅ **Deploy previews** - Test PRs before merging
✅ **Free tier sufficient** - 100GB bandwidth/month, 300 build minutes
✅ **No downtime deploys** - Atomic deployments

## Troubleshooting

### Build Failed

**Check the build log:**
1. Netlify dashboard → **Deploys** → Click failed deploy
2. View **Deploy log** for errors

**Common issues:**

**Hugo version mismatch:**
```toml
# Update netlify.toml if needed
HUGO_VERSION = "0.111.3"  # Must match your local version
```

**Wrong build command:**
```bash
# Test locally first
cd hugo-site
hugo --minify
# Should complete without errors
```

**Missing files:**
```bash
# Ensure all files are committed
git status
git add hugo-site/
```

### Site Not Loading

**Check deploy status:**
- Netlify dashboard should show green "Published"
- If not, check build logs

**Clear cache:**
- Hard refresh browser: `Ctrl+Shift+R` (Linux/Win) or `Cmd+Shift+R` (Mac)

**Check DNS:**
```bash
# Verify DNS is pointing to Netlify
dig francofrescura.sahistory.org.za

# Should show:
# CNAME -> *.netlify.app
# or A record -> 75.2.60.5
```

### Images Not Loading

**Check paths in content:**
- Must use absolute paths: `/images/photo.jpg`
- Not relative: `images/photo.jpg`

**Verify images are in repo:**
```bash
ls hugo-site/static/images/
```

## Advanced Configuration

### Environment Variables

Set in Netlify dashboard → **Site settings** → **Environment variables**

```bash
HUGO_ENV=production
```

### Build Hooks

Create webhook URLs to trigger builds:
- **Site settings** → **Build & deploy** → **Build hooks**
- Useful for external CMS or scheduled rebuilds

### Functions (if needed later)

Netlify Functions can add backend functionality:
```bash
# Create netlify/functions/ directory
# Add serverless functions
```

### Forms (if needed later)

Built-in form handling:
```html
<form netlify>
  <!-- Netlify automatically processes submissions -->
</form>
```

## Updating Content

**Simple workflow:**

```bash
# Edit content
nano hugo-site/content/biography/franco-frescura.md

# Commit
git add .
git commit -m "Update biography"

# Push - Netlify deploys automatically
git push origin main

# Check deploy at: https://app.netlify.com
```

**That's it!** No build commands, no manual uploads, no server access needed.

## Migration from Current Setup

If you're currently serving from cPanel:

1. **Deploy to Netlify** (follow steps above)
2. **Test the Netlify URL** (random-name.netlify.app)
3. **Update DNS** to point to Netlify
4. **Wait for DNS propagation** (30 mins)
5. **Done!** Old server can be decommissioned

## Cost

**Free tier includes:**
- 100GB bandwidth/month
- 300 build minutes/month
- Unlimited sites
- Free SSL
- Deploy previews

**For this site:**
- ~252 pages, 15MB total
- Typical traffic uses <10GB/month
- Build takes ~30 seconds
- **Completely free** for typical usage

## Support

**Netlify Docs:**
- [Netlify + Hugo guide](https://docs.netlify.com/integrations/frameworks/hugo/)
- [Deploy settings](https://docs.netlify.com/configure-builds/overview/)
- [Custom domains](https://docs.netlify.com/domains-https/custom-domains/)

**For issues:**
- Check build logs in Netlify dashboard
- [Netlify Support](https://www.netlify.com/support/)
- [Hugo Docs](https://gohugo.io/documentation/)

## Comparison: Netlify vs cPanel

| Feature | Netlify | cPanel |
|---------|---------|--------|
| Setup time | 5 minutes | 30+ minutes |
| Deployment | Git push (automatic) | Manual upload/rsync |
| SSL | Automatic & free | Manual setup |
| CDN | Included | Not included |
| Rollbacks | One click | Manual restore |
| Preview deploys | Automatic | Not available |
| Server management | None | SSH, permissions, etc |
| Cost | Free | Hosting fees |

**Recommendation:** Use Netlify for this static site. It's simpler, faster, and more reliable.

---

**Last Updated:** October 2025
**Hugo Version:** 0.111.3+
**Netlify CLI:** Optional (not required for basic deployment)
