# Action Items - Franco Frescura Archive Improvements

**Generated:** November 13, 2025
**Full Analysis:** See [CONTENT_ANALYSIS_AND_IMPROVEMENTS.md](./CONTENT_ANALYSIS_AND_IMPROVEMENTS.md)

---

## Summary

✅ **Migration Status:** 100% complete - all content successfully migrated
⚠️ **Areas for Improvement:** Content organization, template reusability, analytics

---

## Priority 1: Critical (Do First) 🔴

### 1. Restructure `/pages` Directory Content
**Issue:** Content in wrong locations causing organizational confusion

**Actions:**
- [ ] Move `lectures_culture_transition_lecture*.md` (4 files) → `/lectures/culture-transition/`
- [ ] Move `conservation-report-keiskamahoek-impactstudy.md` → `/architecture/conservation/`
- [ ] Review and remove duplicate `indigenous-architecture-index.md`
- [ ] Review and consolidate `urbanisation-housing-index.md`
- [ ] Decision needed: Keep or remove `visual-archive-index.md` (placeholder page)
- [ ] Remove or consolidate `travelogue.md` (duplicate exists in graphic-work)
- [ ] Update all internal links affected by moves

**Impact:** Improves content organization, URL structure, navigation clarity

**Estimate:** 2-3 hours

---

### 2. Clean Up Duplicate Index Files
**Issue:** Both `_index.md` and `section-name-index.md` exist in many sections

**Duplicates Found:**
- [ ] `architecture/architecture-index.md` vs `architecture/_index.md`
- [ ] `architecture/colonial/colonial-setlement-index.md` vs `_index.md`
- [ ] `architecture/conservation/historical-conservation--index.md` vs `_index.md`
- [ ] `architecture/indigenous/indiginous-architecture-index.md` vs `_index.md`
- [ ] `architecture/mission-stations/mission-stations-index.md` vs `_index.md`
- [ ] `biography/franco-frescura-index.md` vs `_index.md`
- [ ] `graphic-work/graphic-work-index.md` vs `_index.md`
- [ ] `lectures/lectures-index.md` and `lectures-main-index.md` vs `_index.md`
- [ ] `postal-history/postal-history-index.md` vs `_index.md`
- [ ] `urban-issues/urban-issues-*-index.md` (3 files) vs `_index.md`

**Actions:**
- [ ] For each duplicate, review if content-based index has unique content
- [ ] If unique content exists, merge into section `_index.md`
- [ ] If no unique content, delete redundant file
- [ ] Update navigation links
- [ ] Run link checker to verify no broken links

**Impact:** Eliminates confusion, cleaner URLs, better SEO

**Estimate:** 3-4 hours

---

### 3. Fix Content Frontmatter Consistency
**Issue:** Inconsistent metadata across content files

**Actions:**
- [ ] Audit all markdown files for missing descriptions
- [ ] Add descriptions to files without them (SEO critical)
- [ ] Standardize date format to `YYYY-MM-DD`
- [ ] Review and add missing keywords/tags
- [ ] Verify all category assignments are correct
- [ ] Ensure all content has proper `type` field

**Script to help:**
```bash
cd hugo-site
# Find files without descriptions
grep -L "description:" content/**/*.md

# Check date formats
grep "^date:" content/**/*.md | grep -v "date: '[0-9]\{4\}"
```

**Impact:** Better SEO, improved metadata, consistent structure

**Estimate:** 4-5 hours

---

## Priority 2: Important (This Sprint) 🟡

### 4. Generalize Theme for Reusability
**Goal:** Make this template usable for other SAHO subsites

**Actions:**
- [ ] Rename theme `frescura-academic` → `saho-academic`
- [ ] Move all Franco-specific content to `hugo.toml` configuration
- [ ] Create theme configuration template
- [ ] Document theme customization options
- [ ] Create theme README with setup instructions
- [ ] Test theme with different color schemes
- [ ] Create example site configurations for different archive types

**Files to Create:**
- `themes/saho-academic/README.md`
- `themes/saho-academic/theme.toml`
- `docs/THEME_CUSTOMIZATION.md`
- `config-template.toml`

**Impact:** Enables rapid creation of new SAHO subsites

**Estimate:** 1-2 days

---

### 5. Add Analytics Integration
**Goal:** Enable visitor tracking and insights

