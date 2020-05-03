from rest_framework import serializers

from .models import Carro, Proprietario


class ProprietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprietario
        fields = "__all__"
        read_only = ('id',)


class CarroSerializer(serializers.ModelSerializer):
    proprietario = ProprietarioSerializer()

    class Meta:
        model = Carro
        fields = "__all__"
        read_only = ('id',)

    def create(self, validated_data):
        proprietario = validated_data.pop("proprietario")
        proprietario = Proprietario.objects.create(**proprietario)
        validated_data["proprietario_id"] = proprietario.id
        carro = Carro.objects.create(**validated_data)
        return carro
