(() => {
  const prose = document.querySelector('.is-services .prose');
  if (!prose) return;

  const headings = Array.from(prose.querySelectorAll('h2'));
  const faqHeading = headings.find((h) => h.textContent.trim().toLowerCase() === 'faq');
  if (!faqHeading) return;

  const blockNodes = [];
  let cursor = faqHeading.nextElementSibling;
  while (cursor && cursor.tagName !== 'H2') {
    blockNodes.push(cursor);
    cursor = cursor.nextElementSibling;
  }

  if (!blockNodes.length) return;

  const accordion = document.createElement('div');
  accordion.className = 'faq-accordion';

  for (let i = 0; i < blockNodes.length; i += 1) {
    const maybeQuestion = blockNodes[i];
    if (maybeQuestion.tagName !== 'H3') continue;

    const item = document.createElement('details');
    item.className = 'faq-item';

    const summary = document.createElement('summary');
    summary.className = 'faq-question';
    summary.textContent = maybeQuestion.textContent.trim();
    item.appendChild(summary);

    const answer = document.createElement('div');
    answer.className = 'faq-answer';

    let j = i + 1;
    while (j < blockNodes.length && !['H2', 'H3'].includes(blockNodes[j].tagName)) {
      answer.appendChild(blockNodes[j].cloneNode(true));
      j += 1;
    }

    item.appendChild(answer);
    accordion.appendChild(item);

    i = j - 1;
  }

  if (!accordion.children.length) return;

  blockNodes.forEach((node) => node.remove());
  faqHeading.insertAdjacentElement('afterend', accordion);

  const items = Array.from(accordion.querySelectorAll('.faq-item'));
  if (items[0]) items[0].open = true;

  items.forEach((item) => {
    item.addEventListener('toggle', () => {
      if (!item.open) return;
      items.forEach((other) => {
        if (other !== item) other.open = false;
      });
    });
  });
})();
