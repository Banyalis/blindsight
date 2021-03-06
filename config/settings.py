# -*- coding: utf-8 -*-

"""
Django settings for starter project.

Generated by 'django-admin startproject' using Django 1.8.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import json
from datetime import timedelta

from kombu import Exchange, Queue

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if os.path.isfile(os.path.join(BASE_DIR, 'config.json')):
    with open(os.path.join(BASE_DIR, 'config.json')) as f:
        config = json.loads(f.read())
else:
    with open(os.path.join(BASE_DIR, 'config.test.json')) as f:
        config = json.loads(f.read())


def get_config(setting, config=config, quite=False):
    """Get the secret variable or return explicit exception."""
    try:
        return config[setting]
    except KeyError:
        if not quite:
            print "Set the {0} config parameter in config.json".format(setting)
        return ''


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r5ivw==#o&3qftu=8!&40zct%)$-mc1-jb6cbvx1685ee(*wa('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ('*', )

INTERNAL_IPS = ('127.0.0.1', )

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'front',
    # 'tools.salesforce',
    'tools.files',
    'django_filters',
    'rest_framework',
    'django_js_reverse',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # ?????????????????????????????????? ???????? ???????????????????? ???????????????????? ???????????????? ?????????????????? ???????????? ??????????
    'tools.various.middleware.MobileDetectionMiddleware',
)

ROOT_URLCONF = 'config.urls'

JINJA_DEFAULT_CACHE_SIZE = 400
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(os.path.abspath(BASE_DIR), 'templates'),
                 os.path.join(os.path.abspath(BASE_DIR), 'assets', 'app'),
                 os.path.join(os.path.abspath(BASE_DIR), 'assets', 'custom_libs'),
                 os.path.join(os.path.abspath(BASE_DIR), 'static')],
        'APP_DIRS': True,
        'OPTIONS': {
            'auto_reload': DEBUG,
            'trim_blocks': True,
            'lstrip_blocks': True,
            'cache_size': 0 if DEBUG else JINJA_DEFAULT_CACHE_SIZE,
            'environment': 'config.jinja.environment',
            'extensions': ['jinja2.ext.do', 'jinja2.ext.loopcontrols', 'jinja2.ext.i18n', 'jinja2.ext.with_',],
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': get_config('DB_NAME'),
#         'USER': get_config('DB_USER'),
#         'PASSWORD': get_config('DB_PASSWORD'),
#         'HOST': get_config('DB_HOST'),
#         'PORT': get_config('DB_PORT'),
#     }
# }

CACHE_INVALIDATE_ON_CREATE = 'whole-model'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:%s' % (get_config('CACHE_PORT', quite=True) or '11211', ),
    },
    'cache_machine': {
        'BACKEND': 'caching.backends.memcached.MemcachedCache',
        'LOCATION': [
            '127.0.0.1:%s' % (get_config('CACHE_PORT', quite=True) or '11211', )
        ],
        'KEY_PREFIX': '%s:cm:' % (get_config('CACHE_PREFIX'),),
    },
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        # Any other renders
    ),

    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        # Any other parsers
    ),
    # 'DEFAULT_FILTER_BACKENDS': (
    #     'django_filters.rest_framework.DjangoFilterBackend',
    # ),
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


class Lang:
    En = 'en'


LANGUAGES = (
    (Lang.En, 'English'),
)

LANGUAGES_TUPLE = (Lang.En, )


# REDIS
# REDIS_HOST = get_config('REDIS_HOST')
# REDIS_PORT = get_config('REDIS_PORT')
# REDIS_DB = get_config('REDIS_DB')

# CELERY SETTINGS
# CONFIG_CELERY_QUEUE = get_config('CELERY_QUEUE', quite=True) or 'true'
# BROKER_URL = 'redis://%s:%d/%d' % (REDIS_HOST, REDIS_PORT, REDIS_DB)
# CELERY_DEFAULT_QUEUE = CONFIG_CELERY_QUEUE
# CELERY_QUEUES = (
#     Queue(CONFIG_CELERY_QUEUE, Exchange(CONFIG_CELERY_QUEUE), routing_key=CONFIG_CELERY_QUEUE),
# )
# CELERY_ENABLE_UTC = True

# CELERYBEAT_SCHEDULE = {
#     'salesforce-sync': {
#         'task': 'tools.salesforce.tasks.sync',
#         'schedule': timedelta(minutes=10),
#     },
# }

#ANYMAIL
# EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
# ANYMAIL = get_config('ANYMAIL')
# DEFAULT_FROM_EMAIL = get_config('DEFAULT_FROM_EMAIL')

# EMAIL_SEND = get_config('EMAIL_SEND', quite=True) or False

# SALESFORCE_CLIENT_ID = get_config('SALESFORCE_CLIENT_ID')
# SALESFORCE_CLIENT_SECRET = get_config('SALESFORCE_CLIENT_SECRET')
# SALESFORCE_SANDBOX = get_config('SALESFORCE_SANDBOX', quite=True)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

HOT_RELOADING = get_config('HOT_RELOADING') or False

MEDIA_LOCATION = 'media'
MEDIA_TEMP_URL = "/%s/" % (MEDIA_LOCATION,)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = (get_config('STATIC_URL_HOT') if HOT_RELOADING else get_config('STATIC_URL')) or get_config('STATIC_URL') or '/static/'
MEDIA_URL = get_config('MEDIA_URL') or "/%s/" % (MEDIA_LOCATION,)

FRONT_STATS = None
CONTROL_STATS = None

try:
    with open(os.path.join(BASE_DIR, 'webpack.front.stats.json')) as front_stats:
        FRONT_STATS = json.load(front_stats)
except IOError:
    print 'No webpack.front.stats.json file'

try:
    with open(os.path.join(BASE_DIR, 'webpack.control.stats.json')) as control_stats:
        CONTROL_STATS = json.load(control_stats)
except IOError:
    print 'No webpack.control.stats.json file'

# Information to link builded static files with Django.
# For Django to know by what name to reference
WEBPACK_BUNDLES = {
    'front': FRONT_STATS,
    'control': CONTROL_STATS,
}
