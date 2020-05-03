from rest_framework.routers import SimpleRouter
from .api import MultaViewSet

app_name = "core"
router = SimpleRouter()


router.register(r"multas", MultaViewSet, basename="multas")

urlpatterns = router.urls
