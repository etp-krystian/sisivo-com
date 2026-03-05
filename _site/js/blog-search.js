(() => {
  const input = document.getElementById("blog-search-input");
  const list = document.getElementById("blog-posts-list");
  const meta = document.getElementById("blog-search-meta");
  const noResults = document.getElementById("blog-no-results");

  if (!input || !list) return;

  const items = Array.from(list.querySelectorAll("[data-search]"));
  const total = items.length;

  const normalize = (value) =>
    (value || "")
      .toString()
      .toLowerCase()
      .normalize("NFKD")
      .replace(/[\u0300-\u036f]/g, "")
      .trim();

  const updateMeta = (shown) => {
    if (!meta) return;
    meta.textContent = shown === total ? `${total} posts` : `${shown} of ${total} posts`;
  };

  const run = () => {
    const q = normalize(input.value);
    const terms = q ? q.split(/\s+/).filter(Boolean) : [];
    let shown = 0;

    for (const item of items) {
      const haystack = normalize(item.getAttribute("data-search"));
      const match = terms.length
        ? terms.every((term) => haystack.includes(term))
        : true;

      item.hidden = !match;
      if (match) shown += 1;
    }

    if (noResults) noResults.hidden = shown !== 0;
    updateMeta(shown);
  };

  updateMeta(total);
  input.addEventListener("input", run, { passive: true });
})();

