/**
 * Search functionality for Franco Frescura Archive
 * Uses Hugo's JSON index for client-side search
 */

let searchIndex = [];
let searchInput;
let searchResults;

// Initialize search when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
  searchInput = document.getElementById('search-input');
  searchResults = document.getElementById('search-results');

  if (!searchInput || !searchResults) {
    return;
  }

  // Load search index
  loadSearchIndex();

  // Setup search input handler with debouncing
  let searchTimeout;
  searchInput.addEventListener('input', function() {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => performSearch(this.value), 300);
  });

  // Focus search input
  searchInput.focus();
});

/**
 * Load the search index from Hugo's JSON output
 */
function loadSearchIndex() {
  fetch('/index.json')
    .then(response => response.json())
    .then(data => {
      searchIndex = data;
      console.log(`Search index loaded: ${searchIndex.length} pages`);
    })
    .catch(error => {
      console.error('Failed to load search index:', error);
      searchResults.innerHTML = '<div class="search-no-results">Search is temporarily unavailable.</div>';
    });
}

/**
 * Perform search across the index
 */
function performSearch(query) {
  if (!query || query.length < 2) {
    searchResults.innerHTML = '';
    return;
  }

  const results = searchInIndex(query);
  displayResults(results, query);
}

/**
 * Search the index for matching pages
 */
function searchInIndex(query) {
  const searchTerms = query.toLowerCase().split(/\s+/).filter(term => term.length > 1);
  const results = [];

  searchIndex.forEach(page => {
    let score = 0;
    const titleLower = (page.title || '').toLowerCase();
    const contentLower = (page.content || '').toLowerCase();
    const tagsLower = (page.tags || []).join(' ').toLowerCase();
    const categoriesLower = (page.categories || []).join(' ').toLowerCase();

    searchTerms.forEach(term => {
      // Title matches (highest weight)
      if (titleLower.includes(term)) {
        score += 10;
      }

      // Tags and categories matches (medium weight)
      if (tagsLower.includes(term)) {
        score += 5;
      }
      if (categoriesLower.includes(term)) {
        score += 5;
      }

      // Content matches (lower weight)
      if (contentLower.includes(term)) {
        score += 1;
      }
    });

    if (score > 0) {
      results.push({
        page: page,
        score: score
      });
    }
  });

  // Sort by score (highest first)
  results.sort((a, b) => b.score - a.score);

  return results;
}

/**
 * Display search results
 */
function displayResults(results, query) {
  if (results.length === 0) {
    searchResults.innerHTML = `
      <div class="search-no-results">
        No results found for "<strong>${escapeHtml(query)}</strong>"
        <br><br>
        Try different keywords or check your spelling.
      </div>
    `;
    return;
  }

  let html = `<div class="search-stats">Found ${results.length} result${results.length !== 1 ? 's' : ''} for "<strong>${escapeHtml(query)}</strong>"</div>`;

  results.slice(0, 50).forEach(result => {
    const page = result.page;
    const snippet = createSnippet(page.content, query);
    const section = page.section || 'General';

    html += `
      <div class="search-result">
        <div class="search-result-title">
          <a href="${page.permalink}">${escapeHtml(page.title)}</a>
        </div>
        <div class="search-result-section">${escapeHtml(section)}</div>
        <div class="search-result-snippet">${snippet}</div>
      </div>
    `;
  });

  if (results.length > 50) {
    html += `<div class="search-stats">Showing top 50 results of ${results.length}</div>`;
  }

  searchResults.innerHTML = html;
}

/**
 * Create a snippet from content with highlighted search terms
 */
function createSnippet(content, query, maxLength = 200) {
  if (!content) {
    return 'No content available';
  }

  const searchTerms = query.toLowerCase().split(/\s+/).filter(term => term.length > 1);
  const contentLower = content.toLowerCase();

  // Find first occurrence of any search term
  let startPos = -1;
  searchTerms.forEach(term => {
    const pos = contentLower.indexOf(term);
    if (pos !== -1 && (startPos === -1 || pos < startPos)) {
      startPos = pos;
    }
  });

  // Extract snippet around the match
  let snippet;
  if (startPos === -1) {
    snippet = content.substring(0, maxLength);
  } else {
    const start = Math.max(0, startPos - 50);
    const end = Math.min(content.length, startPos + maxLength);
    snippet = (start > 0 ? '...' : '') + content.substring(start, end) + (end < content.length ? '...' : '');
  }

  // Highlight search terms
  searchTerms.forEach(term => {
    const regex = new RegExp(`(${escapeRegex(term)})`, 'gi');
    snippet = snippet.replace(regex, '<mark>$1</mark>');
  });

  return snippet;
}

/**
 * Escape HTML to prevent XSS
 */
function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

/**
 * Escape regex special characters
 */
function escapeRegex(text) {
  return text.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}
