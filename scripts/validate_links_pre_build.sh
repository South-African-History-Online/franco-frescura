#!/bin/bash
#
# Pre-build link validation hook for Hugo
# Run this before building the Hugo site to catch broken links early
#
# Usage:
#   ./scripts/validate_links_pre_build.sh
#
# Or add to package.json:
#   "scripts": { "prebuild": "./scripts/validate_links_pre_build.sh" }
#

set -e

echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║              Pre-Build Link Validation                                ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "⚠️  Python 3 not found. Skipping link validation."
    exit 0
fi

# Check if required Python modules are installed
python3 -c "import yaml, bs4" 2>/dev/null || {
    echo "⚠️  Required Python modules not installed. Skipping link validation."
    echo "   Install with: pip install PyYAML beautifulsoup4 lxml"
    exit 0
}

# Run link analysis
echo "🔍 Analyzing internal links..."
echo ""

if python3 scripts/analyze_links.py; then
    echo ""
    echo "✅ Link validation passed"
    exit 0
else
    EXIT_CODE=$?
    echo ""
    echo "❌ Link validation found issues"
    echo ""
    echo "Options:"
    echo "  1. Fix the broken links"
    echo "  2. Run: python3 scripts/fix_all_links.py"
    echo "  3. Skip validation: SKIP_LINK_CHECK=1 hugo"
    echo ""

    # Check if we should fail the build
    if [ "$SKIP_LINK_CHECK" = "1" ]; then
        echo "⚠️  Skipping link check (SKIP_LINK_CHECK=1)"
        exit 0
    fi

    exit $EXIT_CODE
fi
