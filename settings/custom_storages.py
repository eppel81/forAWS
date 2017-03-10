from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class StaticFilesStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    region_name = 'eu-west-2'


class MediaFilesStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    region_name = 'eu-west-2'
