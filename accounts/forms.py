# accounts/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


# accounts/forms.py




class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user