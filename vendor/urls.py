from django.urls import path
from .views import seller_request_view

urlpatterns = [
    path('seller-request/', seller_request_view, name='seller_request'),
]
