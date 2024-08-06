from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm,ArticleForm
from django.contrib import messages
from vendor.models import SellerRequest
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from nafishome.models import Inseam,Product
from userpanel.models import TemporaryProduct
from .models import SellerProduct



# Create your views here.
# accounts/views.py


@login_required
def Admin_view(request):
    return render(request, 'adminpanel/adminindex.html')


def product_create_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminpanel')  # جایگزین کنید با URL مناسب
    else:
        form = ProductForm()
    return render(request, 'adminpanel/product/add_product.html', {'form': form})

#اضافه کردن محصول
@login_required
def add_product(request):
    aspect_ratios = Inseam.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # اضافه کردن request.FILES
        if form.is_valid():
            form.save()
            messages.success(request, 'محصول با موفقیت ثبت شد.')
            return redirect('adminpanel:add_product')  # یا صفحه‌ای دیگر که تمایل دارید پس از افزودن محصول به آن منتقل شوید.
    else:
        form = ProductForm()

    return render(request, 'adminpanel/product/add_product.html', {'form': form, 'aspect_ratios': aspect_ratios})




#اضافه کردن محصول
@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'مقاله با موفقیت ثبت شد.')
            return redirect('adminpanel:add_article')  # یا صفحه‌ای دیگر که تمایل دارید پس از افزودن محصول به آن منتقل شوید.
    else:
        form = ArticleForm()

    return render(request, 'adminpanel/Weblog/add_article.html', {'form': form})


#نمایش درخواست فروشنده

def seller_request_list_view(request):
    # دریافت تمام درخواست‌های ثبت‌شده
    requests = SellerRequest.objects.all()

    # ارسال اطلاعات به قالب
    context = {
        'requests': requests,  # لیست تمام درخواست‌ها
    }
    return render(request, 'adminpanel/vendor_request/show_request.html', context)


def approve_request(request, pk):
    # دریافت درخواست مشخص شده
    seller_request = get_object_or_404(SellerRequest, pk=pk)
    # تغییر وضعیت به تایید شده
    seller_request.status = 'approved'
    seller_request.save()
    return redirect('adminpanel:seller-requests-list')

def reject_request(request, pk):
    # دریافت درخواست مشخص شده
    seller_request = get_object_or_404(SellerRequest, pk=pk)
    # تغییر وضعیت به رد شده
    seller_request.status = 'rejected'
    seller_request.save()
    # بازگشت به لیست درخواست‌ها
    return redirect('adminpanel:seller-requests-list')


#نمایش محصولات وارد شده توسط فروشنده ها

def approve_products(request):
    products = TemporaryProduct.objects.all()
    return render(request, 'adminpanel/vendor_request/show_product_vendor_add.html', {'products': products})


def approve_product(request, pk):
    tempproduct = get_object_or_404(TemporaryProduct, pk=pk)

    # انتقال داده‌ها از TemporaryProduct به Product
    main_product=Product.objects.create(
        product_name=tempproduct.product_name,
        product_brandname=tempproduct.product_brandname,
        product_price=tempproduct.product_price,
        product_image=tempproduct.product_image,
        product_contry=tempproduct.product_contry,
        product_number=tempproduct.product_number,
        product_stock=tempproduct.product_stock,
        product_view=tempproduct.product_view,
        product_width=tempproduct.product_width,
        product_Diameter=tempproduct.product_Diameter,
        product_layer=tempproduct.product_layer,
        product_weight=tempproduct.product_weight,
        product_speed=tempproduct.product_speed,
        product_discountpercent_total=tempproduct.product_discountpercent_total,
        product_discountpercent_this=tempproduct.product_discountpercent_this,
        product_discount_price=tempproduct.product_discount_price,
        product_profitpercent=tempproduct.product_profitpercent,
        product_price_final=tempproduct.product_price_final,
        product_type=tempproduct.product_type,
        product_car_type=tempproduct.product_type,
        product_model=tempproduct.product_model,
        product_garanty_year=tempproduct.product_garanty_year,
        product_create_year=tempproduct.product_create_year,

    )

    seller = User.objects.get(username=tempproduct.product_seller_name)
    SellerProduct.objects.create(
        seller=seller,
        product=main_product
    )
    # حذف رکورد از پایگاه داده موقت
    tempproduct.delete()

    messages.success(request, 'محصول با موفقیت تأیید شد و به پایگاه داده اصلی منتقل شد.')
    return redirect('adminpanel:approve_products')  #