# frozen_string_literal: true

source "https://rubygems.org"

# Jekyll and essential plugins
gem "jekyll", "~> 4.3.2"            # Jekyll core gem
gem "jekyll-feed", "~> 0.16"        # Plugin to generate Atom feeds
gem "jekyll-seo-tag", "~> 2.8"      # Plugin to enhance SEO with meta tags
gem "jekyll-sitemap", "~> 1.4"      # Plugin to generate a sitemap.xml
gem "jekyll-paginate", "~> 1.1"     # Plugin for pagination functionality

# Theme (add any desired theme)
gem "minimal-mistakes-jekyll", "~> 4.24" # Minimal Mistakes theme gem

# Plugins for development environment
group :jekyll_plugins do
  gem "webrick", "~> 1.7"           # Required for local server in Jekyll 4.x
end

# For Windows users (add if running on a Windows platform)
gem "wdm", "~> 0.1.1", platforms: [:mswin, :mingw, :x64_mingw] # File watcher for Windows
