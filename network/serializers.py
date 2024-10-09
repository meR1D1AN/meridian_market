from rest_framework import serializers
from .models import Node, Product, Contact, Supplier, BaseClass


# Сериализатор для модели Contact
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["email", "country", "city", "street", "building_number"]


# Сериализатор для модели Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["product_name", "product_model", "release_date"]


# Сериализатор для родительлской модели
class BaseClassSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(read_only=True)
    product = ProductSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    # Добавляем уровень иерархии
    hierarchy_level = serializers.SerializerMethodField()

    class Meta:
        model = BaseClass
        fields = [
            "id",
            "name",
            "type",
            "contact",
            "product",
            "debt_to_supplier",
            "created_at",
            "hierarchy_level",
        ]

    def get_hierarchy_level(self, obj):
        return obj.get_hierarchy_level()  # Вызываем метод для получения уровня


# Сериализатор для поставщика
class SupplierSerializer(BaseClassSerializer):
    # Используем StringRelatedField для отображения имени поставщика
    supplier_parent = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Supplier
        fields = BaseClassSerializer.Meta.fields + ["supplier_parent"]


# Основной сериализатор для модели Node
class NodeSerializer(BaseClassSerializer):
    supplier_node = SupplierSerializer(read_only=True)

    class Meta:
        model = Node
        fields = BaseClassSerializer.Meta.fields + ["supplier_node"]
