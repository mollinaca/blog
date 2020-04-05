#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 's.hosoya'
SITENAME = '渡りの日々.'
SITEURL = 'http://localhost:8000'
PATH = 'content'
TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'en'
RELATIVE_URLS = True

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
SOCIAL = (('twitter', 'https://twitter.com/syoutin'),
          ('github','https://github.com/mollinaca'))

DEFAULT_PAGINATION = 1

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
THEME = "../pelican-themes/foundation-default-colours"

# theme conf
FOUNDATION_FRONT_PAGE_FULL_ARTICLES = True
FOUNDATION_ALTERNATE_FONTS = True
FOUNDATION_TAGS_IN_MOBILE_SIDEBAR = True
#FOUNDATION_NEW_ANALYTICS = False
#FOUNDATION_ANALYTICS_DOMAIN = ''
FOUNDATION_FOOTER_TEXT = 'Powered by <a href="http://getpelican.com">Pelican</a> and <a href="http://foundation.zurb.com/">Zurb Foundation</a>. Theme by <a href="http://hamaluik.com">Kenton Hamaluik</a>.'
FOUNDATION_PYGMENT_THEME = 'monokai'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
