# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('lingvista.transdef.views',
    url(r'^trainer/', 'trainer', name='trainer')
)