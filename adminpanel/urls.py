from django.urls import path
from .views import *

app_name = 'adminpanel'
urlpatterns = [
    path('', Admin_view, name='adminpanel_home'),
    path('add_product/', add_product, name='add_product'),
    path('add_article/', add_article, name='add_article'),
    path('seller-requests/', seller_request_list_view, name='seller-requests-list'),
    path('approve-products/', approve_products, name='approve_products'),
    path('approve-product/<int:pk>/', approve_product, name='approve_product'),
    path('approve-request/<int:pk>/', approve_request, name='approve-request'),
    path('reject-request/<int:pk>/', reject_request, name='reject-request'),

]