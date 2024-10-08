from rest_framework import serializers
from .models import Node, Product, Contact


# Сериализатор для модели Contact (контактная информация)
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["email", "country", "city", "street", "building_number"]


# Сериализатор для модели Product (продукты)
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["product_name", "product_model", "release_date"]


# Сериализатор для поставщика (отдельный)
class SupplierSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(read_only=True)  # Контактная информация для поставщика

    class Meta:
        model = Node
        fields = [
            "id",
            "name",
            "type",
            "contact",
        ]  # Выводим только нужные поля (без debt_to_supplier)


# Основной сериализатор для модели Node
class NodeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(
        many=True, read_only=True
    )  # Продукты как вложенные объекты
    contact = ContactSerializer(read_only=True)  # Контакты как вложенные объекты
    supplier = SupplierSerializer(
        read_only=True
    )  # Поставщик через отдельный сериализатор

    class Meta:
        model = Node
        fields = [
            "id",
            "name",
            "type",
            "contact",
            "products",
            "supplier",
            "debt_to_supplier",
            "created_at",
        ]
        read_only_fields = ["debt_to_supplier"]
