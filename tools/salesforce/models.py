# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils import timezone
from tools.various.db import Base
from tools.various.fields import CustomListField
import requests
import json

from .tasks import send


class SalesforceAccess(models.Model):
    access_token = models.CharField(max_length=255, null=True, blank=True)
    refresh_token = models.CharField(max_length=255, null=True, blank=True)
    instance = models.CharField(max_length=255, null=True, blank=True)
    issued_at = models.DateTimeField(null=True, blank=True)

    @property
    def auth_url(self):
        return 'https://%s.salesforce.com/services/oauth2/authorize' % (
            'test' if settings.SALESFORCE_SANDBOX else 'login',
        )

    @property
    def logout_url(self):
        return 'https://%s.salesforce.com/services/oauth2/revoke' % (
            'test' if settings.SALESFORCE_SANDBOX else 'login',
        )

    @property
    def token_url(self):
        return 'https://%s.salesforce.com/services/oauth2/token' % (
            'test' if settings.SALESFORCE_SANDBOX else 'login',
        )

    @property
    def api_url(self):
        return '%s/services/data/v45.0/' % (self.instance, )

    @classmethod
    def logout(cls):
        obj, created = cls.objects.get_or_create(id=1)
        res = requests.post(obj.logout_url, data={
            'token': obj.access_token,
        })

        obj.delete()

        return res.status_code


    @classmethod
    def api_query(cls, url=None, method='get', data=None):

        if not data:
            data = {}

        obj, created = cls.objects.get_or_create(id=1)

        headers = {'Authorization': 'Bearer %s' % (obj.access_token,)}

        # print json.dumps(data, indent=4)

        res = getattr(requests, method)(
            url='%s%s' % (obj.api_url, url),
            json=data,
            headers=headers
        )

        if 400 <= res.status_code <= 403:
            headers = {'Authorization': 'Bearer %s' % (cls.refresh(),)}

            res = getattr(requests, method)(
                url='%s%s' % (obj.api_url, url),
                json=data,
                headers=headers
            )

        # print res, res.json()

        if 200 <= res.status_code < 300:
            return res.json() if res.status_code != 204 else {}

        return None


    @classmethod
    def refresh(cls):

        obj, created = cls.objects.get_or_create(id=1)

        if not obj.instance:
            return None

        data = {
            'grant_type': 'refresh_token',
            'client_id': settings.SALESFORCE_CLIENT_ID,
            'client_secret': settings.SALESFORCE_CLIENT_SECRET,
            'refresh_token': obj.refresh_token,
        }

        # print json.dumps(data, indent=4)

        oauth_response = requests.post(obj.token_url, data)

        oauth_response.raise_for_status()
        oauth_body = oauth_response.json()
        # print json.dumps(oauth_body, indent=4)
        obj.access_token = oauth_body.get('access_token')
        obj.issued_at = datetime.fromtimestamp(int(oauth_body.get('issued_at')) / 1000)
        obj.instance = oauth_body.get('instance_url')

        obj.save()

        return obj.access_token

    def leads(self):

        headers = {'Authorization': 'Bearer %s' % (self.access_token, )}

        res = requests.get(
            '%ssobjects/Lead/describe/' % (self.api_url, ),
            headers=headers
        )
        # print json.dumps(res.json(), indent=4)

    class Meta:
        verbose_name_plural = 'Salesforce Access'


class SalesforceField(Base):

    class TYPE:
        STRING = 's'
        PICKLIST = 'p'
        INT = 'i'
        BOOL = 'b'

    TYPE_CHOICES = (
        (TYPE.STRING, u'String'),
        (TYPE.PICKLIST, u'Picklist'),
        (TYPE.INT, u'Integer'),
        (TYPE.BOOL, u'Boolean')
    )

    name = models.CharField(max_length=32, db_index=True)
    parent = models.CharField(max_length=16, db_index=True, null=True, blank=True)
    type = models.CharField(max_length=1, db_index=True, choices=TYPE_CHOICES)
    values = CustomListField(default={}, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    search = models.BooleanField(default=False, db_index=True)
    development = models.BooleanField(default=False, db_index=True)

    @classmethod
    def sync(cls, parent='Lead'):

        access, created = SalesforceAccess.objects.get_or_create(id=1)

        if not access.instance:
            return None

        headers = {'Authorization': 'Bearer %s' % (access.access_token,)}

        res = requests.get(
            '%ssobjects/%s/describe/' % (access.api_url, parent),
            headers=headers
        ).json()

        fields = dict([(f['name'], f) for f in res['fields']])

        for field in cls.objects.filter(parent=parent):

            if field.name not in fields or field.type != cls.TYPE.PICKLIST:
                continue

            values = [{
                'value': value['value'],
                'label': value['label'],
            } for value in fields[field.name]['picklistValues'] if value['active']]

            relation = fields[field.name].get('relationshipName', None)

            if relation and relation == 'RecordType':
                res = requests.get(
                    '%ssobjects/%s/describe/layouts/' % (access.api_url, parent),
                    headers=headers
                ).json()

                values = [{
                    'value': record_type['recordTypeId'],
                    'label': record_type['name'],
                } for record_type in res['recordTypeMappings'] if record_type['available'] and record_type['active']]

                # print json.dumps(res, indent=4)

            field.values = values
            field.updated_at = timezone.now()
            field.save()

        # print json.dumps(fields, indent=4)
        # print "========"
        # print json.dumps(fields['RecordType'], indent=4)

    def __unicode__(self):
        return '%s: %s' % (self.parent, self.name)


class SalesforceLead(Base):

    type = models.PositiveSmallIntegerField(db_index=True, null=True, blank=True, default=None)
    data = CustomListField(default={}, null=True, blank=True)
    api_id = models.CharField(max_length=32, db_index=True, null=True, blank=True, default=None)
    created_at = models.DateTimeField(null=True, blank=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    def send(self):
        if self.api_id or self.sent_at:
            return

        print "Salesforce: Sending..."

        type_mapping = {
            3: 'Thrive Lead'
        }

        values = dict([(
            value['label'], value['value']
        ) for value in SalesforceField.objects.get(name='RecordTypeId').values])

        result = SalesforceAccess.api_query(
            url='sobjects/Lead/',
            method='post',
            data=self.data
        )

        if result and result['id']:
            self.api_id = result['id']
            self.sent_at = timezone.now()
            self.save(update_fields=('api_id', 'sent_at',))

            mapped = type_mapping.get(self.type, None)

            if mapped:

                SalesforceAccess.api_query(
                    url='sobjects/Lead/%s' % (self.api_id, ),
                    method='patch',
                    data={
                        'RecordTypeId': values[mapped]
                    }
            )

    def save(self, force_insert=False, *args, **kwargs):

        if not self.id:
            self.created_at = timezone.now()
            super(SalesforceLead, self).save(force_insert=force_insert, *args, **kwargs)
            send.delay(self.id)
            return

        super(SalesforceLead, self).save(force_insert=force_insert, *args, **kwargs)

