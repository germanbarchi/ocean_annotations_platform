from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['fabula.exp.dc.uba.ar', 'localhost']


DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': 'backups/'}


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ocean_annotations',
        'USER': 'mbmeza',
        'PASSWORD': 'teaming2021',
        'HOST': 'localhost',
        'PORT': '',
    }
}


STATIC_URL = "/pair_comparison/static/"
SITE_ROOT = '/home/mbmeza/pair_comparison/ocean_annotations/'
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'ocean_annotations/static/'),
)

MEDIA_URL = "/ocean_annotations/media/"

# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

# sentry_sdk.init(
#     dsn="https://764ecaf140484992b316e7fc0b88c40c@o219390.ingest.sentry.io/6584845",
#     integrations=[
#         DjangoIntegration(),
#     ],

#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     # We recommend adjusting this value in production.
#     traces_sample_rate=1.0,

#     # If you wish to associate users to errors (assuming you are using
#     # django.contrib.auth) you may enable sending PII data.
#     send_default_pii=True
# )
