from django.urls import path
from . import views

urlpatterns = [
    path("", views.Articlindex, name="article"),
    path('article_detail/<int:article_id>/', views.article_detail, name='article_detail'),
]
