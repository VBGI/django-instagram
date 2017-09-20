# -*- coding: utf-8 -*-

from django.conf.urls import *
from .views import get_instagram_data

urlpatterns = patterns('',
    url(r'^([a-zA-Z0-9_]+)', get_instagram_data, name='instagram-app-loader')
    )