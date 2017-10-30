#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Everything can be found in here http://docs.getpelican.com/en/stable/settings.html

###
### SITE METADATA
###

AUTHOR = 'Isak Falk'
SITENAME = 'isakfalk'
SITEURL = 'https://isakfalk.com'
FEED_DOMAIN = SITEURL

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = ''
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = ''
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_RSS = ''

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
           'assets',
           'sitemap',
           'org_reader',
           'render_math']

# Org reader (https://github.com/getpelican/pelican-plugins/tree/master/org_reader)
ORG_READER_EMACS_LOCATION = '/usr/bin/emacs24'
#ORG_READER_EMACS_SETTINGS
#ORG_READER_BACKEND

# Render math

# Disqus
DISQUS_SITENAME = "isakfalk"

# Google analytics
GOOGLE_ANALYTICS_ID = "UA-106408402-1"
GOOGLE_ANALYTICS_PROP = ""

# Configuration for the "sitemap" plugin
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'always',
        'indexes': 'hourly',
        'pages': 'monthly'
    }
}

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

# Global keywords should be all lowercase as it is part of the HTML
GLOBAL_KEYWORDS = ['ai',
                   'ml',
                   'cs',
                   'statistics',
                   'mathematics',
                   'computers',
                   'programming',
                   'python',
                   'deep learning']

# Blogroll (Top left of site)
LINKS = (('index', SITEURL + '/index.html'),
         ('about', SITEURL + '/pages/about.html'),
         ('CV', SITEURL + '/static/files/cv.pdf'))

# Social widget (Top right of site)
SOCIAL = (('email', 'mailto:me@isakfalk.com'),
          ('github', 'https://github.com/IsakFalk'),
          ('stackoverflow', 'https://stackoverflow.com/users/3617800/white-noise'),
          ('twitter', 'https://twitter.com/isakfalk_'),
          ('feed', FEED_DOMAIN + '/' + FEED_ALL_ATOM))

# URL's for pages
ARCHIVES_URL = 'archives.html'
# TAGS_URL = '/tags.html'
CATEGORIES_URL = 'categories.html'

# Hide email from spambots
MANGLE_EMAILS = True

###
### THEME SPECIFIC END
###

# Disqus
DISQUS_SITENAME = "isakfalk"

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
