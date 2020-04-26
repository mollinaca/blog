#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
from unidecode import unidecode

# General Settings
AUTHOR = 's.hosoya'
SITENAME = "Days of migratory birds" 
SITEURL = 'https://blog.watarinohibi.tokyo' # for Production
PATH = 'content'
ROBOTS = 'index, follow'
COPYRIGHT_YEAR = datetime.now().year
RELATIVE_URLS = True
DEFAULT_PAGINATION = 3
LOAD_CONTENT_CACHE = False
SITELOGO = 'https://blog.watarinohibi.tokyo/images/static/profile.png'
#FAVICON = 'https://blog.watarinohibi.tokyo/images/static/favicon.ico'

# TZ & Locale
TIMEZONE = 'Asia/Tokyo'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'ja': '%Y-%m-%d(%a)',
}
DEFAULT_LANG = 'ja'

# Site setting
MAIN_MENU = True
MENUITEMS = (
  ('Archives', '/archives.html'),
  ('Categories', '/categories.html'),
  ('Tags', '/tags.html'),
)
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_PAGES_ON_MENU = True
CC_LICENSE = {
  'name': 'Creative Commons Attribution-ShareAlike',
  'version': '4.0',
  'slug': 'by-sa',
}

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
PLUGIN_PATHS = ['plugins/', 'plugins-custom/']
PLUGINS = ['tag_cloud',
           'sitemap',
           'related_posts',
           'better_codeblock_line_numbering',
           'tipue_search',]
SITEMAP = {
    'format': 'xml'
}
RELATED_POSTS_MAX = 5
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']

# Tag Substitutions
SLUG_REGEX_SUBSTITUTIONS = (
    (unidecode('タグテスト'), 'tag_test'),
    (unidecode('雑記'), 'diary'),
    (unidecode('ニュース'), 'news'),
    (unidecode('時事'), 'current_news'),
    (unidecode('政治'), 'politics'),
    (unidecode('思考実験'), 'te'),
    (unidecode('ゲーム'), 'game'),
    (unidecode('プログラミング'), 'p'),
    (unidecode('競技プログラミング'), 'cp')
    )

# Theme
# https://github.com/alexandrevicenzi/Flex
THEME = "themes/Flex"
PYGMENTS_STYLE = 'monokai'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
USE_LESS = True
