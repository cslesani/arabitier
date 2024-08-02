from django import forms
from nafishome.models import Product
from article.models import Article

class ProductForm(forms.ModelForm):
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


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['article_title', 'article_message', 'article_author','article_date','article_image']
