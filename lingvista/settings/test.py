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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'tmp:',
    }
}

SECRET_KEY = '@mo#3hjd#_x5bn0x0@43px-7(frjlebr2=$^bu*unzk4nd4z$4'

ALLOWED_HOSTS = []
