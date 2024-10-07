from django.contrib import admin
from django.utils.html import format_html

from .models import Node


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "type",
        "country",
        "city",
        "product_name",
        "supplier_link",
        "debt_to_supplier",
        "created_at",
    )
    list_filter = ("country", "city", "type")
    search_fields = ("name", "city")
    autocomplete_fields = ["supplier"]
    actions = ["clear_debt"]

    # Метод для отображения ссылки на поставщика
    def supplier_link(self, obj):
        if obj.supplier:
            # Возвращаем HTML ссылку на поставщика, если он есть
            return format_html(
                '<a href="{}">{}</a>', obj.supplier.get_admin_url(), obj.supplier.name
            )
        # Если поставщика нет, возвращаем "(Нет поставщика)"
        return "(Нет поставщика)"

    supplier_link.short_description = "Поставщик"  # Заголовок колонки

    # Admin action для обнуления задолженности
    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_debt(self, request, queryset):
        queryset.update(debt_to_supplier=0)
