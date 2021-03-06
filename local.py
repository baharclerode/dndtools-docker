# -*- coding: utf-8 -*-

import os

# Change this to False if you run it in development
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# See https://docs.djangoproject.com/en/1.6/ref/settings/#databases for reference
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['MYSQL_DATABASE'],
        'USER': os.environ['MYSQL_USER'],
        'PASSWORD': os.environ['MYSQL_PASSWORD'],
        'HOST': os.getenv('MYSQL_HOST','127.0.0.1'),
        'PORT': '',
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
            },
        }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.getenv('SECRET_KEY', 'TODO FILL')

SITE_ID = 1

if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    )

RECAPTCHA_PUBLIC = 'TODO FILL'
RECAPTCHA_PRIVATE = 'TODO FILL'
