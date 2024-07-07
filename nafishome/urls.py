from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="main-view"),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),

]
