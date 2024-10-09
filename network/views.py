from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .filters import NodeFilter
from .models import Node, Supplier
from .serializers import NodeSerializer
from .serializers import SupplierSerializer, SupplierUpdateSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_class = NodeFilter
    filterset_fields = ["contact__country"]

    @swagger_auto_schema(
        operation_description="Получить список всех тоговых сетей",
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
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Удалить тоговую сеть",
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

    def perform_update(self, serializer):
        # Проверяем, пытается ли пользователь обновить поле debt_to_supplier
        if "debt_to_supplier" in serializer.validated_data:
            raise ValidationError("Обновление поля 'debt_to_supplier' запрещено.")
        # Если поле не обновляется, продолжаем обновление
        serializer.save(debt_to_supplier=self.get_object().debt_to_supplier)


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return SupplierUpdateSerializer  # Для обновления
        return SupplierSerializer

    @swagger_auto_schema(
        operation_description="Получить список всех поставщиков",
        responses={200: openapi.Response("OK", SupplierSerializer(many=True))},
        tags=["2.Поставщики"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получить информацию о поставщике",
        responses={200: SupplierSerializer},
        tags=["2.Поставщики"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID поставщика",
            )
        ],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Обновить информацию о поставщике",
        responses={200: SupplierUpdateSerializer},
        tags=["2.Поставщики"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID поставщика",
            )
        ],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Частичное обновление информации о поставщике",
        responses={200: SupplierUpdateSerializer},
        tags=["2.Поставщики"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID поставщика",
            )
        ],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Удалить поставщика",
        responses={204: None},
        tags=["2.Поставщики"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID поставщика",
            )
        ],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="""
        Создание нового поставщика
        """,
        responses={200: openapi.Response("OK", SupplierSerializer())},
        tags=["2.Поставщики"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
