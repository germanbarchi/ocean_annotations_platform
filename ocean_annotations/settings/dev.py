from .base import *

DEBUG = True

ALLOWED_HOSTS = ['ec2-3-145-0-236.us-east-2.compute.amazonaws.com','localhost', '127.0.0.1']


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ocean_test_liaa',
        'USER': 'gbarchi',
        'PASSWORD': 'g.barchi',
        'HOST': 'localhost',
        'PORT': '',
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#        'USER': 'mbmeza',
#        'PASSWORD': 'teaming2021',
#        'HOST': 'localhost',
#        'PORT': '',                                                                                                                                       
#    }
#}