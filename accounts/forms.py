# accounts/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        label='نام کاربری یا ایمیل',
        widget=forms.TextInput(attrs={
            'class': 'focus:shadow-primary-outline text-sm leading-5.6 block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-3 font-normal text-gray-700 outline-none transition-all focus:border-red-300 focus:outline-none',
            'placeholder': 'شماره موبایل یا ایمیل خود را وارد کنید'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'focus:shadow-primary-outline text-sm leading-5.6 block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-3 font-normal text-gray-700 outline-none transition-all focus:border-red-300 focus:outline-none',
            'placeholder': 'رمز عبور خود را وارد کنید'
        }),
        label='رمز عبور'
    )
