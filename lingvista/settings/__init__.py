# -*- coding: utf-8 -*-
import os

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), os.pardir)

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = ''
MEDIA_URL = '/media/'
STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_ROOT + '/static/',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lingvista.urls'
WSGI_APPLICATION = 'lingvista.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_ROOT + '/templates/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'social.apps.django_app.default',
    # 'lingvista.account',
    'lingvista.api',
    'lingvista.transdef',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#AUTH_USER_MODEL = 'account.Account'

#PUBLIC TRANSLATION API ACCESS
MS_TRANSLATOR_CLIENT_ID = 'lingvista'
MS_TRANSLATOR_CLIENT_SECRET = 'tEa4ZYJt7NLl+09I3XeQQ4FnRrMlfNl64g1kdpC/3m8='

ACCOUNT_ACTIVATION_DAYS = 7

AUTHENTICATION_BACKENDS = (
      'social.backends.github.GithubOrganizationOAuth2',
      'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect'
)

# SOCIAL_AUTH_USER_MODEL = 'account.Account'

SOCIAL_AUTH_GITHUB_ORG_KEY = '3aaa2258dd5b31bede42'
SOCIAL_AUTH_GITHUB_ORG_SECRET = '6559b1bbd9e89ddcb836d6b19c717cf1536f6264'
SOCIAL_AUTH_GITHUB_ORG_NAME = 'Pyjamas'
