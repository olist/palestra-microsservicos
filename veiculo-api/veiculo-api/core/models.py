from django.db import models


class Proprietario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()


class Carro(models.Model):
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE)
    placa = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
