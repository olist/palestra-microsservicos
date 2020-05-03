from rest_framework.routers import SimpleRouter
from .api import CarroViewSet

app_name = "core"
router = SimpleRouter()

router.register(r"carros", CarroViewSet, basename="carros")

urlpatterns = router.urls
