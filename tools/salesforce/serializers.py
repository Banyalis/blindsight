# -*- coding: utf-8 -*-

from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin
from tools.various.serializers import CustomModelSerializer, CustomBulkSerializer, CustomJSONField, CustomImageField
from drf_writable_nested import NestedCreateMixin, NestedUpdateMixin

from rest_framework import serializers
from . import models


class SalesforceAccessSerializer(CustomModelSerializer):

    # logout_url = serializers.SerializerMethodField()

    # def get_logout_url(self, instance):
    #     return instance.logout_url

    class Meta:
        fields = ('instance',)
        model = models.SalesforceAccess
