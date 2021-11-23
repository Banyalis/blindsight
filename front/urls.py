# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.conf import settings
from . import views
from . import views_utils

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^memories/$', views.MemoriesView.as_view(), name='memories'),
    url(r'^memories/memory-(?P<slug>\w+(?:-+\w+)*)/$', views.MemoriesPopup.as_view(), name='memories-popup'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^404/$', views.Custom404View.as_view(), name='custom_404'),
    url(r'^api/', include('front.api_urls', app_name='api', namespace='api')),
]

if settings.DEBUG:
    urlpatterns += [
        # url(r'^404/$', views_utils.Custom404View.as_view()),
        url(r'^500/$', views_utils.demo_500),
    ]
