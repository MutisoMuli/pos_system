# Generated by Django 5.0 on 2024-10-17 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0009_remove_product_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="product",
            name="barcode",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="buying_price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="product",
            name="stock_quantity",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="product",
            name="unit",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="subcategory",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
