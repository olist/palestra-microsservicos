from loafer.ext.aws.routes import SNSQueueRoute

from .config import settings
from .handlers import envia_multa_handler


provider_options = {
    "endpoint_url": settings.AWS_ENDPOINT_URL,
    "options": {"MaxNumberOfMessages": 10, "WaitTimeSeconds": 1},
}


routes = (
    SNSQueueRoute(
        settings.MULTA_CRIADA_FILA,
        provider_options=provider_options,
        handler=envia_multa_handler,
    ),
)
