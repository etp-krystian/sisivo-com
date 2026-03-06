(() => {
  const prose = document.querySelector('.is-services .prose');
  if (!prose) return;

  const headings = Array.from(prose.querySelectorAll('h2'));
  const relatedHeading = headings.find((h) => h.textContent.trim().toLowerCase() === 'related services');
  if (!relatedHeading) return;

  let list = relatedHeading.nextElementSibling;
  while (list && list.tagName !== 'UL' && list.tagName !== 'H2') {
    list = list.nextElementSibling;
  }

  if (!list || list.tagName !== 'UL') return;

  const links = Array.from(list.querySelectorAll('a[href]'));
  if (!links.length) return;

  const wrapper = document.createElement('div');
  wrapper.className = 'related-services-explorer';

  const intro = document.createElement('p');
  intro.className = 'related-services-intro';
  intro.textContent = 'Explore the next best step based on your current service page.';
  wrapper.appendChild(intro);

  const grid = document.createElement('ul');
  grid.className = 'related-services-grid';

  links.forEach((anchor) => {
    const item = document.createElement('li');

    const link = document.createElement('a');
    link.className = 'related-service-link';
    link.href = anchor.href;

    const label = document.createElement('span');
    label.textContent = anchor.textContent.trim();

    const icon = document.createElement('span');
    icon.className = 'material-symbols-rounded';
    icon.setAttribute('aria-hidden', 'true');
    icon.textContent = 'arrow_forward';

    link.appendChild(label);
    link.appendChild(icon);
    item.appendChild(link);
    grid.appendChild(item);
  });

  wrapper.appendChild(grid);
  list.replaceWith(wrapper);
})();
