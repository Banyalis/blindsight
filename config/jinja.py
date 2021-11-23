# -*- coding: utf-8 -*-
import json
import os
import re

from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.translation import ugettext
from django.core.urlresolvers import reverse
from django.template.loader import engines
from django.utils.html import linebreaks, escape
from django.conf import settings
from django.utils import timezone
from datetime import datetime
import pendulum

from jinja2 import Environment

from config.settings import BASE_DIR


def includeraw(template):
    env = engines['jinja2'].env
    source, fn, _ = env.loader.get_source(env, template)

    return source


def active(request, pattern):
    """
    Template tag to highlight selected page in the menu
    """
    if re.search(pattern, request.path):
        return 'isActive'
    return ''


def jsonify(value):
    return json.dumps(value)


def require(template):
    return includeraw(template)

def nl2br(input):
    return linebreaks(escape(input))

def format_datetime(date, format):
    dt = date if isinstance(date, datetime) else pendulum.parse(date) if isinstance(date, basestring)\
        else timezone.localtime(date)
    return dt.strftime(format)


def bundle(bundle_name, chunk_name, file):
    if settings.DEBUG:
        with open(os.path.join(settings.BASE_DIR, 'webpack.{}.stats.json'.format(bundle_name))) as stats:
            bundle_data = json.load(stats)
    else:
        bundle_data = settings.WEBPACK_BUNDLES.get(bundle_name, None)

    file_data = file.split('.')
    file_name = file_data[0]
    file_ext = file_data[1]

    chunk = bundle_data['chunks'].get(chunk_name, [])

    try:
        bundle_file_name = [str(f['name']) for f in chunk if os.path.basename(str(f['name'])).startswith(file_name) and os.path.basename(str(f['name'])).endswith(file_ext)][0]
    except IndexError:
        bundle_file_name = ''

    return bundle_file_name


def is_mobile(request):
    return request.is_mobile and not request.is_tablet

def is_tablet(request):
    return request.is_mobile and request.is_tablet


def environment(**options):
    env = Environment(**options)

    if os.path.isfile(os.path.join(BASE_DIR, 'config.json')):
        with open(os.path.join(BASE_DIR, 'config.json')) as f:
            config = json.loads(f.read())
    else:
        with open(os.path.join(BASE_DIR, 'config.test.json')) as f:
            config = json.loads(f.read())

    env.filters['jsonify'] = jsonify
    env.filters['require'] = require
    env.filters['datetime'] = format_datetime
    env.filters['nl2br'] = nl2br

    env.globals.update({
        'bundle': bundle,
        'static': staticfiles_storage.url,
        'active': active,
        'url': reverse,
        '_': ugettext,
        'config': config,
        'settings': settings,
        'DEBUG': settings.DEBUG,
        'STATIC_URL': settings.STATIC_URL,
        'HOT_RELOADING': settings.HOT_RELOADING,
        'MEDIA_URL': settings.MEDIA_URL,
        'includeraw': includeraw,
        'isMobile': is_mobile,
        'isTablet': is_tablet
    })
    return env
