from django.urls import path
from .views import add_to_cart, view_cart, remove_from_cart,create_order,payment_gateway
from .views import get_cart_item_count

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
    path('create_order/', create_order, name='create_order'),
    path('payment_gateway/<str:order_number>/', payment_gateway, name='payment_gateway'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('get_cart_item_count/', get_cart_item_count, name='get_cart_item_count'),

]
