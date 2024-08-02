from django import forms
from .models import SellerRequest

class SellerRequestForm(forms.ModelForm):
    class Meta:
        model = SellerRequest
        fields = ['full_name', 'phone_number', 'date_of_birth', 'business_name', 'description',
                  'business_license', 'national_id_card', 'shop_photo', 'address']

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-700 outline-none transition-all focus:border-red-300'}),
            'phone_number': forms.TextInput(attrs={
                'class': 'text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-700 outline-none transition-all focus:border-red-300'}),
            'business_name': forms.TextInput(attrs={
                'class': 'text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-700 outline-none transition-all focus:border-red-300'}),
            'business_license':forms.FileInput(attrs={
                'class' :'block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-700 outline-none transition-all focus:border-red-300'}),
            'national_id_card': forms.FileInput(attrs={
                'class': 'block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-700 outline-none transition-all focus:border-red-300'}),
            'shop_photo': forms.FileInput(attrs={
                'class': 'block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-700 outline-none transition-all focus:border-red-300'}),


            'date_of_birth': forms.DateInput(attrs={'type': 'date','class': 'text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-700 outline-none transition-all focus:border-red-300'}),  # ویجت برای انتخاب تاریخ تولد
            'address': forms.Textarea(attrs={
                'class': 'text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-700 outline-none transition-all focus:border-red-300',
                'cols': 20, 'rows': 7}),
            'description': forms.Textarea(attrs={
                'class': 'text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-700 outline-none transition-all focus:border-red-300',
                'cols': 20, 'rows': 7}),
        }

    def clean_business_license(self):
        business_license = self.cleaned_data.get('business_license')
        if business_license:
            if business_license.size > 2 * 1024 * 1024:  # محدودیت حجم فایل (2 مگابایت)
                raise forms.ValidationError("حجم فایل جواز کسب نباید بیشتر از 2 مگابایت باشد.")
        return business_license
