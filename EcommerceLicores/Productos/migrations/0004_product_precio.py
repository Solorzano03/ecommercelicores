# Generated by Django 4.0 on 2022-12-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0003_product_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='precio'),
        ),
    ]
