from django.contrib import admin
from django.utils.html import format_html
from .models import Node, Product, Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "country", "city", "street", "building_number")
    search_fields = ("email", "city")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_model", "release_date")
    search_fields = ("product_name", "product_model")


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "type",
        "contact",
        "get_product",
        "supplier_link",
        "debt_to_supplier",
        "created_at",
    )
    list_filter = ("type", "contact__city")
    search_fields = ("name",)

    # Ссылка на поставщика
    def supplier_link(self, obj):
        if obj.supplier:
            return format_html(
                '<a href="{}">{}</a>', obj.supplier.get_admin_url(), obj.supplier.name
            )
        return "(Нет поставщика)"

    supplier_link.short_description = "Поставщик"

    # Action для обнуления задолженности
    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_debt(self, request, queryset):
        queryset.update(debt_to_supplier=0)

    actions = [clear_debt]

    def get_product(self, obj):
        return ", ".join([product.product_name for product in obj.product.all()])

    get_product.short_description = "Контактная информация"
