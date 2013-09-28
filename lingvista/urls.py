# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^api/v1/', include('lingvista.api.urls')),

    url(r'^$', 'lingvista.views.index', name='lingvista-index'),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
