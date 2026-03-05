# Copilot Instructions for Eleventy Marketing Site

## Project Overview
This is an **Eleventy (11ty)** static site generator for Easy Tech Partners, a HubSpot agencies services company. The site promotes four service lines: HubSpot, Integrations, E-commerce, and Data Insights.

**Key workflows:**
- `npm run dev` – Starts Eleventy watch server (auto-reloads on changes)
- `npm run build` – Builds static output to `_site/` directory

## Architecture & Component Structure

### Directory Layout
```
src/                    # Source files (input root)
  *.md                  # Content pages (index, about-us, contact-us, services/*.md)
  images/               # Static assets (passed through to _site/images)
  _includes/
    base.njk            # Master layout template (contains full HTML structure with nav, styling)
.eleventy.js            # Configuration: defines input/output dirs, passthrough copy rules
_site/                  # Generated static output (git-ignored, regenerated on build)
```

### Page Structure
Each markdown file uses front matter to declare its layout and title:
```yaml
---
layout: base
title: Page Title Here
---
```
The `layout: base` references `base.njk` which wraps markdown content in the full page structure.

## Key Patterns & Conventions

### Styling Location
**All CSS is inline in `base.njk` inside `<style>` tags** (lines ~10-250). There are no external CSS files. CSS variables define the design system:
- Colors: `--accent` (blue), `--text-main`, `--bg`, etc.
- Layout: `--layout-width: 980px` controls max-width
- Spacing/Radius: Consistent use of px values (20px, 24px, 18px, 12px, 16px)

When modifying styles, edit the CSS variables and classes directly in `base.njk`.

### Adding New Pages
1. Create a `.md` file in `src/` with front matter specifying `layout: base` and `title`
2. Markdown content becomes the page body inside base layout
3. For service pages → create in `src/services/` folder (builds to `_site/services/page-name/`)

### Navigation Update
The nav structure is hardcoded in `base.njk`. If adding pages, update the `.nav-list` in `base.njk` to include links.

## External Dependencies
- **@11ty/eleventy** (^3.1.2) – Static site generator
- **Nunjucks templating** – Built-in to Eleventy for `.njk` files
- **No npm packages for styling/scripts** – Everything is vanilla HTML/CSS/JS

## Build & Output
- Input: `src/` (configured in `.eleventy.js`)
- Output: `_site/` (auto-generated, do not edit directly)
- Images: `src/images/` → `_site/images/` (passthrough copy via `addPassthroughCopy`)
- All pages automate to HTML in output folder structure matching source paths

## Common Tasks

**Add a new service:** Create `src/services/service-name.md` → builds to `_site/services/service-name/index.html`

**Update nav links:** Edit `.nav-list` in `base.njk`

**Change colors/spacing:** Modify CSS variables (`:root` block) in `base.njk`

**Fix broken links:** Check that page titles/filenames match link hrefs in nav and content
