# Generated by Django 5.0.3 on 2024-03-10 07:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=250, unique=True)),
                ("slug", models.SlugField(max_length=250, unique=True)),
                ("description", models.TextField(blank=True)),
                ("image", models.ImageField(blank=True, upload_to="Category")),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
                "ordering": ("name",),
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
                ("name", models.CharField(max_length=250, unique=True)),
                ("slug", models.SlugField(max_length=250, unique=True)),
                ("description", models.TextField(blank=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("image", models.ImageField(blank=True, upload_to="Product")),
                ("stock", models.IntegerField()),
                ("available", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.category"
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
                "ordering": ("name",),
            },
        ),
    ]
