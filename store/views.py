from django.shortcuts import render,redirect, get_object_or_404
from nafishome.models import Product
from article.models import Article



from django.http import HttpResponse
from django.template import loader
# Create your views here.




def store_index(request):
    data = Product.objects.all()

    countcart = 0  # مقدار پیش‌فرض برای شمارش آیتم‌های سبد خرید
    from cart.models import CartItem
    if request.user.is_authenticated:
        countcart = CartItem.objects.filter(cart__user=request.user).count()

    # محاسبه با سود
    for p in data:
        profit_percent = p.product_profitpercent / 100
        profit_price = int(p.product_price + (p.product_price * profit_percent))
        p.product_price_final = profit_price

    # محاسبه با تخفیف
    for p in data:
        if p.product_discountpercent_total > 0:
            discount_percent = p.product_discountpercent_total / 100
            discounted_price = int(p.product_price_final - (p.product_price_final * discount_percent))
            p.product_discount_price = discounted_price
        else:
            p.product_discount_price = None

        if p.product_discountpercent_this > 0 and p.product_discount_price is None:
            discount_percent_this = p.product_discountpercent_this / 100
            discounted_price_this = int(p.product_price_final - (p.product_price_final * discount_percent_this))
            p.product_discount_price = discounted_price_this

        elif p.product_discountpercent_this > 0 and p.product_discount_price is not None:
            discount_percent_this = p.product_discountpercent_this / 100
            discounted_price_this = int(p.product_discount_price - (p.product_discount_price * discount_percent_this))
            p.product_discount_price = discounted_price_this

        elif p.product_discountpercent_total == 0 and p.product_discountpercent_this == 0:
            p.product_discount_price = None

    return render(request, 'store/storeindex.html', {'data': data,  'countcart': countcart})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})