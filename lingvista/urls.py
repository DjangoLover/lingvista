# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'lingvista.views.index', name='lingvista-index'),
    url(r'^logout/$', 'lingvista.views.logout_user', name='lingvista-logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^api/v1/', include('lingvista.api.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^transdef/', include('lingvista.transdef.urls')),
    
    url(r'^account/$', include('lingvista.account.urls', namespace='account')),
)
