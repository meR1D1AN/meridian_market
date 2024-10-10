from rest_framework import serializers
from .models import Node, Product, Contact


# Сериализатор для модели Contact
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


# Сериализатор для модели Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


# Основной сериализатор для модели Node
class NodeSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(read_only=True)
    product = ProductSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    supplier = serializers.CharField(read_only=True)

    class Meta:
        model = Node
        fields = [
            "id",
            "name",
            "level",
            "contact",
            "product",
            "supplier",
            "debt_to_supplier",
            "created_at",
        ]
