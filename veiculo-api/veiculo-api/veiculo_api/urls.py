from django.conf.urls import include, url

urlpatterns = [
    url(r'^v1/', include('core.routes')),
]
