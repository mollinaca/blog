#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 's.hosoya'
SITENAME = '渡りの日々.'
SITEURL = 'http://localhost:8000'
PATH = 'content'
TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
SOCIAL = (('twitter', 'https://twitter.com/syoutin'),
          ('github','https://github.com/mollinaca'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Additional
#::python
TIMEZONE = 'Asia/Tokyo'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'ja': '%Y-%m-%d(%a)',
}

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
USE_FOLDER_AS_CATEGORY = True

# Theme
THEME = "../pelican-themes/bootstrap2-dark"
