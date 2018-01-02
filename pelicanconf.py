#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Prashant Tiwari'
SITENAME = 'Blogs and thoughts.'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

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
        )

# Social widget
SOCIAL = (
             ('GitHub', 'https://github.com/pt247'),
             ('LinkedIn', 'https://www.linkedin.com/in/prashanttiwari247/'),
             ('Twitter', 'https://twitter.com/tintin5us'),
             ('Gmail: prashanttiwari247@gmail.com', 'mailto:prashanttiwari247@gmail.com'),
             ('Skype: prashanttiwari247', '#'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGINS = ['encrypt_content']

ENCRYPT_CONTENT = {
    'title_prefix': '[Encrypted]',
    'summary': 'This content is encrypted.'
}

DEFAULT_DATE = 'fs'
STATIC_PATHS = ['images', 'pdfs']
# ARTICAL_PATHS = ['pages']
# PAGE_PATHS = ['pages']
DISPLAY_PAGES_ON_MENU = False
