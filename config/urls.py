from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.views.generic import View
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="API для управления онлайн платформой торговой сети электроники Meridian Market",
        default_version="v0.01",
        description="""
        API онлайн платформы торговой сети электроники Meridian Market.
        """,
        contact=openapi.Contact(email="nikita@mer1d1an.ru"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# Вьюха, которая принудительно делает POST-запрос для логаута
class ForcePostLogoutView(View):
    def get(self, request, *args, **kwargs):
        # Создаем POST-запрос для логаута
        return LogoutView.as_view(next_page="/docs/")(request)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("network.urls")),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc"),
    # Перенаправляем GET-запрос на логаут, чтобы выполнялся POST-запрос
    path("accounts/logout/", ForcePostLogoutView.as_view()),
]
