# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('lingvista.api.views',
    url(r'^translate/$', 'translate', name='api_translate'),
    url(r'^langs/$', 'langs', name='api_langs'),
)