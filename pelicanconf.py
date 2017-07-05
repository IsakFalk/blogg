#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Everything can be found in here http://docs.getpelican.com/en/stable/settings.html

###
### SITE METADATA
###

AUTHOR = 'Isak Falk'
SITENAME = 'Bayes #1 fan club'
# SITEURL = 'http://isakfalk.com'
# FEED_DOMAIN = SITEURL

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TIMEZONE = 'Europe/London'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'

DEFAULT_LANG = 'en'

###
### URL SETTINGS
###

# How to format output I think
# ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
# ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
# PAGE_URL = 'pages/{slug}/'
# PAGE_SAVE_AS = 'pages/{slug}/index.html'

###
### STYLING AND PLUGINS
###

# Plugins
PLUGIN_PATHS = ['/home/isak/website/pelican_ext/pelican-plugins']
PLUGINS = ['i18n_subsites']

# Typogrify
TYPOGRIFY = True

# Pygments options to be used for .rst files (http://docs.getpelican.com/en/stable/content.html#internal-pygments-options)
PYGMENTS_RST_OPTIONS = []

# Theme
THEME = "/home/isak/website/pelican_ext/pelican-themes/pelican-bootstrap3"

# Disqus
DISQUS_SITENAME = "isakfalk.com"

# Jinja env for bootstrap3
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Styling
BOOTSTRAP_THEME = 'simplex'

# Syntax highlighting
PYGMENTS_STYLE = 'native'

# Pages
DISPLAY_PAGES_ON_MENU = True

# No pagination (You are not clickbait)
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

###
### TECHNICAL STUFF
###

# Cache
LOAD_CONTENT_CACHE = False

# Keep .git files in output directory
OUTPUT_RETENTION = [".hg", ".git", ".bzr"]

# Ignore files
IGNORE_FILES = ['.#*', '__pycache__']

###
### PATHS SETTINGS
###

# Content path
PATH = 'content'
# Page pathss (relative to PATH)
PAGE_PATHS = ['pages']
# Article paths (relative to PATH)
ARTICLE_PATHS = ['']
# Static paths (relative to PATH)
STATIC_PATHS = ['static/images', 'extra/robots.txt', 'extra/favicon.ico']

# Output path
OUTPUT_PATH = 'output/'

# robots.txt/favicon
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

###
### LINKS SETTINGS
###

# Social links
SOCIAL = (('twitter', 'https://twitter.com/isakfalk_'),
          ('linkedin', 'http://www.linkedin.com/in/isakfalk'),
          ('github', 'http://github.com/isakfalk'),
          ('stackoverflow', 'https://stackoverflow.com/users/3617800/white-noise', 'stack-overflow'))

# Blogroll links
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('This site', 'http://isakfalk.com'))


