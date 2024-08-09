from django.conf import settings
from storages.backends.s3boto3 import S3StaticStorage

class CustomS3StaticStorage(S3StaticStorage):
    location = settings.AWS_MEDIA_LOCATION