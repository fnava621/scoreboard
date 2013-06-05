from .base import *
from os import environ
from urlparse import urlparse
from django.core.exceptions import ImproperlyConfigured
import dj_database_url


DEBUG = False

TEMPLATE_DEBUG = DEBUG

DATABASES = {}

SOUTH_DATABASE_ADAPTERS = {'default':'south.db.postgresql_psycopg2'}

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



