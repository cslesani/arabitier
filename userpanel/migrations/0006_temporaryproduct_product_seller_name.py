# Generated by Django 5.0.6 on 2024-08-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpanel', '0005_remove_temporaryproduct_seller_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporaryproduct',
            name='product_seller_name',
            field=models.CharField(default='مدیر اصلی', max_length=300),
        ),
    ]
