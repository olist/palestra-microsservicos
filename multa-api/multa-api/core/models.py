import json

from django.conf import settings
from django.db import models
from django.dispatch import receiver

from .clients import sns_client


class TipoMulta(models.Model):
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.CharField(max_length=255)


class Multa(models.Model):
    tipo = models.ForeignKey(TipoMulta, on_delete=models.CASCADE)
    placa = models.CharField(max_length=255)

    @property
    def as_dict(self):
        return {
            "id": self.id,
            "tipo": {"valor": str(self.tipo.valor), "descricao": self.tipo.descricao},
            "placa": self.placa,
        }


@receiver(models.signals.post_save, sender=Multa)
def publica_multa(sender, **kwargs):
    multa = kwargs.get("instance")

    sns_client.publish(
        TopicArn=settings.MULTA_TOPICO_ARN,
        Message=json.dumps(multa.as_dict),
    )
