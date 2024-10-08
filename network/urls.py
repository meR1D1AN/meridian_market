from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NodeViewSet
from .views import SupplierViewSet

router = DefaultRouter()
router.register(r"nodes", NodeViewSet, basename="nodes")
router.register(r"suppliers", SupplierViewSet, basename="suppliers")

urlpatterns = [
    path("", include(router.urls)),
]
