from django.db import models
from django.urls import reverse

NULLABLE = {"null": True, "blank": True}


class Node(models.Model):
    FACTORY = "factory"
    RETAIL_NETWORK = "retail_network"
    ENTREPRENEUR = "entrepreneur"

    NODE_TYPES = [
        (FACTORY, "Завод"),
        (RETAIL_NETWORK, "Розничная сеть"),
        (ENTREPRENEUR, "Индивидуальный предприниматель"),
    ]
    # Название
    name = models.CharField(
        max_length=255, verbose_name="Название", help_text="Укажите название"
    )
    # Контакты
    email = models.EmailField(
        verbose_name="Электронная почта", help_text="Укажите почту"
    )
    country = models.CharField(
        max_length=100, verbose_name="Страна", help_text="Укажите страну"
    )
    city = models.CharField(
        max_length=100, verbose_name="Город", help_text="Укажите город"
    )
    street = models.CharField(
        max_length=100, verbose_name="Улица", help_text="Укажите улица"
    )
    building_number = models.CharField(
        max_length=10, verbose_name="Номер дома", help_text="Укажите номер дома"
    )
    # Продукты
    product_name = models.CharField(
        max_length=255,
        verbose_name="Название продукта",
        help_text="Укажите Название продукта",
    )
    product_model = models.CharField(
        max_length=100,
        verbose_name="Модель продукта",
        help_text="Укажите модель продукта",
    )
    release_date = models.DateField(
        verbose_name="Дата выхода на рынок", help_text="Укажите дату выхода на рынок"
    )
    # Поставщик
    supplier = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="clients",
        verbose_name="Поставщик",
        help_text="Выберите поставщика",
        **NULLABLE,
    )
    # Задолженность перед поставщиком
    debt_to_supplier = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Задолженность",
        help_text="Укажите задолженность, с точносью до копеек",
        default=0.00,
    )
    # Дата и время создания
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания и время создания"
    )
    # Уровень структуры
    type = models.CharField(
        max_length=20,
        choices=NODE_TYPES,
        verbose_name="Структура",
        help_text="Выберите структуру",
    )

    class Meta:
        verbose_name = "Торговая сеть электроники"
        verbose_name_plural = "Торговые сети электроники"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_admin_url(self):
        return reverse("admin:network_node_change", args=[self.id])
