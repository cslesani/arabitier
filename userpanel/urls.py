from django.urls import path
from .views import Admin_view
urlpatterns = [
    path('', Admin_view, name='userpanel'),
]