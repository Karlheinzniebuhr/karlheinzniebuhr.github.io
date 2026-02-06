(function () {
  'use strict';

  var overlay = document.getElementById('searchOverlay');
  var input = document.getElementById('searchInput');
  var results = document.getElementById('searchResults');
  var index = null;
  var store = null;

  // Open / close
  function openSearch() {
    overlay.classList.add('active');
    input.value = '';
    input.focus();
    results.innerHTML = '<div class="search-empty">Type to search across all posts\u2026</div>';
  }

  function closeSearch() {
    overlay.classList.remove('active');
    input.value = '';
  }

  // Wire up all triggers
  document.querySelectorAll('[data-search-trigger]').forEach(function (el) {
    el.addEventListener('click', function (e) {
      e.preventDefault();
      openSearch();
    });
  });

  // Keyboard shortcut
  document.addEventListener('keydown', function (e) {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      if (overlay.classList.contains('active')) {
        closeSearch();
      } else {
        openSearch();
      }
    }
    if (e.key === 'Escape' && overlay.classList.contains('active')) {
      closeSearch();
    }
  });

  // Click outside modal
  overlay.addEventListener('click', function (e) {
    if (e.target === overlay) closeSearch();
  });

  // Close button
  var closeBtn = overlay.querySelector('.search-close');
  if (closeBtn) closeBtn.addEventListener('click', closeSearch);

  // Build index
  function buildIndex(data) {
    store = {};
    index = lunr(function () {
      this.ref('url');
      this.field('title', { boost: 10 });
      this.field('categories', { boost: 5 });
      this.field('content');

      data.forEach(function (item) {
        this.add(item);
        store[item.url] = item;
      }, this);
    });
  }

  // Fetch data
  var baseurl = document.querySelector('meta[name="baseurl"]');
  var prefix = baseurl ? baseurl.getAttribute('content') : '';
  var dataUrl = prefix + '/search.json';

  fetch(dataUrl)
    .then(function (r) { return r.json(); })
    .then(function (data) { buildIndex(data); })
    .catch(function (err) { console.warn('Search index load failed:', err); });

  // Search
  input.addEventListener('input', function () {
    if (!index) {
      results.innerHTML = '<div class="search-empty">Loading search index\u2026</div>';
      return;
    }

    var query = input.value.trim();
    if (!query) {
      results.innerHTML = '<div class="search-empty">Type to search across all posts\u2026</div>';
      return;
    }

    var hits;
    try {
      hits = index.search(query + '~1');
    } catch (e) {
      try {
        hits = index.search(query);
      } catch (e2) {
        hits = [];
      }
    }

    if (hits.length === 0) {
      results.innerHTML = '<div class="search-empty">No results for \u201c' + escapeHtml(query) + '\u201d</div>';
      return;
    }

    var html = '';
    hits.slice(0, 12).forEach(function (hit) {
      var item = store[hit.ref];
      if (!item) return;
      var excerpt = item.content ? item.content.substring(0, 150) + '\u2026' : '';
      html += '<a href="' + item.url + '" class="search-result-item">' +
        '<div class="search-result-title">' + escapeHtml(item.title) + '</div>' +
        '<div class="search-result-date">' + escapeHtml(item.date) + '</div>' +
        (excerpt ? '<div class="search-result-excerpt">' + escapeHtml(excerpt) + '</div>' : '') +
        '</a>';
    });
    results.innerHTML = html;
  });

  function escapeHtml(str) {
    var div = document.createElement('div');
    div.appendChild(document.createTextNode(str));
    return div.innerHTML;
  }
})();
