# -*- coding: utf-8 -*-

from django.contrib.auth import logout, authenticate, login
from datetime import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings
import urllib
from front.views import BaseView

from django.views.generic import TemplateView
from django.views.generic import View

from . import models
import requests
import json


class AuthorizeView(View):

    def get(self, request, *args, **kwargs):

        obj, created = models.SalesforceAccess.objects.get_or_create(id=1)

        params = {
            'client_id': settings.SALESFORCE_CLIENT_ID,
            'response_type': 'code',
            'redirect_uri': 'https://' + request.META['HTTP_HOST'] + reverse('salesforce:authorized'),
        }

        print json.dumps(params, indent=4)
        print obj.auth_url

        auth_url = '%s?%s' % (
            obj.auth_url,
            urllib.urlencode(params)
        )

        return HttpResponseRedirect(auth_url)


class AuthorizedView(View):

    def get(self, request, *args, **kwargs):

        obj, created = models.SalesforceAccess.objects.get_or_create(id=1)

        code = request.GET.get('code', None)

        data = {
            'grant_type': 'authorization_code',
            'client_id': settings.SALESFORCE_CLIENT_ID,
            'client_secret': settings.SALESFORCE_CLIENT_SECRET,
            'redirect_uri': 'https://' + request.META['HTTP_HOST'] + reverse('salesforce:authorized'),
            'code': code,
        }

        # print json.dumps(data, indent=4)

        oauth_response = requests.post(obj.token_url, data)

        oauth_response.raise_for_status()
        oauth_body = oauth_response.json()
        # print json.dumps(oauth_body, indent=4)
        obj.access_token = oauth_body.get('access_token')
        obj.instance = oauth_body.get('instance_url')
        obj.refresh_token = oauth_body.get('refresh_token')
        obj.issued_at = datetime.fromtimestamp(int(oauth_body.get('issued_at')) / 1000)

        obj.save()

        return HttpResponseRedirect(reverse('control:salesforce'))


class TestView(View):

    def get(self, request, *args, **kwargs):

        # obj, created = models.SalesforceAccess.objects.get_or_create(id=1)

        # obj.leads()

        # obj.refresh()

        models.SalesforceField.sync()

        return HttpResponse()
