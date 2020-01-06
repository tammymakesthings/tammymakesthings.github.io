#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tammy Cravit'
SITENAME = 'Tammy Makes Things'
SITESUBTITLE = 'hardware hacking, python, making stuff, etc.'
SITEURL = 'https://tammymakesthings.com'
GITHUB_URL = 'https://github.com/tammymakesthings'
TWITTER_USERNAME = 'maker_tammy'

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
}

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}.html'

THEME = 'themes/blue-penguin'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
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
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
