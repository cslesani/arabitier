from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'phone_number']
        labels = {
            'address': 'آدرس',
            'phone_number': 'شماره تلفن',
        }
        widgets = {
            'address': forms.TextInput(attrs={
                'class': 'text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-700 outline-none transition-all focus:border-red-300',
                'placeholder': 'آدرس خود را وارد کنید',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-700 outline-none transition-all focus:border-red-300',
                'placeholder': 'شماره تلفن خود را وارد کنید',
            }),
        }
