from django.db import models
from django.contrib.auth.models import User

class SellerRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'در حال بررسی'),
        ('approved', 'تایید شده'),
        ('rejected', 'رد شده'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()  # فیلد تاریخ تولد
    business_name = models.CharField(max_length=100)
    description = models.TextField()

    # فیلدهای آپلود فایل
    business_license = models.ImageField(upload_to='image/vendor/business_licenses/')
    national_id_card = models.ImageField(upload_to='image/vendor/national_id_cards/')
    shop_photo = models.ImageField(upload_to='image/vendor/shop_photos/')
    address = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  # فیلد وضعیت

    def __str__(self):
        return f'{self.full_name} - {self.business_name}'