**Actions:**
- [ ] Choose analytics platform (recommend Plausible for privacy)
- [ ] Add analytics configuration to `hugo.toml`
- [ ] Create partial template for analytics scripts
- [ ] Add conditional loading (only in production)
- [ ] Add GDPR-compliant cookie consent if needed
- [ ] Document analytics setup in SAHO subsite guide
- [ ] Test analytics in staging environment

**Configuration Addition:**
```toml
[params.analytics]
  provider = "plausible"  # Options: plausible, google, matomo, none
  plausibleDomain = "francofrescura.sahistory.org.za"
  googleAnalyticsId = ""
  matomoSiteId = ""
  anonymizeIP = true
```

**Impact:** Enables data-driven improvements, understand user behavior

**Estimate:** 4-6 hours

---

### 6. Implement Structured Data (Schema.org)
**Goal:** Enhance SEO with rich snippets

**Actions:**
- [ ] Create `layouts/partials/structured-data.html`
- [ ] Add JSON-LD for different content types:
  - WebSite (homepage)
  - Person (biography pages)
  - Article (research articles)
  - ArchiveOrganization (about SAHO)
- [ ] Include structured data in `baseof.html`
- [ ] Test with Google Rich Results Test
- [ ] Document in style guide

**Impact:** Better search engine visibility, rich snippets in results

**Estimate:** 4-6 hours

---

### 7. Create Content Archetypes
**Goal:** Standardize content creation

**Actions:**
- [ ] Create `archetypes/` directory
- [ ] Define archetype for each content type:
  - `default.md` - Generic page
  - `biography.md` - Person profiles
  - `article.md` - Research articles
  - `document.md` - Historical documents
  - `event.md` - Historical events
  - `place.md` - Location pages
- [ ] Document archetype usage
- [ ] Test archetype generation

**Example Usage:**
```bash
hugo new biography/person-name.md --kind biography
```

**Impact:** Faster content creation, consistent structure, complete metadata

**Estimate:** 3-4 hours

---

## Priority 3: Enhancement (Next Sprint) 🟢

### 8. Add Related Content System
- [ ] Configure Hugo related content parameters
- [ ] Create related content partial template
- [ ] Add to single page layout
- [ ] Style related content section
- [ ] Test relevance and adjust weights

**Estimate:** 2-3 hours

---

### 9. Improve Search Functionality
- [ ] Enhance search UI/UX
- [ ] Add section/category filters
- [ ] Add date range filtering
- [ ] Improve result relevance scoring
- [ ] Add result highlighting
- [ ] Add "no results" helpful messaging

**Estimate:** 1 day

---

### 10. Optimize Images
- [ ] Implement Hugo image processing
- [ ] Generate responsive images (srcset)
- [ ] Convert images to WebP format
- [ ] Add lazy loading attribute
- [ ] Create image shortcode for consistent usage
- [ ] Document image guidelines

**Estimate:** 1 day

---

### 11. Create SAHO Subsite Setup Documentation
- [ ] Write `docs/SAHO_SUBSITE_SETUP.md`
- [ ] Create step-by-step setup guide
- [ ] Document configuration options
- [ ] Create deployment guides for:
  - Netlify
  - GitHub Pages
  - Vercel
  - cPanel
- [ ] Create troubleshooting section
- [ ] Record setup video tutorial (optional)

**Estimate:** 1-2 days

---

## Priority 4: Future Enhancements 🔵

### 12. Multi-Language Support
- [ ] Design language directory structure
- [ ] Update theme for i18n support
- [ ] Create language switcher component
- [ ] Configure language fallbacks
- [ ] Document translation workflow

**Estimate:** 2-3 days

---

### 13. Component Library
- [ ] Create shortcode for cards
- [ ] Create shortcode for timelines
- [ ] Create shortcode for image galleries
- [ ] Create shortcode for person cards
- [ ] Create shortcode for citations
- [ ] Document all components with examples

**Estimate:** 2-3 days

---

### 14. Advanced Features
- [ ] Timeline visualizations (for biographical content)
- [ ] Interactive maps (for places)
- [ ] Document viewer/reader
- [ ] Citation generator
- [ ] Print-friendly pages
- [ ] Dark mode toggle
- [ ] Reading progress indicator

**Estimate:** 1-2 weeks

---

