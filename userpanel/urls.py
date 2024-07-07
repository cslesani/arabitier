from django.urls import path
from .views import Admin_view,user_orders,address_profile
urlpatterns = [
    path('', Admin_view, name='userpanel'),
    path('orders/', user_orders, name='user_orders'),
    path('user_address/',address_profile, name='user_address'),

]