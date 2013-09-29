# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('lingvista.account.views',
    url(r'^settings/$', 'settings', name='settings'),
    url(r'^delivery_settings/$', 'delivery_settings', name='delivery-settings'),
)