from django.db import models
from nafishome.models import Product
from django.contrib.auth.models import User
# Create your models here.

class SellerProduct(models.Model):
    seller = models.CharField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.seller.username} - {self.product.product_name}"