from django.db import models
from django.urls import reverse

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


class BaseClass(models.Model):
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
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        verbose_name="Контакты",
        help_text="Укажите контакты данные",
        related_name="nodes",
        **NULLABLE,
    )
    # Продукты
    product = models.ManyToManyField(
        Product,
        verbose_name="Продукты",
        help_text="Укажите продукт",
        related_name="nodes",
        blank=True,
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
        auto_now_add=True, verbose_name="Дата и время создания"
    )
    # Уровень структуры
    type = models.CharField(
        max_length=20,
        choices=NODE_TYPES,
        verbose_name="Структура",
        help_text="Выберите структуру",
    )


class Supplier(BaseClass):
    # Поставщик
    supplier_parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="suppliers",
        max_length=255,
        verbose_name="Поставщик",
        help_text="Укажите поставщика",
        **NULLABLE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
        ordering = ["name"]

    def get_admin_url(self):
        return reverse("admin:network_supplier_change", args=[self.id])


class Node(BaseClass):
    # Поставщик
    supplier_node = models.ForeignKey(
        Supplier,
        on_delete=models.SET_NULL,
        verbose_name="Поставщик",
        help_text="Выберите поставщика",
        related_name="supplier_nodes",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Торговая сеть электроники"
        verbose_name_plural = "Торговые сети электроники"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

    def get_admin_url(self):
        return reverse("admin:network_supplier_node_change", args=[self.id])

    def save(self, *args, **kwargs):
        if self.debt_to_supplier < 0:
            raise ValueError("Задолженность не может быть отрицательной.")
        elif (
            self.supplier_node
            and not Supplier.objects.filter(id=self.supplier_node.id).exists()
        ):
            raise ValueError("Выбранный поставщик не существует.")
        super().save(*args, **kwargs)
