#!/bin/bash
# cPanel deployment script for Franco Frescura Archive
# This script deploys the built Hugo site to cPanel via rsync/SSH

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}Franco Frescura Archive - cPanel Deployment${NC}"
echo -e "${BLUE}================================================${NC}"

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
PUBLIC_DIR="$PROJECT_ROOT/hugo-site/public"

# Load deployment configuration
DEPLOY_CONFIG="$PROJECT_ROOT/deploy-config.sh"

if [ ! -f "$DEPLOY_CONFIG" ]; then
    echo -e "${RED}Error: Deployment configuration not found${NC}"
    echo -e "${YELLOW}Please create deploy-config.sh from deploy-config.example.sh${NC}"
    echo -e "${YELLOW}Run: cp deploy-config.example.sh deploy-config.sh${NC}"
    echo -e "${YELLOW}Then edit deploy-config.sh with your cPanel credentials${NC}"
    exit 1
fi

# Source configuration
source "$DEPLOY_CONFIG"

# Validate configuration
if [ -z "$CPANEL_USER" ] || [ -z "$CPANEL_HOST" ] || [ -z "$CPANEL_PATH" ]; then
    echo -e "${RED}Error: Missing required configuration${NC}"
    echo -e "${YELLOW}Please configure CPANEL_USER, CPANEL_HOST, and CPANEL_PATH in deploy-config.sh${NC}"
    exit 1
fi

# Check if public directory exists
if [ ! -d "$PUBLIC_DIR" ]; then
    echo -e "${RED}Error: Build directory not found at $PUBLIC_DIR${NC}"
    echo -e "${YELLOW}Please run: ./scripts/build-production.sh${NC}"
    exit 1
fi

# Show deployment details
echo -e "\n${YELLOW}Deployment Configuration:${NC}"
echo -e "${BLUE}  User:     $CPANEL_USER${NC}"
echo -e "${BLUE}  Host:     $CPANEL_HOST${NC}"
echo -e "${BLUE}  Path:     $CPANEL_PATH${NC}"
echo -e "${BLUE}  Port:     ${CPANEL_PORT:-22}${NC}"
echo -e "${BLUE}  Method:   ${DEPLOY_METHOD:-rsync}${NC}"

# Confirmation prompt
echo -e "\n${YELLOW}This will deploy the site to:${NC}"
echo -e "${BLUE}$CPANEL_USER@$CPANEL_HOST:$CPANEL_PATH${NC}"
echo -e "\n${YELLOW}Continue? (y/N)${NC}"
read -r CONFIRM

