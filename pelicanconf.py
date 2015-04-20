#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Neal Gordon'
SITENAME = 'navigating the noosphere'
#SITESUBTITLE = 'fun with engineering and technology'
SITEURL = 'http://nagordon.github.io'
HIDE_SITENAME = False

################# DEVELOPMENT SETTINGS ###########################
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# when changing settings set this to false
LOAD_CONTENT_CACHE = False

################# Pelican SETTINGS ###########################
DISPLAY_PAGES_ON_MENU = True
TAG_CLOUD_STEPS = 6
TAG_CLOUD_MAX_ITEMS = 15
DISPLAY_ARTICLE_INFO_ON_INDEX = True
PATH = 'content'
STATIC_PATHS = ['images', 'code', 'notebooks']
NOTEBOOK_DIR = 'notebooks'
#ARTICLE_PATHS = ['content']

THEME = "themes/pelican-bootstrap3" 
#THEME = 'notmyidea'

# ipynb settings
MARKUP = ('md')#, 'ipynb')
PLUGIN_PATHS = ['plugins']
PLUGINS = ['liquid_tags.img', 
           'liquid_tags.youtube', 
           'liquid_tags.include_code', 
	   'liquid_tags.notebook']#		'ipynb', 'render_math']

SUMMARY_MAX_LENGTH = 100
USE_FOLDER_AS_CATEGORY = False

################# BOOTSTRAP SETTINGS ###########################
BANNER = 'images/banner.jpg'
#BANNER_SUBTITLE = 'This is my subtitle'
#BOOTSTRAP_THEME = 'simplex'
SHOW_ARTICLE_AUTHOR = True
SHOW_DATE_MODIFIED = True
BOOTSTRAP_FLUID = True
BANNER_ALL_PAGES = False
SITELOGO = '/images/logo.jpg'
SITELOGO_SIZE = 50
DEFAULT_PAGINATION = False   #10
DISPLAY_BREADCRUMBS = False
HIDE_SIDEBAR  = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
#FAVICON = '/images/logo.jpg'
DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 3

AVATAR = 'images/me.png'
ABOUT_ME = 'Here I am!'

#GITHUB_URL = 'https://github.com/nagordon'
GITHUB_USER = 'nagordon'

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

EMAIL = 'nealagordon@gmail.com'

TIMEZONE = 'America/New_York'
DATE_FORMATS = {'en': '%Y-%m-%d'}
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/profile/public-profile-settings?trk=prof-edit-edit-public_profile'),
          ('GitHub', 'https://github.com/nagordon'),
		  ('Reddit','http://www.reddit.com/user/nagordon'),
		  ('Instructables','http://www.instructables.com/member/nagordon'),
		  ('StackOverflow','http://stackoverflow.com/users/2438993/nagordon'),)
