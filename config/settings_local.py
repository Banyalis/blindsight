from settings import *  # noqa

DEBUG = True

#TEMPLATE_DEBUG = DEBUG

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), ) # noqa

STATIC_ROOT = None

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