if [[ ! "$CONFIRM" =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}Deployment cancelled${NC}"
    exit 0
fi

# Test SSH connection
echo -e "\n${YELLOW}1. Testing SSH connection...${NC}"
if ssh -p "${CPANEL_PORT:-22}" -o ConnectTimeout=10 -o BatchMode=yes "$CPANEL_USER@$CPANEL_HOST" "echo 'Connection successful'" 2>/dev/null; then
    echo -e "${GREEN}   ✓ SSH connection successful${NC}"
else
    echo -e "${RED}   ✗ SSH connection failed${NC}"
    echo -e "${YELLOW}   Please check your SSH configuration and ensure:${NC}"
    echo -e "${YELLOW}   1. SSH key is added to cPanel (Home > SSH Access > Manage SSH Keys)${NC}"
    echo -e "${YELLOW}   2. Your public key is in ~/.ssh/authorized_keys on the server${NC}"
    echo -e "${YELLOW}   3. SSH is enabled in cPanel (Home > SSH Access)${NC}"
    echo -e "\n${YELLOW}   To setup SSH key:${NC}"
    echo -e "${BLUE}   ssh-keygen -t ed25519 -C 'deploy@francofrescura'${NC}"
    echo -e "${BLUE}   ssh-copy-id -p ${CPANEL_PORT:-22} $CPANEL_USER@$CPANEL_HOST${NC}"
    exit 1
fi

# Create backup on server (if configured)
if [ "${CREATE_BACKUP:-true}" = "true" ]; then
    echo -e "\n${YELLOW}2. Creating backup on server...${NC}"
    BACKUP_DIR="backups/franco-frescura-$(date +%Y%m%d-%H%M%S)"
    ssh -p "${CPANEL_PORT:-22}" "$CPANEL_USER@$CPANEL_HOST" \
        "mkdir -p ~/$BACKUP_DIR && [ -d $CPANEL_PATH ] && cp -r $CPANEL_PATH/* ~/$BACKUP_DIR/ 2>/dev/null || true"
    echo -e "${GREEN}   ✓ Backup created: ~/$BACKUP_DIR${NC}"
fi

# Deploy based on method
if [ "${DEPLOY_METHOD:-rsync}" = "rsync" ]; then
    echo -e "\n${YELLOW}3. Deploying via rsync...${NC}"

    # Rsync options
    RSYNC_OPTS="-avz --delete --progress"

    # Dry run first (if configured)
    if [ "${DRY_RUN:-false}" = "true" ]; then
        echo -e "${BLUE}   Running in DRY RUN mode (no changes will be made)${NC}"
        RSYNC_OPTS="$RSYNC_OPTS --dry-run"
    fi

    # Execute rsync
    rsync $RSYNC_OPTS \
        -e "ssh -p ${CPANEL_PORT:-22}" \
        --exclude='.git' \
        --exclude='.DS_Store' \
        --exclude='Thumbs.db' \
        "$PUBLIC_DIR/" \
        "$CPANEL_USER@$CPANEL_HOST:$CPANEL_PATH/"

    echo -e "${GREEN}   ✓ Deployment complete${NC}"

elif [ "${DEPLOY_METHOD}" = "scp" ]; then
    echo -e "\n${YELLOW}3. Deploying via SCP...${NC}"

    # Create tarball
    TARBALL="/tmp/franco-frescura-$(date +%Y%m%d%H%M%S).tar.gz"
    cd "$PUBLIC_DIR"
    tar -czf "$TARBALL" .
    echo -e "${BLUE}   Created tarball: $TARBALL${NC}"

    # Upload tarball
    scp -P "${CPANEL_PORT:-22}" "$TARBALL" "$CPANEL_USER@$CPANEL_HOST:/tmp/"

    # Extract on server
    ssh -p "${CPANEL_PORT:-22}" "$CPANEL_USER@$CPANEL_HOST" << EOF
        mkdir -p $CPANEL_PATH
        cd $CPANEL_PATH
        tar -xzf /tmp/$(basename $TARBALL)
        rm /tmp/$(basename $TARBALL)
EOF

    # Cleanup local tarball
    rm "$TARBALL"
    echo -e "${GREEN}   ✓ Deployment complete${NC}"

else
    echo -e "${RED}Error: Unknown deployment method: $DEPLOY_METHOD${NC}"
    exit 1
fi

# Set permissions on server
echo -e "\n${YELLOW}4. Setting permissions...${NC}"
ssh -p "${CPANEL_PORT:-22}" "$CPANEL_USER@$CPANEL_HOST" << 'EOF'
    find CPANEL_PATH_PLACEHOLDER -type d -exec chmod 755 {} \;
    find CPANEL_PATH_PLACEHOLDER -type f -exec chmod 644 {} \;
EOF
echo -e "${GREEN}   ✓ Permissions set${NC}"

# Verify deployment
echo -e "\n${YELLOW}5. Verifying deployment...${NC}"
REMOTE_FILE_COUNT=$(ssh -p "${CPANEL_PORT:-22}" "$CPANEL_USER@$CPANEL_HOST" "find $CPANEL_PATH -type f | wc -l")
LOCAL_FILE_COUNT=$(find "$PUBLIC_DIR" -type f | wc -l)

echo -e "${BLUE}   Local files:  $LOCAL_FILE_COUNT${NC}"
echo -e "${BLUE}   Remote files: $REMOTE_FILE_COUNT${NC}"

if [ "$REMOTE_FILE_COUNT" -gt 0 ]; then
    echo -e "${GREEN}   ✓ Deployment verified${NC}"
else
    echo -e "${RED}   ✗ Warning: No files found on remote server${NC}"
fi

# Final summary
echo -e "\n${BLUE}================================================${NC}"
echo -e "${GREEN}✓ Deployment complete!${NC}"
echo -e "${BLUE}================================================${NC}"
echo -e "\n${YELLOW}Site URL:${NC} ${BLUE}https://francofrescura.sahistory.org.za${NC}"
echo -e "${YELLOW}Files deployed:${NC} ${BLUE}$LOCAL_FILE_COUNT${NC}"

if [ "${CREATE_BACKUP:-true}" = "true" ]; then
    echo -e "${YELLOW}Backup location:${NC} ${BLUE}~/$BACKUP_DIR${NC}"
fi

echo -e "\n${YELLOW}Troubleshooting:${NC}"
echo -e "1. If site doesn't load, check cPanel Document Root settings"
echo -e "2. If images are missing, verify file permissions (644 for files, 755 for directories)"
echo -e "3. If URLs don't work, ensure .htaccess is present and mod_rewrite is enabled"
echo -e "4. Test with: ${BLUE}curl -I https://francofrescura.sahistory.org.za${NC}\n"
