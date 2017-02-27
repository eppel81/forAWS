# try:
#     from .common import *
# except ImportError:
#     pass

from settings.common import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'forAWS',
        'USER': 'awsuser',
        'PASSWORD': 'Qq123123',
        'HOST': 'foraws.c9dlfukonvxr.us-west-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}


INSTALLED_APPS += ('storages',)
AWS_STORAGE_BUCKET_NAME = "test-aws-uploads"
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL
