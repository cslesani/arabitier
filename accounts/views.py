# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied

def user_is_admin(user):
    if user.is_authenticated and user.is_superuser:
        return True
    raise PermissionDenied

def user_is_not_admin(user):
    if user.is_authenticated and not user.is_superuser:
        return True
    raise PermissionDenied

class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/loginindex.html'
    authentication_form =LoginForm

    def get_success_url(self):
        return reverse_lazy('user_dashboard')

class AdminLoginView(auth_views.LoginView):
    template_name = 'accounts/loginindex.html'
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy('admin_dashboard')

@login_required
@user_passes_test(user_is_admin)
def admin_dashboard(request):
    return render(request, 'adminpanel/adminindex.html')

@login_required
@user_passes_test(user_is_not_admin)
def user_dashboard(request):
    return render(request, 'userpanel/useindex.html')

def dashboard_redirect(request):
    if request.user.is_superuser:
        return redirect('admin_dashboard')
    else:
        return redirect('user_dashboard')

def logout_user(request):
    return redirect('main-view')

"""def Login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:

                login(request, user)
                return redirect('adminpanel')  # آدرس پنل شخصی‌سازی شده
            else:
                form.add_error(None, 'نام کاربری یا رمز عبور اشتباه است')
    else:
        form = LoginForm()
    return render(request, 'accounts/loginindex.html', {'form': form})"""
