#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tammy Cravit'
SITENAME = 'Tammy Makes Things'
SITETITLE = 'Tammy Makes Things'
SITESUBTITLE = 'hardware hacking, python, making stuff, etc.'

GITHUB_URL = 'https://github.com/tammymakesthings'
TWITTER_USERNAME = 'maker_tammy'
BROWSER_COLOR = '#330F54'
ROBOTS = 'index, follow'
COPYRIGHT_YEAR = 2016
PYGMENTS_STYLE = 'monokai'

MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
    ('Projects', '/projects/index.html'),
    ('Contact', '/contact/index.html'),
)

PATH = 'content'
OUTPUT_PATH = '..'
ARTICLE_PATHS = ['blog']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images',
                'pages/images',
                'pages/projects/images'
                'extra/CNAME',
                'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/custom.css': {'path': 'static/custom.css'},
}

DELETE_OUTPUT_DIRECTORY = False

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}.html'

THEME = '/home/tammy/pelican-themes/flex'
MAIN_MENU = True

IGNORE_FILES = ['.#*', '__pycache__']
TYPOGRIFY = True
WITH_FUTURE_DATES = False
DEFAULT_DATE = 'fs'
TIMEZONE = 'America/Phoenix'
DEFAULT_LANG = 'en'

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    'pelican-page-hierarchy',
    #    'pelican-gist',
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Blog', '/'),
    ('Projects', '/projects/'),
    ('Links', '/links/'),
    ('&nbsp;', '#'),
    ('About Me', '/about/'),
    ('Contact', '/contact/'),
)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/maker_tammy'),
    ('github', 'https://github.com/tammymakesthings'),
    ('keybase', 'https://keybase.io/tammymakesthings'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
