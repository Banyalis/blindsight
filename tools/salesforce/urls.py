# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^authorize/$', views.AuthorizeView.as_view(), name='authorize'),
    url(r'^authorized/$', views.AuthorizedView.as_view(), name='authorized'),
    url(r'^test/$', views.TestView.as_view(), name='test'),
]
