from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


from .models import Node
from .serializers import NodeSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["contact__country"]

    @swagger_auto_schema(
        operation_description="Получить список всех звеньев сети",
        responses={200: openapi.Response("OK", NodeSerializer(many=True))},
        tags=["1. Торговые сети"],
        manual_parameters=[
            openapi.Parameter(
                "country",
                openapi.IN_QUERY,
                description="Фильтр по стране",
                type=openapi.TYPE_STRING,
                required=False,
            )
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="""
        Создание новой торговой сети
        """,
        responses={200: openapi.Response("OK", NodeSerializer())},
        tags=["1. Торговые сети"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получить информацию о торговой сети",
        responses={200: NodeSerializer},
        tags=["1. Торговые сети"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID торговой сети",
            ),
        ],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Обновить информацию о торговой сети",
        responses={200: NodeSerializer},
        tags=["1. Торговые сети"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID торговой сети",
            ),
        ],
    )
    def update(self, request, *args, **kwargs):
        # Проверяем, пытается ли пользователь обновить поле debt_to_supplier
        if "debt_to_supplier" in request.data:
            raise ValidationError("Обновление поля 'debt_to_supplier' запрещено.")
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Частичное обновление информации о торговой сети",
        responses={200: NodeSerializer},
        tags=["1. Торговые сети"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID торговой сети",
            ),
        ],
    )
    def partial_update(self, request, *args, **kwargs):
        # Проверяем, пытается ли пользователь обновить поле debt_to_supplier
        if "debt_to_supplier" in request.data:
            raise ValidationError("Обновление поля 'debt_to_supplier' запрещено.")
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Удалить торговую сеть",
        responses={204: None},
        tags=["1. Торговые сети"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID торговой сети",
            ),
        ],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
