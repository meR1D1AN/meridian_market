from django.contrib import admin
from django.urls import path, include
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


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("network.urls")),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc"),
]
