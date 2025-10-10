---
title: "Search"
layout: "search"
type: "page"
---

# Search the Archive

Search across all articles, lectures, and documentation in the Franco Frescura Archive.

<div id="search-container">
  <input type="text" id="search-input" placeholder="Search articles, topics, keywords..." autocomplete="off">
  <div id="search-results"></div>
</div>

<style>
#search-container {
  max-width: 800px;
  margin: 2rem auto;
}

#search-input {
  width: 100%;
  padding: 1rem;
  font-size: 1.1rem;
  border: 2px solid var(--primary-color, #8B4513);
  border-radius: 4px;
  margin-bottom: 1rem;
}

#search-input:focus {
  outline: none;
  border-color: var(--accent-color, #A0522D);
  box-shadow: 0 0 0 3px rgba(139, 69, 19, 0.1);
}

#search-results {
  margin-top: 2rem;
}

.search-result {
  padding: 1.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: #fff;
  transition: box-shadow 0.2s;
}

.search-result:hover {
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.search-result-title {
  font-size: 1.3rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.search-result-title a {
  color: var(--primary-color, #8B4513);
  text-decoration: none;
}

.search-result-title a:hover {
  text-decoration: underline;
}

.search-result-section {
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
  text-transform: capitalize;
}

.search-result-snippet {
  color: #333;
  line-height: 1.6;
}

.search-result-snippet mark {
  background-color: #fff3cd;
  padding: 2px 4px;
  font-weight: bold;
}

.search-no-results {
  text-align: center;
  color: #666;
  padding: 3rem;
  font-size: 1.1rem;
}

.search-stats {
  color: #666;
  margin-bottom: 1rem;
  font-size: 0.9rem;
}
</style>

<script src="/js/search.js"></script>
