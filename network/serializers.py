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
    # Добавляем уровень иерархии
    hierarchy_level = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    # Используем StringRelatedField для отображения имени поставщика
    supplier_parent = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Supplier
        fields = [
            "id",
            "name",
            "type",
            "contact",
            "product",
            "supplier_parent",
            "debt_to_supplier",
            "created_at",
            "hierarchy_level",
        ]
        # extra_kwargs = {
        #     "debt_to_supplier": {"read_only": False}  # Поле доступно для создания
        # }

    def get_hierarchy_level(self, obj):
        return obj.get_hierarchy_level()  # Вызываем метод для получения уровня


class SupplierUpdateSerializer(SupplierSerializer):
    class Meta:
        model = Supplier
        fields = SupplierSerializer.Meta.fields
        extra_kwargs = {
            "debt_to_supplier": {"read_only": True}  # Поле доступно для создания
        }

    def update(self, instance, validated_data):
        validated_data.pop("debt_to_supplier", None)  # Убираем поле при обновлении
        return super().update(instance, validated_data)


# Основной сериализатор для модели Node
class NodeSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(read_only=True)
    product = ProductSerializer(many=True, read_only=True)
    # Добавляем уровень иерархии
    hierarchy_level = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    supplier_node = SupplierSerializer(read_only=True)

    class Meta:
        model = Node
        fields = [
            "id",
            "name",
            "type",
            "contact",
            "supplier_node",
            "product",
            "debt_to_supplier",
            "created_at",
            "hierarchy_level",
        ]
        extra_kwargs = {
            "debt_to_supplier": {"read_only": False}  # Поле доступно для создания
        }

    def get_hierarchy_level(self, obj):
        return obj.get_hierarchy_level()  # Вызываем метод для получения уровня

    # Переопределяем метод update, чтобы запретить обновление debt_to_supplier
    def update(self, instance, validated_data):
        validated_data.pop("debt_to_supplier", None)  # Убираем поле при обновлении
        return super().update(instance, validated_data)
