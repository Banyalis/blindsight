# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_bulk.routes import BulkRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import api

router = BulkRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
]

urlpatterns += format_suffix_patterns([
    url(r'^salesforce/access/', api.SalesforceAccess.as_view(), name='access'),
    url(r'^salesforce/logout/', api.SalesforceLogout.as_view(), name='logout'),
])

