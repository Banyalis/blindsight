# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from . import api as views
from . import views_utils

router = DefaultRouter()
# router.register(r'memories/list', common.NewsViewSet, basename='memories')

urlpatterns = [
    url(r'^', include(router.urls)),
]

urlpatterns += [
    url(r'^index/$', views.Index.as_view(), name='index'),
    url(r'^memories/$', views.Memories.as_view(), name='memories'),
    url(r'^about/$', views.About.as_view(), name='about'),
    url(r'^memories/memory-(?P<slug>\w+(?:-+\w+)*)/$', views.MemoriesPopup.as_view(), name='memories-popup'),
    url(r'^', include('tools.files.urls', app_name='files', namespace='files')),
]