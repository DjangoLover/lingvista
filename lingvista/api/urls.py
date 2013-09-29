# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from lingvista.api.views import AccountSettingsView

urlpatterns = patterns('lingvista.api.views',
    url(r'^transdef/$', 'transdef', name='api_translate'),
    url(r'^langs/$', 'langs', name='api_langs'),
    url(r'^account/', AccountSettingsView.as_view()),
)