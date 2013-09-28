# -*- coding: utf-8 -*-
from lingvista.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'lingvista',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'lingvista',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)

SECRET_KEY = '@mo#3hjd#_x5bn0x0@43px-7(frjlebr2=$^bu*unzk4nd4z$4'

ALLOWED_HOSTS = []
