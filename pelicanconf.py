#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Everything can be found in here http://docs.getpelican.com/en/stable/settings.html

###
### SITE METADATA
###

AUTHOR = 'Isak Falk'
SITENAME = 'isakfalk'
SITEURL = 'http://localhost:8000'
FEED_DOMAIN = SITEURL

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None

# Date settings
TIMEZONE = 'Europe/London'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'

DEFAULT_LANG = 'en'

###
### URL SETTINGS
###

###
### STYLING AND THEME
###

# Plugins
PLUGIN_PATHS = ['/home/isak/website/pelican_ext/pelican-plugins']
PLUGINS = ['i18n_subsites',
           'liquid_tags.img',
           'liquid_tags.video',
           'liquid_tags.youtube',
           'liquid_tags.vimeo',
           'liquid_tags.include_code',
           'liquid_tags.notebook',
           'assets']

# Typogrify
TYPOGRIFY = True

# Theme
theme_path = "/home/isak/website/pelican_ext/pelican-themes/"
theme = "personal-theme"
THEME = theme_path + theme

###
### THEME SPECIFIC
###
USER_LOGO_URL = "/static/images/profile.jpg"
FUZZY_DATES = False

SITETITLE = 'What the Bayes?!'
SITESUBTITLE = 'Highly biased opinions on ML, programming and more'

GLOBAL_KEYWORDS = ['Hello', 'Hi', 'How are you']

# Blogroll (Top left of site)
LINKS = (('index', SITEURL + '/index.html'),
         ('about', SITEURL + '/pages/about.html'),
         ('CV', SITEURL + '/static/cv.pdf'))

# Social widget (Top right of site)
SOCIAL = (('email', 'mailto:isak.falk@live.se'),
          ('github', 'https://github.com/IsakFalk'),
          ('stackoverflow', 'https://stackoverflow.com/users/3617800/white-noise'),
          ('twitter', 'https://twitter.com/isakfalk_'))

# URL's for pages
ARCHIVES_URL = 'archives.html'
# TAGS_URL = '/tags.html'
CATEGORIES_URL = 'categories.html'

###
### THEME SPECIFIC END
###

# Disqus
DISQUS_SITENAME = "isakfalk"

# Google analytics
GOOGLE_ANALYTICS_ID = "UA-106408402-1"
GOOGLE_ANALYTICS_PROP = ""
# Jinja env for bootstrap3
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Syntax highlighting
PYGMENTS_STYLE = 'friendly'

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
# ARTICLE_PATHS = ['']
# Static paths (relative to PATH)
STATIC_PATHS = [
    'static/images',
    'static/files',
    'extra/robots.txt',
    'extra/favicon.ico'
]
# Extra data
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
# Code directory for liquid tags
CODE_DIR = 'static/code'
# Notebook directory for liquid tags
NOTEBOOK_DIR = 'static/notebooks'
