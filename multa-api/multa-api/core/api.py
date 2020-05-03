from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Multa
from .serializers import MultaSerializer


class MultaViewSet(ModelViewSet):
    queryset = Multa.objects.all()
    serializer_class = MultaSerializer
    permission_classes = [AllowAny]
    http_method_names = ["get", "post"]
