# Generated by Django 5.0.6 on 2024-08-05 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nafishome', '0019_product_seller_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='seller_name',
        ),
    ]