## Quick Wins (Can Do Anytime) ⚡

These are small improvements that can be done quickly:

- [ ] Add "Back to top" button
- [ ] Add print stylesheet
- [ ] Create 404 page with helpful navigation
- [ ] Add breadcrumbs to all pages
- [ ] Create accessibility statement page
- [ ] Add RSS feed links
- [ ] Create sitemap.xml (if not auto-generated)
- [ ] Add robots.txt improvements
- [ ] Create favicon set (multiple sizes)
- [ ] Add Open Graph images for all sections

**Each estimate:** 15-30 minutes

---

## Testing Checklist

After implementing changes, run these tests:

### Content Tests
- [ ] All internal links work
- [ ] All images load correctly
- [ ] No duplicate content URLs
- [ ] All pages have descriptions
- [ ] Navigation is logical and complete

### Technical Tests
- [ ] Hugo build succeeds without errors
- [ ] No broken links (run link checker)
- [ ] Mobile responsive on all devices
- [ ] Fast page load times (< 3 seconds)
- [ ] Valid HTML (W3C validator)

### SEO Tests
- [ ] All pages have meta descriptions
- [ ] All images have alt text
- [ ] Proper heading hierarchy (h1, h2, h3)
- [ ] Canonical URLs set correctly
- [ ] XML sitemap generates correctly
- [ ] robots.txt is correct

### Accessibility Tests
- [ ] Keyboard navigation works
- [ ] Screen reader friendly
- [ ] Sufficient color contrast
- [ ] ARIA labels where needed
- [ ] No flashing content

---

## Resource Estimates

### Total Time by Priority

| Priority | Items | Est. Time | Team Members |
|----------|-------|-----------|-------------|
| P1 (Critical) | 3 items | 9-12 hours | 1-2 people |
| P2 (Important) | 4 items | 3-4 days | 1-2 people |
| P3 (Enhancement) | 4 items | 4-6 days | 1 person |
| P4 (Future) | 3 items | 2-3 weeks | 1-2 people |

### Recommended Sprint Plan

**Sprint 1 (Week 1):** Priority 1 items
- Content restructuring
- Duplicate cleanup
- Frontmatter consistency

**Sprint 2 (Week 2-3):** Priority 2 items
- Theme generalization
- Analytics integration
- Structured data
- Content archetypes

**Sprint 3 (Week 4-5):** Priority 3 items
- Related content
- Enhanced search
- Image optimization
- Documentation

**Future Sprints:** Priority 4 items as needed

---

## Success Metrics

### Content Quality
- ✅ 100% of pages have descriptions
- ✅ 100% of images have alt text
- ✅ 0 broken internal links
- ✅ Consistent frontmatter structure

### User Experience
- ✅ < 3 second page load time
- ✅ Mobile responsive score > 95
- ✅ Accessibility score > 90
- ✅ Clear information architecture

### Template Readiness
- ✅ Can set up new subsite in < 4 hours
- ✅ Comprehensive documentation exists
- ✅ Theme is fully configurable
- ✅ Example configurations available

### SEO Performance
- ✅ Rich snippets appearing in search
- ✅ All pages indexed
- ✅ Increasing organic traffic
- ✅ Good search rankings for key terms

---

## Questions for SAHO Team

Before proceeding with some items, clarification needed:

1. **Analytics Platform:** Which analytics service should be used across SAHO subsites?
2. **Multi-language:** Which languages should be supported initially?
3. **Visual Archive:** Should the placeholder page be developed or removed?
4. **Branding:** Are there specific SAHO brand guidelines to follow?
5. **Domain Structure:** Will all subsites use `[name].sahistory.org.za` format?
6. **Budget:** Any budget for paid services (analytics, hosting, etc.)?
7. **Timeline:** What's the target date for the next SAHO subsite launch?

---

## Contact

For questions or clarifications on these action items:
- Review the full analysis: [CONTENT_ANALYSIS_AND_IMPROVEMENTS.md](./CONTENT_ANALYSIS_AND_IMPROVEMENTS.md)
- Check project status: [PROJECT_STATUS.md](./PROJECT_STATUS.md)
- Refer to migration docs: [MIGRATION_COMPLETE.md](./MIGRATION_COMPLETE.md)

---

**Last Updated:** November 13, 2025
**Next Review:** After Sprint 1 completion
