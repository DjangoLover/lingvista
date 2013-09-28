# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/v1/', include('lingvista.api.urls')),
    url(r'^$', 'lingvista.views.index', name='lingvista-index'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
