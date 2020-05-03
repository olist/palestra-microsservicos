from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Carro
from .serializers import CarroSerializer


class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    permission_classes = [AllowAny]
    lookup_field = "placa"
    http_method_names = ["get", "post"]
