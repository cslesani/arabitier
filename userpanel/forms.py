from django import forms
from .models import UserProfile,TemporaryProduct
from nafishome.models import Inseam,Width,Diameter

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


class TemporaryProductForm(forms.ModelForm):
    product_view = forms.ChoiceField(
        choices=[(inseam.value, inseam.value) for inseam in Inseam.objects.all()],
        label="فاق"
    )
    product_width = forms.ChoiceField(
        choices=[(width.value, width.value) for width in Width.objects.all()],
        label="عرض"
    )
    product_Diameter = forms.ChoiceField(
        choices=[(diameter.value, diameter.value) for diameter in Diameter.objects.all()],
        label="عرض"
    )
    class Meta:
        model = TemporaryProduct
        fields = [
            'product_name', 'product_brandname', 'product_contry', 'product_number',
            'product_price', 'product_stock', 'product_view', 'product_width',
            'product_Diameter', 'product_layer', 'product_weight', 'product_speed',
            'product_discountpercent_total', 'product_discountpercent_this',
            'product_discount_price', 'product_profitpercent', 'product_price_final',
            'product_type', 'product_car_type', 'product_model', 'product_garanty_year',
            'product_create_year', 'product_image'
        ]
