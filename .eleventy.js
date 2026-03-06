module.exports = function (eleventyConfig) {
  const buildDate = new Date();
  const iso = buildDate.toISOString();
  const display = `${iso.slice(0, 10)} ${iso.slice(11, 16)} UTC`;

  eleventyConfig.addGlobalData("build", {
    iso,
    display,
  });

  eleventyConfig.addShortcode("ms", (name, options = {}) => {
    const iconName = (name || "").toString().trim();
    if (!iconName.length) return "";

    const opts = options && typeof options === "object" ? options : {};
    const className = (opts.class || "material-symbols-rounded").toString().trim();
    const label = (opts.label || "").toString().trim();
    const filled = Boolean(opts.filled);
    const weight = Number.isFinite(Number(opts.weight)) ? Number(opts.weight) : null;

    const styleVars = [];
    if (filled) styleVars.push("--ms-fill: 1");
    if (weight) styleVars.push(`--ms-wght: ${weight}`);
    const styleAttr = styleVars.length ? ` style="${styleVars.join("; ")}"` : "";

    if (label.length) {
      return `<span class="${className}" role="img" aria-label="${label.replace(/\"/g, "&quot;")}"${styleAttr}>${iconName}</span>`;
    }

    return `<span class="${className}" aria-hidden="true"${styleAttr}>${iconName}</span>`;
  });

  eleventyConfig.addPassthroughCopy({
    "src/images": "images",
    "src/js": "js"
  });

  // Draft support:
  // - `draft: true` => do not write output + exclude from collections.
  eleventyConfig.addGlobalData("eleventyComputed", {
    permalink: (data) => (data.draft ? false : data.permalink),
    eleventyExcludeFromCollections: (data) =>
      data.draft ? true : data.eleventyExcludeFromCollections,
  });

  eleventyConfig.addFilter("readableDate", (dateObj, locale = "en") => {
    if (!dateObj) return "";
    try {
      return new Intl.DateTimeFormat(locale, {
        year: "numeric",
        month: "long",
        day: "2-digit",
      }).format(dateObj);
    } catch {
      return String(dateObj);
    }
  });

  eleventyConfig.addFilter("json", (value) => JSON.stringify(value));

  eleventyConfig.addCollection("posts", (collectionApi) => {
    return collectionApi
      .getFilteredByTag("post")
      .slice()
      .sort((a, b) => b.date - a.date);
  });

  return {
    dir: {
      input: "src",
      includes: "_includes",
      output: "_site"
    }
  };
};
