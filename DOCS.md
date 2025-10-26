# Documentation Setup

This project now includes a complete Jekyll documentation site in the `docs/` directory.

## Quick Start

### Running Locally

1. **Install Ruby and Bundler** (if not installed):
   ```bash
   # On Ubuntu/Debian
   sudo apt-get install ruby-full
   
   # On macOS
   brew install ruby
   
   # On Windows (with WSL)
   # Ruby usually comes with WSL
   ```

2. **Install dependencies**:
   ```bash
   cd docs
   bundle install
   ```

3. **Run Jekyll server**:
   ```bash
   bundle exec jekyll serve
   ```

4. **View documentation**:
   Open http://localhost:4000 in your browser

### Building the Site

To build static files:

```bash
cd docs
bundle exec jekyll build
```

Output will be in `docs/_site/` directory.

## Documentation Structure

The docs directory contains:

- **`index.md`** - Homepage with overview
- **`getting-started.md`** - Installation and quick start guide
- **`usage.md`** - Detailed usage examples and patterns
- **`api-reference.md`** - Complete language reference
- **`_config.yml`** - Jekyll configuration
- **`_layouts/`** - Page templates
- **`_includes/`** - Reusable components
- **`assets/`** - CSS and static files

## Adding Documentation

### Adding a New Page

1. Create a new `.md` file in the `docs/` directory:

```markdown
---
layout: default
title: Page Title
---

Your content here...
```

2. Add to navigation in `docs/_layouts/default.html`:

```html
<a class="page-link" href="{{ '/your-page' | relative_url }}">Your Page</a>
```

### Editing Existing Pages

Simply edit the `.md` files in the `docs/` directory. Changes will be reflected when you restart Jekyll.

## Customization

### Changing the Theme

Edit `docs/_config.yml`:

```yaml
theme: minima  # Change to your preferred theme
```

### Modifying Styles

Edit `docs/assets/css/style.css` to customize the look and feel.

### Updating Navigation

Edit the `site-nav` section in `docs/_layouts/default.html`.

## Deployment

### GitHub Pages (Automatic)

The site is configured for automatic deployment via GitHub Actions:

1. Push to the `main` branch
2. The `.github/workflows/jekyll-deploy.yml` workflow will build and deploy
3. Documentation will be available at `https://[username].github.io/pyhdl`

### Manual Deployment

1. Build the site:
   ```bash
   bundle exec jekyll build
   ```

2. Deploy the `_site` directory to your web server

3. Or push to GitHub Pages branch:
   ```bash
   git subtree push --prefix docs/_site origin gh-pages
   ```

## Troubleshooting

### Ruby/Jekyll Not Found

Install Ruby:
```bash
# Ubuntu/Debian
sudo apt-get install ruby-full

# Then install bundler
gem install bundler
```

### Bundle Install Errors

Make sure you're in the `docs/` directory:
```bash
cd docs
bundle install
```

### Port Already in Use

If port 4000 is busy:
```bash
bundle exec jekyll serve --port 4001
```

## Documentation Content

### Current Pages

1. **Homepage** (`index.md`)
   - Project overview
   - Quick start
   - Features and benefits

2. **Getting Started** (`getting-started.md`)
   - Installation instructions
   - Basic syntax
   - First conversion example

3. **Usage Guide** (`usage.md`)
   - Command-line interface
   - Complete examples
   - Best practices

4. **API Reference** (`api-reference.md`)
   - Complete language reference
   - Supported features
   - Operators and types

## Next Steps

- Add more examples
- Include screenshots/diagrams
- Add a changelog
- Create a developer guide
- Add API documentation

For more information, see `docs/README.md`.

