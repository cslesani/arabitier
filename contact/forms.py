# forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-700 outline-none transition-all focus:border-red-300'}),
            'email': forms.EmailInput(attrs={'class': 'text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-700 outline-none transition-all focus:border-red-300'}),
            'description': forms.Textarea(attrs={'class': 'text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-700 outline-none transition-all focus:border-red-300', 'cols': 20, 'rows': 7}),
        }
