# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_bulk import BulkModelViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, AuthenticationFailed, ParseError

from . import models
from . import serializers

from tools.various.utils import oembed_parsed


class SalesforceAccess(generics.RetrieveAPIView):

    serializer_class = serializers.SalesforceAccessSerializer
    queryset = models.SalesforceAccess.objects.all()

    def get_object(self):
        access, created = models.SalesforceAccess.objects.get_or_create(id=1)
        return access


class SalesforceLogout(APIView):

    def get(self, request, *args, **kwargs):

        return Response(status=models.SalesforceAccess.logout())
