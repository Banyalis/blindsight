# -*- coding: utf-8 -*-

import json
from abc import ABCMeta, abstractproperty

from django.views.generic import View
from django.http import HttpResponse, Http404
from django.core.serializers.json import DjangoJSONEncoder
import data
from . import models

import copy

class Index(View):
    def get(self, request):
        context = {}

        context['index'] = data.index

        return HttpResponse(json.dumps(context, cls=DjangoJSONEncoder), content_type="application/json")

class Memories(View):
    def get(self, request):
        context = {}

        context['memories'] = data.memories

        return HttpResponse(json.dumps(context, cls=DjangoJSONEncoder), content_type="application/json")

class About(View):
    def get(self, request):
        context = {}

        context['about'] = data.about

        return HttpResponse(json.dumps(context, cls=DjangoJSONEncoder), content_type="application/json")

class MemoriesPopup(View):
    def get(self, request, slug):
        context = {}

        context['memories'] = data.memories
        context['popup'] = data.popups[slug]

        return HttpResponse(json.dumps(context, cls=DjangoJSONEncoder), content_type="application/json")