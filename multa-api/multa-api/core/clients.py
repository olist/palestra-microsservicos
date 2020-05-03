import boto3

from django.conf import settings

sns_client_options = {
    "region_name": settings.AWS_DEFAULT_REGION,
    "aws_access_key_id": settings.AWS_ACCESS_KEY_ID,
    "aws_secret_access_key": settings.AWS_SECRET_ACCESS_KEY,
    "endpoint_url": settings.AWS_ENDPOINT_URL,
}

sns_client = boto3.client("sns", **sns_client_options)
