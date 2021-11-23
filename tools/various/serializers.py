# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.fields import SkipField
from rest_framework_bulk import BulkSerializerMixin, BulkListSerializer
from django.core.files import File
from django.core.files.base import ContentFile
import simplejson as json
import copy
import requests
import os
from django.db.models import Model

from django.conf import settings

from tools.various.fields import CustomListField
from tools.files.fields import CustomImgField, CustomFileField, CustomImgFieldS3, CustomFileFieldS3, get_aspect
from tools.files.models import TempFile
from tools.files.utils import get_image_dimension


class CustomJSONField(serializers.JSONField):

    def to_representation(self, obj):
        if isinstance(obj, basestring):
            return json.loads(obj)
        return obj

    def to_internal_value(self, data):
        if isinstance(data, basestring):
            return json.loads(data)
        return data


class CustomImageField(CustomJSONField):

    def __init__(self, **kwargs):
        self.resolutions = kwargs.pop('resolutions', None)
        self.duplicate_instance = kwargs.pop('duplicate_instance', None)
        kwargs.pop('max_length', None)
        super(CustomImageField, self).__init__(**kwargs)

    def to_representation(self, obj):

        res = {
            '%s_url' % (key,): getattr(obj, '%s_url' % (key,), None)
        for key in (self.resolutions or obj.field.my_resolutions.keys()) } if obj else None

        if res:

            w = getattr(obj.instance, '%s_width' % (self.field_name,), None)
            h = getattr(obj.instance, '%s_height' % (self.field_name,), None)

            if w and h:
                res.update({
                    'aspect': round(get_aspect(w, h), 4)
                })

        return res

    def to_internal_value(self, data):

        try:
            # if isinstance(data, basestring) and os.path.isfile(data):
            #     return super(CustomImageField, self).to_internal_value(
            #         ContentFile(open(data), name=os.path.basename(data)))

            if isinstance(data, File):
                return super(CustomImageField, self).to_internal_value(data)

            temp_img_id = None
            url = None

            if isinstance(data, dict):
                temp_img_id = data.get('temp_img_id', None)
                url = data.get('url', None)
            instance = self.parent.instance
            # if not isinstance(instance, Model):
            #     print self.context

            field = getattr(instance, self.field_name, None)

            if self.duplicate_instance:
                field = getattr(self.duplicate_instance, self.field_name, None)
                return super(CustomImageField, self).to_internal_value(File(open(field.file.name, 'rb'), name=field.original_name))

            if temp_img_id:
                temp_image = TempFile.objects.get(id=temp_img_id)
                return super(CustomImageField, self).to_internal_value(File(open(temp_image.file.path, 'rb'), name=temp_image.originalName))

            if url:
                request = requests.get(url, verify=False, stream=True)
                request.raise_for_status()
                return super(CustomImageField, self).to_internal_value(ContentFile(request.content, name=url))

            if field:
                return field

            else:
                raise SkipField
                #res = super(CustomImageField, self).to_internal_value(data)
                #return res

        except AttributeError:
            raise SkipField
            #return super(CustomImageField, self).to_internal_value(data)


class CustomFileFieldSerializer(serializers.FileField):

    def __init__(self, **kwargs):
        self.duplicate_instance = kwargs.pop('duplicate_instance', None)
        kwargs.pop('max_length')
        super(CustomFileFieldSerializer, self).__init__(**kwargs)

    def to_representation(self, obj):
        return obj.url() or None

    def to_internal_value(self, data):

        try:
            temp_file_id = None
            url = None

            if isinstance(data, File):
                return super(CustomFileFieldSerializer, self).to_internal_value(data)

            if isinstance(data, dict):
                temp_file_id = data.get('temp_file_id', None) if isinstance(data, dict) else None
                url = data.get('url', None) if isinstance(data, dict) else None
            field = getattr(self.parent.instance, self.field_name, None)

            if self.duplicate_instance:
                field = getattr(self.duplicate_instance, self.field_name, None)
                return super(CustomFileFieldSerializer, self).to_internal_value(File(open(field.file.name, 'rb'), name=field.original_name))

            if temp_file_id:
                temp_image = TempFile.objects.get(id=temp_file_id)
                return super(CustomFileFieldSerializer, self).to_internal_value(File(open(temp_image.file.path, 'rb'), name=temp_image.originalName))

            if url:
                request = requests.get(url, verify=False, stream=True)
                request.raise_for_status()
                return super(CustomFileFieldSerializer, self).to_internal_value(ContentFile(request.content, name=os.path.basename(url)))

            if field:
                return field

            else:
                return File(os.path.join(settings.MEDIA_ROOT, os.path.relpath(data, settings.MEDIA_URL) if data.startswith('http') else data )) if data else None

        except AttributeError:
            return super(CustomFileFieldSerializer, self).to_internal_value(data)


class CustomDurationField(serializers.DurationField):

    def to_representation(self, obj):
        res = super(CustomDurationField, self).to_representation(obj)
        res = u':'.join([part for i, part in enumerate(res.split(u':')) if int(part) or i])
        return res


class CustomBulkSerializer(BulkListSerializer):
    serializer_field_mapping = copy.deepcopy(serializers.ModelSerializer.serializer_field_mapping)
    serializer_field_mapping[CustomListField] = CustomJSONField
    serializer_field_mapping[CustomImgField] = CustomImageField
    serializer_field_mapping[CustomFileField] = CustomFileFieldSerializer
    serializer_field_mapping[CustomImgFieldS3] = CustomImageField
    serializer_field_mapping[CustomFileFieldS3] = CustomFileFieldSerializer


class CustomModelSerializer(serializers.ModelSerializer):

    serializer_field_mapping = copy.deepcopy(serializers.ModelSerializer.serializer_field_mapping)
    serializer_field_mapping[CustomListField] = CustomJSONField
    serializer_field_mapping[CustomImgField] = CustomImageField
    serializer_field_mapping[CustomFileField] = CustomFileFieldSerializer
    serializer_field_mapping[CustomImgFieldS3] = CustomImageField
    serializer_field_mapping[CustomFileFieldS3] = CustomFileFieldSerializer

    def __init__(self, *args, **kwargs):
        self.duplicate_instance = kwargs.pop('duplicate_instance', None)
        super(CustomModelSerializer, self).__init__(*args, **kwargs)

    def build_field(self, field_name, info, model_class, nested_depth):
        field_class, field_kwargs = super(CustomModelSerializer, self).build_field(field_name, info, model_class, nested_depth)

        if field_class is CustomImageField or \
            field_class is CustomFileFieldSerializer or \
            field_class is CustomModelSerializer:

            field_kwargs.update({
                'duplicate_instance': self.duplicate_instance
            })

        return field_class, field_kwargs

    def _update_fk_items(self, instance, items, rel_field_name, field_name, serializer_class, model_class=None):
        if items is not None:
            items_mapping = {item.id: item for item in getattr(instance, rel_field_name).all()}
            items_data = filter(None, [item.get('id', None) for item in items])

            for item in items:
                _item = items_mapping.get(item.get('id', None), None)
                i = dict(item)
                if _item is None:
                    r = serializer_class(data=i)
                    if r.is_valid():
                        _item = r.save(**{field_name: instance})
                        items_data.append(_item.id)
                else:
                    r = serializer_class(_item, i)
                    if r.is_valid():
                        r.save()

            (model_class or serializer_class.Meta.model).objects.filter(id__in=set(items_mapping.keys()) - set(items_data)).delete()
