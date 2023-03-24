# frozen_string_literal: true

source 'https://rubygems.org'

gem 'jekyll', '~> 4.3'
group :jekyll_plugins do
  gem 'jektex'
  gem 'jekyll-archives'
  gem 'jekyll-gist'
  gem 'jekyll-paginate-v2'
  gem 'jekyll-pre-commit'
  gem 'jekyll-redirect-from'
  gem 'jekyll-relative-links'
  # Lock jekyll-sass-converter to 2.x on Linux-musl
  gem 'jekyll-seo-tag'
  gem 'jekyll-sitemap'
  gem 'jekyll-spaceship'
  gem 'jekyll-theme-chirpy'
  gem 'jekyll-twitch'
end

if RUBY_PLATFORM =~ /linux-musl/
  gem 'jekyll-sass-converter', '~> 2.0'
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem 'tzinfo', '>= 1', '< 3'
  gem 'tzinfo-data'
end

platforms :mingw, :x64_mingw, :mswin do
  gem 'wdm', '~> 0.1.1'
end

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem
# do not have a Java counterpart.
platform :jruby do
  gem 'http_parser.rb', '~> 0.6.0'
end
