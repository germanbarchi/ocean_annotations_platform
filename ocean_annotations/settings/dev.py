from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'USER': 'mbmeza',
        'PASSWORD': 'teaming2021',
        'HOST': 'localhost',
        'PORT': '',                                                                                                                                       
    }
}