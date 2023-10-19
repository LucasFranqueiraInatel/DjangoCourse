from .settings import *

from django.core.management.utils import get_random_secret_key
SECRET_KEY = get_random_secret_key()

DEBUG = False
ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ('127.0.0.1', 'localhost',)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sidia',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'db',
        'PORT': '5432',
    }
}