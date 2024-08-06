from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username

from django.db import models

class TemporaryProduct(models.Model):
    product_name = models.CharField(max_length=200)
    product_brandname = models.CharField(max_length=100, default='')
    product_contry = models.CharField(max_length=100, default='ایران')
    product_number = models.IntegerField()
    product_price = models.IntegerField(default=0)
    product_stock = models.IntegerField(default=0)
    product_view = models.IntegerField(default=0)
    product_width = models.IntegerField(default=0)
    product_Diameter = models.FloatField(default=0)
    product_layer = models.IntegerField(default=0)
    product_weight = models.IntegerField(default=0)
    product_speed = models.IntegerField(default=0)
    product_discountpercent_total = models.IntegerField(default=0)
    product_discountpercent_this = models.IntegerField(default=0)
    product_discount_price = models.IntegerField(default=0)
    product_profitpercent = models.IntegerField(default=0)
    product_price_final = models.IntegerField(default=0)
    product_type = models.CharField(max_length=100, default='سواری')
    product_car_type = models.CharField(max_length=100, default='پژو')
    product_model = models.CharField(max_length=100, default='206')
    product_garanty_year = models.IntegerField(default=0)
    product_create_year = models.IntegerField(default=0)
    product_seller_name=models.CharField(max_length=300, default='مدیر اصلی')
    product_image = models.ImageField(upload_to='temporary_products/')

    def __str__(self):
        return self.product_name

