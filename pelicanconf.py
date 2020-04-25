#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# General Settings
AUTHOR = 's.hosoya'
SITENAME = "Days of migratory birds" 
SITEURL = 'http://localhost:8000' # for localhost test
PATH = 'content'
TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'ja'
RELATIVE_URLS = True
DEFAULT_PAGINATION = 3

# TIMEZONE
TIMEZONE = 'Asia/Tokyo'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'ja': '%Y-%m-%d(%a)',
}

# Site setting
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_PAGES_ON_MENU = True

# Site PATH setting
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/')
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/syoutin'),
          ('github','https://github.com/mollinaca'))

# Plugins
PLUGIN_PATHS = ['../pelican-plugins/']
PLUGINS = ['tag_cloud']

## add recent page
## http://www.voidynullness.net/blog/2015/06/25/add-recent-posts-list-to-pelican-blog/
#TEMPLATE_PAGES = {'recent.json': 'api/recent.json', }

# Theme
# https://github.com/getpelican/pelican-themes/tree/master/new-bootstrap2
THEME = "themes/new-bootstrap2"
