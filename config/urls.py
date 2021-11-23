"""starter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from decorator_include import decorator_include
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve

from front.views import Custom404View
from tools.various.decorators import login_required_flat, login_required_flat_api
from tools.various.views import user_login_api

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('front.urls', app_name='front', namespace='front')),
]

urlpatterns += [
    url(r'^control/', include('tools.various.public_urls', namespace='tools_public')),
    # url(r'^control/sf/', include('tools.salesforce.urls', app_name='salesforce', namespace='salesforce')),
    # url(r'^control/api/', decorator_include(login_required_flat, 'tools.files.urls', namespace='control_files')),
    # url(r'^control/', decorator_include(login_required_flat, 'tools.various.urls', namespace='tools')),
    # url(r'^control/api/', decorator_include(login_required_flat, 'tools.salesforce.api_urls', namespace='salesforce_api')),
]

handler404 = Custom404View.as_view()
handler500 = 'front.views_utils.custom_500'

urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})]
urlpatterns += [url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': True})]

if settings.DEBUG:

    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
