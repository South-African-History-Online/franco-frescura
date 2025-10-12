#!/bin/bash
# cPanel Deployment Configuration
# Copy this file to deploy-config.sh and customize for your server
# IMPORTANT: deploy-config.sh is in .gitignore - never commit with real credentials

# cPanel/Server Connection Details
# ================================
# Your cPanel username (same as SSH username)
CPANEL_USER="your-cpanel-username"

# Your cPanel server hostname or IP
CPANEL_HOST="francofrescura.sahistory.org.za"

# SSH port (usually 22, some hosts use custom ports)
CPANEL_PORT="22"

# Remote path where site files should be deployed
# For main domain: usually public_html or www
# For subdomain: usually public_html/subdomain or domains/subdomain.example.com/public_html
# Check in cPanel > Domains > your domain > Document Root
CPANEL_PATH="public_html"

# Deployment Options
# ==================
# Deployment method: "rsync" (recommended) or "scp"
DEPLOY_METHOD="rsync"

# Create backup before deployment (true/false)
CREATE_BACKUP="true"

# Dry run mode - test without making changes (true/false)
# Set to true for testing, false for actual deployment
DRY_RUN="false"

# Advanced Options (usually don't need to change)
# ===============================================
# Rsync additional options (advanced users only)
# RSYNC_EXTRA_OPTS="--compress-level=9"

# Exclude patterns (in addition to defaults)
# RSYNC_EXCLUDE="--exclude='*.log' --exclude='temp/*'"

# SSH key file (if not using default ~/.ssh/id_rsa or ~/.ssh/id_ed25519)
# SSH_KEY_FILE="$HOME/.ssh/cpanel_deploy_key"

# Example Configurations
# ======================

# Example 1: Main domain deployment
# CPANEL_USER="username"
# CPANEL_HOST="server.example.com"
# CPANEL_PATH="public_html"

# Example 2: Subdomain deployment
# CPANEL_USER="username"
# CPANEL_HOST="server.example.com"
# CPANEL_PATH="public_html/francofrescura"

# Example 3: Custom port and path
# CPANEL_USER="username"
# CPANEL_HOST="server.example.com"
# CPANEL_PORT="2222"
# CPANEL_PATH="domains/francofrescura.sahistory.org.za/public_html"
