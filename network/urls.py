from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apps import NetworkConfig
from .views import NodeViewSet

app_name = NetworkConfig.name


router = DefaultRouter()
router.register(r"nodes", NodeViewSet, basename="nodes")

urlpatterns = [
    path("", include(router.urls)),
]
