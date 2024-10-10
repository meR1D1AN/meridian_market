# Generated by Django 5.1.2 on 2024-10-10 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Укажите почту",
                        max_length=254,
                        unique=True,
                        verbose_name="Электронная почта",
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        help_text="Укажите страну",
                        max_length=100,
                        verbose_name="Страна",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        help_text="Укажите город", max_length=100, verbose_name="Город"
                    ),
                ),
                (
                    "street",
                    models.CharField(
                        help_text="Укажите улица", max_length=100, verbose_name="Улица"
                    ),
                ),
                (
                    "building_number",
                    models.CharField(
                        help_text="Укажите номер дома",
                        max_length=10,
                        verbose_name="Номер дома",
                    ),
                ),
            ],
            options={
                "verbose_name": "Контакт",
                "verbose_name_plural": "Контакты",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "product_name",
                    models.CharField(
                        help_text="Укажите название продукта",
                        max_length=255,
                        verbose_name="Название продукта",
                    ),
                ),
                (
                    "product_model",
                    models.CharField(
                        help_text="Укажите модель продукта",
                        max_length=255,
                        verbose_name="Модель продукта",
                    ),
                ),
                (
                    "release_date",
                    models.DateField(
                        help_text="Укажите дату выпуска", verbose_name="Дата выпуска"
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["product_name"],
            },
        ),
        migrations.CreateModel(
            name="Node",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Укажите название",
                        max_length=255,
                        verbose_name="Название",
                    ),
                ),
                (
                    "level",
                    models.IntegerField(
                        choices=[
                            (0, "Завод"),
                            (1, "Розничная сеть"),
                            (2, "Индивидуальный предприниматель"),
                        ],
                        help_text="Выберете уровень сети",
                        verbose_name="Уровень сети",
                    ),
                ),
                (
                    "debt_to_supplier",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        help_text="Укажите задолженность, с точностью до копеек",
                        max_digits=10,
                        verbose_name="Задолженность",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        null=True,
                        verbose_name="Дата и время создания",
                    ),
                ),
                (
                    "contact",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите контакты данные",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_contacts",
                        to="network.contact",
                        verbose_name="Контакты",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите поставщика",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="network.node",
                        verbose_name="Поставщик",
                    ),
                ),
                (
                    "product",
                    models.ManyToManyField(
                        help_text="Укажите продукт",
                        related_name="%(class)s_products",
                        to="network.product",
                        verbose_name="Продукты",
                    ),
                ),
            ],
            options={
                "verbose_name": "Звено сети",
                "verbose_name_plural": "Звенья сети",
            },
        ),
    ]
