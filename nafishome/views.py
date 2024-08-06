from django.shortcuts import render,redirect, get_object_or_404
from article.models import Article
from .forms import ProductSearchForm
from .models import Product, Review
from .forms import ReviewForm
from nafishome.models import Width,Diameter,Inseam



from django.http import HttpResponse
from django.template import loader
# Create your views here.


def success_page(request):
    from cart.models import CartItem
    if request.user.is_authenticated:
        countcart = CartItem.objects.filter(cart__user=request.user).count()
    return render(request, 'success.html',{'countcart': countcart})


def index(request):
    inseams = Inseam.objects.all()
    widths = Width.objects.all()
    diameters = Diameter.objects.all()
    data = Product.objects.all()
    articleindexdata = Article.objects.all().order_by('-id')[:4]

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

        if request.method == 'POST':
            form = ProductSearchForm(request.POST)
            if form.is_valid():
                products = Product.objects.filter(
                    brand=form.cleaned_data['product_brandname'],
                    model=form.cleaned_data['product_model'],
                    type=form.cleaned_data['product_car_type'],
                    year=form.cleaned_data['product_create_year'],
                    size=form.cleaned_data['product_width']
                )
                return render(request, 'product_search_results.html', {'form': form, 'products': products})
        else:
            form = ProductSearchForm()

    return render(request, 'index.html', {'data': data, 'articleindexdata': articleindexdata, 'countcart': countcart,'form': form,'inseams': inseams,'widths': widths,'diameters': diameters})

def product_detail(request, product_id):
    from cart.models import CartItem
    if request.user.is_authenticated:
        countcart = CartItem.objects.filter(cart__user=request.user).count()
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()
    review_count = reviews.count()
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', product_id=product.id)

    context = {
        'countcart':countcart,
        'product': product,
        'reviews': reviews,
        'review_count': review_count,
        'form': form
    }
    return render(request, 'product_detail.html', context)

#search
def product_search(request):
    print("Width:", request.GET.get('width'))
    print("Diameter:", request.GET.get('diameter'))
    print("Inseam:", request.GET.get('inseam'))

    products = Product.objects.all()

    # دریافت مقادیر از فرم
    width = request.GET.get('width')
    diameter = request.GET.get('diameter')
    inseam = request.GET.get('inseam')

    # اعمال فیلترها
    if width:
        products = products.filter(product_width=width)
    if diameter:
        products = products.filter(product_Diameter=diameter)  # توجه به نام فیلد با حرف بزرگ D
    if inseam:
        products = products.filter(product_view=inseam)

    return render(request, 'product_tier_list.html', {'products': products})

