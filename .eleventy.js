module.exports = function (eleventyConfig) {
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
