from django.urls import path
from . import views

urlpatterns = [
    path("", views.store_index, name="store"),


]
