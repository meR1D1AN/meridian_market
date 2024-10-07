import django_filters
from .models import Node


class NetworkNodeFilter(django_filters.FilterSet):
    class Meta:
        model = Node
        fields = ["country", "city"]  # Фильтрация по стране и городу
