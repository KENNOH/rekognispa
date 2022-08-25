from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings
import os

class StaticStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = settings.STATIC_ROOT

class MediaStorage(S3Boto3Storage):
    bucket_name = 'media'
    location = 'media'
