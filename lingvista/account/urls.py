# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^settings/$', 'lingvista.account.views.settings', name='settings'),
    url(r'^delivery_settings/$', 'lingvista.account.views.delivery_settings', name='delivery-settings'),
)