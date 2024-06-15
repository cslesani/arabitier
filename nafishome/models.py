from django.db import models


# Create your models here.

class Product(models.Model):
    #artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_brandname = models.CharField(max_length=100,default='')
    product_contry = models.CharField(max_length=100,default='ایران')
    product_number = models.IntegerField()
    product_price = models.IntegerField(default=0)
    product_stock = models.IntegerField(default=0)
    product_view=models.IntegerField(default=0)
    product_width=models.IntegerField(default=0)
    product_Diameter=models.IntegerField(default=0)
    product_layer=models.IntegerField(default=0)
    product_weight=models.IntegerField(default=0)
    product_speed=models.IntegerField(default=0)
    product_discountpercent_total=models.IntegerField(default=0)
    product_discountpercent_this = models.IntegerField(default=0)
    product_discount_price = models.IntegerField(default=0)
    product_profitpercent = models.IntegerField(default=0)
    product_price_final = models.IntegerField(default=0)
    product_type=models.CharField(max_length=100,default='سواری')
    product_image = models.ImageField(blank=True,upload_to='product/')



