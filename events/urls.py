# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from events.views import *

urlpatterns = patterns('',
    url(r'^(?P<event_id>\d+)/tab/(?P<tab_id>\d+)', tabs, name = 'tab-list'),
    url(r'^(?P<event_id>\d+)', events, name = 'event-list'),
    url(r'^$', direct_to_template, {'template':'events/events_home.html',}, name = 'event-home'),
)