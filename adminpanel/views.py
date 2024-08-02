from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm,ArticleForm
from django.contrib import messages
from vendor.models import SellerRequest
from django.shortcuts import redirect, get_object_or_404
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
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'محصول با موفقیت ثبت شد.')
            return redirect('adminpanel:add_product')  # یا صفحه‌ای دیگر که تمایل دارید پس از افزودن محصول به آن منتقل شوید.
    else:
        form = ProductForm()

    return render(request, 'adminpanel/product/add_product.html', {'form': form})



#اضافه کردن محصول
@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
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
    # بازگشت به لیست درخواست‌ها
    return redirect('adminpanel:seller-requests-list')

def reject_request(request, pk):
    # دریافت درخواست مشخص شده
    seller_request = get_object_or_404(SellerRequest, pk=pk)
    # تغییر وضعیت به رد شده
    seller_request.status = 'rejected'
    seller_request.save()
    # بازگشت به لیست درخواست‌ها
    return redirect('adminpanel:seller-requests-list')
