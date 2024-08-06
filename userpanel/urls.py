from django.urls import path
from .views import Admin_view,user_orders,address_profile,add_product_vendor
urlpatterns = [
    path('', Admin_view, name='userpanel'),
    path('orders/', user_orders, name='user_orders'),
    path('user_address/',address_profile, name='user_address'),
    path('add_product_vendor/',add_product_vendor, name='add_product_vendor'),



]