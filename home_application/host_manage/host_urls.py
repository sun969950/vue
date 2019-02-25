# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'home_application.host_manage.host_views',
    (r'^search_host_config', 'search_host_config'),
    (r'^search_biz$', 'search_biz'),
    (r'^search_host_list$', 'search_host_list'),
    (r'^create_host$', 'create_host'),
    (r'^modify_host$', 'modify_host'),
    (r'^delete_host$', 'delete_host'),
    (r'^search_loadavg$', 'search_loadavg'),

)
