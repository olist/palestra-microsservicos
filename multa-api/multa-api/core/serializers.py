from rest_framework import serializers

from .models import Multa


class MultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multa
        fields = "__all__"
