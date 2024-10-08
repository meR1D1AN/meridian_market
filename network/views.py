from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .filters import NodeFilter
from .models import Node
from .serializers import NodeSerializer
from .serializers import SupplierSerializer


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
        tags=["Торговые сети"],
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
        tags=["Торговые сети"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получить информацию о торговой сети",
        responses={200: NodeSerializer},
        tags=["Торговые сети"],
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
        tags=["Торговые сети"],
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
        tags=["Торговые сети"],
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
        tags=["Торговые сети"],
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
        # Запрещаем обновление поля debt_to_supplier через API
        serializer.save(debt_to_supplier=self.get_object().debt_to_supplier)


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Получить список всех поставщиков",
        responses={200: openapi.Response("OK", SupplierSerializer(many=True))},
        tags=["Поставщики"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получить информацию о поставщике",
        responses={200: SupplierSerializer},
        tags=["Поставщики"],
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
        responses={200: SupplierSerializer},
        tags=["Поставщики"],
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
        responses={200: SupplierSerializer},
        tags=["Поставщики"],
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
        tags=["Поставщики"],
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
        tags=["Поставщики"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
