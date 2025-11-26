# Testing Guide - Priority 1 Content Restructuring

**Branch:** `claude/priority1-content-restructure-011CV5c1yW1YPNUhJxzap2Ng`

---

## Quick Start Testing

### 1. Check Out the Branch

```bash
cd /path/to/franco-frescura
git fetch origin
git checkout claude/priority1-content-restructure-011CV5c1yW1YPNUhJxzap2Ng
```

### 2. Build and Run Hugo Site Locally

**Option A: Using Docker (Recommended)**

```bash
# Navigate to project root
cd /path/to/franco-frescura

# Run Hugo dev server with Docker
docker-compose -f docker-compose.hugo.yml up

# Or use the dev version with both sites
docker-compose -f docker-compose.dev.yml up
```

Then open: **http://localhost:1313**

**Option B: Using Hugo CLI Directly**

```bash
cd hugo-site
hugo server --bind 0.0.0.0
```

Then open: **http://localhost:1313**

---

## What to Test

### Test 1: Verify Site Builds Successfully ✅

**Expected:** Site should build without errors

```bash
cd hugo-site
hugo --quiet

# Should output:
# Total in X ms
# No error messages
```

**Check for:**
- ✅ No build errors
- ✅ No missing file warnings
- ✅ Page count is reasonable (~249 pages)

---

### Test 2: Check Restructured Lectures Section 📚

**What Changed:**
- Created new `/lectures/culture-transition/` subsection
- Moved 4 lecture files from `/pages` to this location

**URLs to Test:**

1. **Main lectures page:**
   - http://localhost:1313/lectures/

2. **Culture in Transition subsection:**
   - http://localhost:1313/lectures/culture-transition/
   - http://localhost:1313/lectures/culture-transition/lectures_culture_transition_lecture1/
   - http://localhost:1313/lectures/culture-transition/lectures_culture_transition_lecture2/
   - http://localhost:1313/lectures/culture-transition/lectures_culture_transition_lecture3/
   - http://localhost:1313/lectures/culture-transition/lectures_culture_transition_lecture4/

3. **Renamed paper:**
   - http://localhost:1313/lectures/transmission-and-change-in-architecture/

**What to Check:**
- ✅ All pages load without 404 errors
- ✅ Content displays correctly
- ✅ Navigation shows culture-transition subsection
- ✅ Lecture series has its own index page

---

### Test 3: Check Architecture Section Reorganization 🏛️

**What Changed:**
- Moved conservation report from `/pages` to `/architecture/conservation/`
- Renamed colonial paper to descriptive name
- Removed redundant index files

**URLs to Test:**

1. **Conservation report (moved):**
   - http://localhost:1313/architecture/conservation/conservation-report-keiskamahoek-impactstudy/

2. **Colonial paper (renamed):**
   - http://localhost:1313/architecture/colonial/village-development-patterns-karoo/

3. **Mission stations intro (renamed):**
   - http://localhost:1313/architecture/mission-stations/introduction-to-mission-stations/

**What to Check:**
- ✅ All pages load correctly
- ✅ Papers display full content
- ✅ No broken links within these pages

---

### Test 4: Check Urban Issues Section 🏙️

**What Changed:**
- Renamed development paper to descriptive name
- Removed minimal index files

**URLs to Test:**

1. **Main urban issues page:**
   - http://localhost:1313/urban-issues/

2. **Renamed paper:**
   - http://localhost:1313/urban-issues/designing-for-developing-economy/

**What to Check:**
- ✅ Section page loads
- ✅ All urban issues articles listed
- ✅ Renamed paper displays correctly

---

### Test 5: Verify Removed Files Don't Exist ❌

**These URLs should return 404:**

Old redundant index files that were removed:
- http://localhost:1313/architecture/architecture-index/
- http://localhost:1313/graphic-work/graphic-work-index/
- http://localhost:1313/postal-history/postal-history-index/
- http://localhost:1313/lectures/lectures-main-index/
- http://localhost:1313/urban-issues/urban-issues-index/
- http://localhost:1313/pages/travelogue/ (duplicate)

**What to Check:**
- ✅ These pages should return 404 errors
- ✅ This is expected behavior (files were redundant)

---

### Test 6: Check /pages Directory 📄

**What Changed:**
- Cleaned from 9 files down to 1 file

**URL to Test:**
- http://localhost:1313/pages/visual-archive-index/

**What to Check:**
- ✅ Visual archive placeholder still exists
- ✅ Other pages files are gone (moved to proper sections)

---

### Test 7: Run Link Checker 🔗

**Option A: Using Python Script**

```bash
cd /path/to/franco-frescura
python3 scripts/test_hugo_links.py
```

**Expected Output:**
- List of all internal links tested
- Success rate (should be >95%)
- Any broken links highlighted

