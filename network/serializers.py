from rest_framework import serializers
from .models import Node


class NodeSerializer(serializers.ModelSerializer):
    supplier = serializers.StringRelatedField()

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
            "supplier",
            "debt_to_supplier",
            "created_at",
            "type",
        ]
        read_only_fields = ["debt_to_supplier"]
