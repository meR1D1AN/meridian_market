from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from .apps import UsersConfig
from .views import UserViewSet, CustomTokenObtainPairView, CustomTokenRefreshView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path(
        "login/",
        CustomTokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        CustomTokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="refresh",
    ),
] + router.urls
