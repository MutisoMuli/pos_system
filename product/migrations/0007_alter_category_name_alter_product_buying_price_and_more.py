# Generated by Django 5.0 on 2024-10-17 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0006_alter_product_buying_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="product",
            name="buying_price",
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name="subcategory",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="product.category"
            ),
        ),
        migrations.AlterField(
            model_name="subcategory",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
