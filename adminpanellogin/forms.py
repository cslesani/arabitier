# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input',  # کلاس CSS برای هماهنگی با قالب
            'id': 'id_username',    # id برای مطابقت با قالب
            'placeholder': 'نام کاربری خود را وارد کنید',  # Placeholder برای ورودی
        }),
        label="نام کاربری",  # برچسب فیلد
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',  # کلاس CSS برای هماهنگی با قالب
            'id': 'id_password',    # id برای مطابقت با قالب
            'placeholder': 'رمز عبور خود را وارد کنید',  # Placeholder برای ورودی
        }),
        label="رمز عبور",  # برچسب فیلد
    )
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-checkbox rounded',  # کلاس CSS برای هماهنگی با قالب
            'id': 'checkbox-signin',  # id برای مطابقت با قالب
        }),
        label="مرا به خاطر بسپار",  # برچسب چک‌باکس
    )
