# PYHDL Documentation

This is the Jekyll documentation site for PYHDL.

## Running Locally

### Prerequisites

- Ruby 2.5 or higher
- Bundler gem

### Setup

```bash
# Install dependencies
bundle install

# Run Jekyll server
bundle exec jekyll serve

# Open in browser
open http://localhost:4000
```

### Build for Production

```bash
bundle exec jekyll build
```

Output will be in `_site/` directory.

## Directory Structure

```
docs/
├── _config.yml          # Jekyll configuration
├── _layouts/            # Page layouts
│   └── default.html     # Main layout
├── _includes/           # Reusable components
│   ├── footer.html
│   └── social.html
├── assets/              # Static assets
│   └── css/
│       └── style.css
├── index.md             # Homepage
├── getting-started.md   # Getting started guide
├── usage.md             # Usage guide
└── api-reference.md     # API reference
```

## Adding New Pages

1. Create a new `.md` file in the root of `docs/`
2. Add front matter:

```yaml
---
layout: default
title: Your Page Title
---
```

3. Add content using Markdown
4. Add navigation link in `_layouts/default.html`

## Deployment

### GitHub Pages

This site is configured to work with GitHub Pages:

1. Push to `gh-pages` branch
2. Enable GitHub Pages in repository settings
3. Site will be live at `https://[username].github.io/pyhdl`

### Other Hosting

```bash
# Build the site
bundle exec jekyll build

# Upload _site/ directory to your web server
```

## Customization

### Changing Theme

Edit `_config.yml`:
```yaml
theme: your-theme
```

### Adding New Navigation Links

Edit `_layouts/default.html` and add menu items in the `site-nav` section.

### Modifying Styles

Edit `assets/css/style.css` or override theme CSS.

## Contributing

When adding new documentation:

1. Use clear, concise Markdown
2. Include code examples
3. Add to navigation if appropriate
4. Test locally before committing

