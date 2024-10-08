from django_filters import rest_framework as filters
from .models import Node


class NodeFilter(filters.FilterSet):
    country = filters.CharFilter(field_name="contact__country")
    city = filters.CharFilter(field_name="contact__city")

    class Meta:
        model = Node
        fields = ["country", "city", "type"]

