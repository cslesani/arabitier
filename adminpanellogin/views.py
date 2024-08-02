# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AdminLoginForm
from django.contrib.auth import logout
from django.shortcuts import redirect

def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')  # یا هر صفحه‌ی دیگری که برای ادمین در نظر دارید

    if request.method == 'POST':
        form = AdminLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_staff:  # بررسی اینکه کاربر ادمین است
                login(request, user)
                messages.success(request, 'محصول با موفقیت ثبت شد.')
                return redirect('admin_dashboard')
            else:
                messages.error(request, 'نام کاربری یا رمز عبور اشتباه است یا شما ادمین نیستید.')
        else:
            messages.error(request, 'فرم نامعتبر است.')
    else:
        form = AdminLoginForm()

    return render(request, 'adminpanellogin/index.html', {'form': form})




"""def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('admin_login')  # اگر کاربر ادمین نبود، به صفحه لاگین ادمین هدایت شود
    # کدهای دیگر برای نمایش داشبورد ادمین
    return render(request, 'admin_dashboard.html')"""




def admin_logout(request):
    # خروج کاربر از وضعیت ادمین
    logout(request)
    # ریدایرکت به صفحه ورود یا هر صفحه دیگری که شما تمایل دارید
    return redirect('admin_login')