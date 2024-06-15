from django.urls import path
from .views import Admin_view,product_create_view,page_1

app_name = 'adminpanel'
urlpatterns = [
    path('', Admin_view, name='adminpanel_home'),
    path('add_product/', product_create_view, name='add_product'),

]