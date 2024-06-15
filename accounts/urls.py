# accounts/urls.py
from django.urls import path
from .views import user_dashboard

"""urlpatterns = [
    path('login/', user_dashboard, name='nafis_login'),
]"""
# urls.py
from django.urls import path
from .views import UserLoginView, AdminLoginView, admin_dashboard, user_dashboard, dashboard_redirect,logout_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('user/login/', UserLoginView.as_view(), name='user_login'),
    path('adminpage/login/', AdminLoginView.as_view(), name='admin_login'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', logout_user, name='logout'),
    path('redirect/', dashboard_redirect, name='dashboard_redirect'),
]


