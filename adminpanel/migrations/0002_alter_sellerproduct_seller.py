# Generated by Django 5.0.6 on 2024-08-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerproduct',
            name='seller',
            field=models.CharField(max_length=300),
        ),
    ]
