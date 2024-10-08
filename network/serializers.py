from rest_framework import serializers
from .models import Node


# Сериализатор для поставщика
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = [
            "id",
            "name",
            "email",
            "country",
            "city",
            "street",
            "building_number",
            "product_name",
            "product_model",
            "release_date",
            "created_at",
            "type",
        ]
        # Поле "created_at" только для чтения
        read_only_fields = ["created_at"]


# Основной сериализатор для узлов сети
class NodeSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)  # Используем SupplierSerializer для отображения поставщика

    class Meta:
        model = Node
        fields = [
            "id",
            "name",
            "email",
            "country",
            "city",
            "street",
            "building_number",
            "product_name",
            "product_model",
            "release_date",
            "supplier",  # Поставщик отображается через отдельный сериализатор
            "debt_to_supplier",  # Поле задолженности
            "created_at",
            "type",
        ]
        # Поле "debt_to_supplier" доступно только для чтения (нельзя обновить через API)
        read_only_fields = ["debt_to_supplier", "created_at"]
