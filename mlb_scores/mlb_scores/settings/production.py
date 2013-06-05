from .base import *
from os import environ
from urlparse import urlparse
from django.core.exceptions import ImproperlyConfigured
import dj_database_url


DEBUG = True

TEMPLATE_DEBUG = DEBUG








DATABASES = {}
DATABASES['default'] =  dj_database_url.config()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

