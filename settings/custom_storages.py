from storages.backends.s3boto import S3BotoStorage
from django.conf import settings


class StaticFilesStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION


class MediaFilesStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION
