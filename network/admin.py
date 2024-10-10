from django.contrib import admin
from .models import Node, Product, Contact


# Action для обнуления задолженности
@admin.action(description="Очистить задолженность перед поставщиком")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt_to_supplier=0)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "country", "city", "street", "building_number")
    search_fields = ("email", "city")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "product_name", "product_model", "release_date")
    search_fields = ("product_name",)


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "get_level",
        "contact",
        "supplier",
        "get_product",
        "debt_to_supplier",
        "created_at",
    )
    list_display_links = ["supplier"]
    # Фильтрация по городу
    list_filter = ("contact__city",)
    # Поиск по имени звена сети
    search_fields = ("name",)
    # Кнопка "Очистить задолженность перед поставщиком"
    actions = [clear_debt]

    def get_product(self, obj):
        return ", ".join(
            [product.product_name for product in obj.product.all()]
        ).title()

    get_product.short_description = "Продукт"

    def get_level(self, obj):
        return obj.get_level_display()

    get_level.short_description = "Уровень сети"
