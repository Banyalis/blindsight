# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.http.response import HttpResponse, HttpResponseRedirect
from django.db.models import Prefetch
from django.http import Http404
from . import models
from datetime import date

# from serializers import common, true, search, technologies, development

from djangorestframework_camel_case.render import CamelCaseJSONRenderer

import json
import data


# Базовая вьюха, от которой наследуются остальные
class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        # Тут можно определить контекст, характерный для всех страниц сайта (например, разделы меню и т.п.)

        context['header'] = data.header

        return context

class Custom404View(BaseView):
    template_name = 'front/pages/NotFound/NotFound.jinja'

    def get_context_data(self, **kwargs):
        context = super(Custom404View, self).get_context_data(**kwargs)

        context['error'] = data.error

        return context

    @classmethod
    def get_rendered_view(cls):
        as_view_fn = cls.as_view()

        def view_fn(request):
            response = as_view_fn(request)
            # this is what was missing before
            response.render()
            return response

        return view_fn

    def get(self, request, *args, **kwargs):
        response = super(Custom404View, self).get(request, *args, **kwargs)
        response['Status'] = 'Not Found'
        response.reason_phrase = 'NOT FOUND'
        response.status_code = 404
        return response


class IndexView(BaseView):
    template_name = 'front/pages/Index/IndexSection.jinja'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['index'] = data.index

        return context

class MemoriesView(BaseView):
    template_name = 'front/pages/Memories/MemoriesSection.jinja'

    def get_context_data(self, **kwargs):
        context = super(MemoriesView, self).get_context_data(**kwargs)

        context['memories'] = data.memories

        return context

class AboutView(BaseView):
    template_name = 'front/pages/About/AboutSection.jinja'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)

        context['about'] = data.about

        return context

class MemoriesPopup(MemoriesView):
    template_name = 'front/pages/MemoriesPopup/Memories.jinja'

    def get_context_data(self, **kwargs):
        context = super(MemoriesPopup, self).get_context_data(**kwargs)
        slug = kwargs.get('slug', None)

        context['popup'] = data.popups[slug]

        return context