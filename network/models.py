from django.db import models

NULLABLE = {"null": True, "blank": True}


class Contact(models.Model):
    email = models.EmailField(
        verbose_name="Электронная почта", help_text="Укажите почту", unique=True
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

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Product(models.Model):
    product_name = models.CharField(
        max_length=255,
        verbose_name="Название продукта",
        help_text="Укажите название продукта",
    )
    product_model = models.CharField(
        max_length=255,
        verbose_name="Модель продукта",
        help_text="Укажите модель продукта",
    )
    release_date = models.DateField(
        verbose_name="Дата выпуска", help_text="Укажите дату выпуска"
    )

    def __str__(self):
        return f"{self.product_name} ({self.product_model})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["product_name"]


class Node(models.Model):
    FACTORY = 0
    RETAIL_NETWORK = 1
    ENTREPRENEUR = 2

    NODE_TYPES = [
        (FACTORY, "Завод"),
        (RETAIL_NETWORK, "Розничная сеть"),
        (ENTREPRENEUR, "Индивидуальный предприниматель"),
    ]
    # Название
    name = models.CharField(
        max_length=255, verbose_name="Название", help_text="Укажите название"
    )
    # Уровень структуры
    level = models.IntegerField(
        choices=NODE_TYPES,
        verbose_name="Уровень сети",
        help_text="Выберете уровень сети",
    )
    # Контакты
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        verbose_name="Контакты",
        help_text="Укажите контакты данные",
        related_name="%(class)s_contacts",
        **NULLABLE,
    )
    # Продукты
    product = models.ManyToManyField(
        Product,
        verbose_name="Продукты",
        help_text="Укажите продукт",
        related_name="%(class)s_products",
    )
    supplier = models.ForeignKey(
        "Node",
        on_delete=models.SET_NULL,
        verbose_name="Поставщик",
        help_text="Укажите поставщика",
        # related_name="%(class)s_suppliers",
        **NULLABLE,
    )
    # Задолженность перед поставщиком
    debt_to_supplier = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Задолженность",
        help_text="Укажите задолженность, с точностью до копеек",
        default=0.00,
    )
    # Дата и время создания
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.name} - ({self.get_level_display()})"

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"
