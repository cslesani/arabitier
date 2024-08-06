from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="main-view"),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('success/', views.success_page, name='success_page'),
    path('search/', views.product_search, name='product_search'),



]
