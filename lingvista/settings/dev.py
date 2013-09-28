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
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lingvista',
        'USER': 'lingvista',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)

SECRET_KEY = '@mo#3hjd#_x5bn0x0@43px-7(frjlebr2=$^bu*unzk4nd4z$4'

ALLOWED_HOSTS = []