**Option B: Manual Link Check**

Navigate through the site and click:
- Main navigation menu items
- Section landing pages
- Internal content links
- Breadcrumb navigation

---

### Test 8: Verify Search Functionality 🔍

**URL to Test:**
- http://localhost:1313/search/

**What to Test:**
1. Search for: "culture transition"
   - ✅ Should find the new lecture series
2. Search for: "keiskammahoek"
   - ✅ Should find the conservation report in new location
3. Search for: "village development karoo"
   - ✅ Should find the renamed colonial paper

---

### Test 9: Check Navigation Menu 🧭

**What to Check:**

1. **Main Navigation:**
   - ✅ All top-level menu items work
   - ✅ Architecture dropdown shows subsections
   - ✅ No broken links in menu

2. **Breadcrumbs:**
   - ✅ Breadcrumbs show correct hierarchy
   - ✅ Example: Lectures > Culture in Transition > Lecture 1

3. **Section Listings:**
   - ✅ Each section page lists its content
   - ✅ No missing pages in listings

---

## Automated Testing

### Run All Tests at Once

```bash
# From project root
cd /path/to/franco-frescura

# Build the site
cd hugo-site && hugo --quiet && cd ..

# Run link checker
python3 scripts/test_hugo_links.py

# Check for orphaned files
find hugo-site/content/pages -type f -name "*.md" ! -name "visual-archive-index.md"
# Should only return: (empty or just visual-archive-index.md)
```

---

## Expected Results Summary

### Build Status
- ✅ **Hugo build:** Success, ~249 pages
- ✅ **Build time:** <500ms
- ✅ **Warnings:** None expected

### Content Organization
- ✅ **Lectures:** 4 culture-transition lectures in subsection
- ✅ **Architecture:** Conservation report in proper location
- ✅ **Urban Issues:** Papers with descriptive names
- ✅ **Pages:** Cleaned to 1 file

### Link Health
- ✅ **Internal links:** >95% working
- ✅ **Section pages:** All accessible
- ✅ **Navigation:** All menu items work

### Files Removed
- ✅ **13 redundant files:** Return 404 (expected)
- ✅ **Duplicate content:** Removed

---

## Common Issues & Solutions

### Issue: Hugo Command Not Found

**Solution:** Use Docker instead:
```bash
docker-compose -f docker-compose.hugo.yml up
```

### Issue: Port 1313 Already in Use

**Solution:** Kill existing Hugo process or use different port:
```bash
hugo server --port 1314
```

### Issue: Some Links Return 404

**Check if:**
1. File was intentionally removed (see "Removed Files" list above)
2. File was renamed (check the commit changes)
3. Link needs updating in source markdown

### Issue: Build Errors

**Check:**
1. You're on the correct branch
2. All files were pulled properly
3. No local modifications conflicting

---

## Testing Checklist

Use this checklist to track your testing:

- [ ] Branch checked out successfully
- [ ] Hugo site builds without errors
- [ ] Localhost server running
- [ ] Main homepage loads
- [ ] Lectures section accessible
- [ ] Culture in Transition subsection works
- [ ] All 4 culture lectures load
- [ ] Conservation report in new location
- [ ] Colonial paper renamed correctly
- [ ] Urban issues papers accessible
- [ ] Navigation menu works
- [ ] Search functionality works
- [ ] Link checker shows >95% success
- [ ] Redundant files properly return 404
- [ ] No unexpected errors in console

---

## Reporting Issues

If you find issues during testing, please note:

1. **What page/URL** has the problem
2. **Expected behavior** vs **actual behavior**
3. **Error messages** (if any)
4. **Browser console errors** (F12 → Console tab)

Example issue report:
```
URL: http://localhost:1313/lectures/culture-transition/
Expected: Page loads with lecture series index
Actual: 404 error
Error: "page not found"
```

---

## Next Steps After Testing

### If Tests Pass ✅
1. Approve the changes
2. Merge the PR
3. Monitor CI/CD pipelines
4. Move to Priority 2 tasks

### If Issues Found ❌
1. Document the issues
2. Create fix commits
3. Re-test
4. Update PR

---

## Quick Reference Commands

```bash
# Check out branch
git checkout claude/priority1-content-restructure-011CV5c1yW1YPNUhJxzap2Ng

# Start Hugo server (Docker)
docker-compose -f docker-compose.hugo.yml up

# Start Hugo server (CLI)
cd hugo-site && hugo server

# Build site
cd hugo-site && hugo

# Run link checker
python3 scripts/test_hugo_links.py

# Check git status
git status

# View changes
git log --oneline -5
```

---

**Last Updated:** November 26, 2025
**Related:** docs/PRIORITY_1_SUMMARY.md
