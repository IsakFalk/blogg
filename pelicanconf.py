#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Everything can be found in here http://docs.getpelican.com/en/stable/settings.html

###
### SITE METADATA
###

AUTHOR = 'Isak Falk'
SITENAME = 'Bayes #1 fan club'
SITEURL = 'http://isakfalk.com'
#FEED_DOMAIN = SITEURL

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
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

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
           'liquid_tags.notebook']
# Typogrify
TYPOGRIFY = True

# Pygments options to be used for .rst files (http://docs.getpelican.com/en/stable/content.html#internal-pygments-options)
PYGMENTS_RST_OPTIONS = []

# Theme
THEME = "/home/isak/website/pelican_ext/pelican-themes/pelican-bootstrap3"

#
# THEME SPECIFIC VARIABLES
#

# Styling
BOOTSTRAP_THEME = 'cosmo'
SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = False
USE_PAGER = True
BOOTSTRAP_FLUID = False
SITELOGO = ''
SITELOGO_SIZE = 30
HIDE_SITENAME = False
DISPLAY_BREADCRUMBS = False
DISPLAY_CATEGORY_IN_BREADCRUMBS = False
FAVICON = 'extra/images/favicon.ico'
#BOOTSTRAP_NAVBAR_INVERSE = False
ABOUT_ME = 'Hey there, I\'m Isak,  welcome to my blog! Here I talk about things I find interesting such as machine learning, programming and statistics.'
AVATAR = 'static/images/profile.jpg'
# SITESUBTITLE = 'yeah, man'
# SITETAG = 'this is a sitetag'
BANNER = 'static/images/banner.png'
BANNER_SUBTITLE = 'Machine Learning, Programming and Statistics'
HIDE_SIDEBAR = False
SIDEBAR_ON_LEFT = True
DISABLE_SIDEBAR_TITLE_ICONS = True
# Path to custom .css file
#CUSTOM_CSS = 'static/custom.css'

#
# END
#

# Disqus
DISQUS_SITENAME = "isakfalk"

# Jinja env for bootstrap3
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Syntax highlighting
PYGMENTS_STYLE = 'friendly'

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
STATIC_PATHS = ['static/images', 'static/code', 'extra/robots.txt', 'extra/favicon.ico']
# Code directory for liquid tags
CODE_DIR = 'static/code'
# Notebook directory for liquid tags
NOTEBOOK_DIR = 'static/notebooks'

# Output path
OUTPUT_PATH = 'output'

# # robots.txt/favicon
# EXTRA_PATH_METADATA = {
#     'extra/robots.txt': {'path': 'robots.txt'},
#     'extra/favicon.ico': {'path': 'favicon.ico'}
# }

###
### LINKS SETTINGS
###

# Social links
SOCIAL = (('twitter', 'https://twitter.com/isakfalk_'),
          ('linkedin', 'http://www.linkedin.com/in/isak-falk/'),
          ('github', 'http://github.com/isakfalk'),
          ('stackoverflow', 'https://stackoverflow.com/users/3617800/white-noise', 'stack-overflow'))

# Blogroll links
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('This site', 'http://isakfalk.com'))
