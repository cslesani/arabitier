from django import forms
from nafishome.models import Product
from article.models import Article
from nafishome.models import Inseam,Width,Diameter


class ProductForm(forms.ModelForm):
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
        model = Product
        fields = [
            'product_name', 'product_brandname', 'product_contry', 'product_number',
            'product_price', 'product_stock', 'product_view', 'product_width',
            'product_Diameter', 'product_layer', 'product_weight', 'product_speed',
            'product_discountpercent_total', 'product_discountpercent_this',
            'product_discount_price', 'product_profitpercent', 'product_price_final',
            'product_type','product_car_type','product_model','product_garanty_year',
            'product_create_year', 'product_image'
        ]
        #product_view = forms.ModelChoiceField(queryset=Inseam.objects.all(), label="فاق")




class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['article_title', 'article_message', 'article_author','article_date','article_image']
