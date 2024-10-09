from rest_framework import serializers
from .models import Node, Product, Contact, Supplier


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
    contact = ContactSerializer(read_only=True)
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Supplier
        fields = "__all__"


# Основной сериализатор для модели Node
class NodeSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    supplier = SupplierSerializer(read_only=True)
    contact = ContactSerializer(read_only=True)

    class Meta:
        model = Node
        fields = [
            "id",
            "name",
            "type",
            "contact",
            "supplier",
            "product",
            "debt_to_supplier",
            "created_at",
        ]
        extra_kwargs = {
            "debt_to_supplier": {"read_only": False}  # Поле доступно для создания
        }

    # Переопределяем метод update, чтобы запретить обновление debt_to_supplier
    def update(self, instance, validated_data):
        validated_data.pop("debt_to_supplier", None)  # Убираем поле при обновлении
        return super().update(instance, validated_data)
