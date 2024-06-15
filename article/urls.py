from django.urls import path
from . import views

urlpatterns = [
    path("", views.Articlindex, name="article"),
]
