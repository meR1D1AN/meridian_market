from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Получение всех пользователей",
        responses={200: UserSerializer(many=True)},
        tags=["2. Пользователи"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Создание пользователя",
        responses={201: openapi.Response("OK", UserSerializer())},
        tags=["2. Пользователи"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение пользователя",
        responses={200: UserSerializer},
        tags=["2. Пользователи"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_STRING,
                description="Укажите ID пользователя",
            )
        ],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Обновление пользователя",
        responses={200: UserSerializer},
        tags=["2. Пользователи"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_STRING,
                description="Укажите ID пользователя",
            )
        ],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Частичное обновление пользователя",
        responses={200: UserSerializer},
        tags=["2. Пользователи"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_STRING,
                description="Укажите ID пользователя",
            )
        ],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Удаление пользователя",
        responses={204: None},
        tags=["2. Пользователи"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_STRING,
                description="Укажите ID пользователя",
            )
        ],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        serializer.save()


class CustomTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        operation_description="Принимает набор учетных данных пользователя и возвращает пару JSON веб-токенов (access и refresh) для подтверждения аутентификации этих учетных данных.",
        tags=["1. Аутентификация"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        operation_description="Обновляет токен авторизации пользователя.",
        tags=["1. Аутентификация"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
