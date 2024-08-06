from django import forms
from .models import Product
from django import forms
from .models import Review,Inseam



class ProductSearchForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_brandname', 'product_model', 'product_car_type', 'product_create_year', 'product_width']
        widgets = {
            'product_brandname': forms.Select(attrs={'class': 'border border-zinc-300 w-11/12 mx-auto rounded-xl p-2 text-zinc-500 outline-none'}),
            'product_model': forms.Select(attrs={'class': 'border border-zinc-300 w-11/12 mx-auto rounded-xl p-2 text-zinc-500 outline-none'}),
            'product_car_type': forms.Select(attrs={'class': 'border border-zinc-300 w-11/12 mx-auto rounded-xl p-2 text-zinc-500 outline-none'}),
            'product_create_year': forms.Select(attrs={'class': 'border border-zinc-300 w-11/12 mx-auto rounded-xl p-2 text-zinc-500 outline-none'}),
            'product_width': forms.Select(attrs={'class': 'border border-zinc-300 w-11/12 mx-auto rounded-xl p-2 text-zinc-500 outline-none'}),
        }

# forms.py

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['optional_name','rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 4}),
        }


class InseamForm(forms.ModelForm):
    class Meta:
        model = Inseam
        fields = ['value']  # یا هر فیلدی که نیاز دارید