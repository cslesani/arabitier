from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from cart.models import Order
from .models import UserProfile
from .forms import UserProfileForm,TemporaryProductForm
from django.contrib import messages
from vendor.models import SellerRequest




# Create your views here.
# accounts/views.py


@login_required
def Admin_view(request):
    try:
        # بررسی وضعیت درخواست فروشنده کاربر
        seller_request = SellerRequest.objects.get(user=request.user, status='approved')
        is_seller = True
    except SellerRequest.DoesNotExist:
        is_seller = False

    return render(request, 'userpanel/useindex.html',{'is_seller':is_seller})

@login_required
def user_orders(request):
    try:
        # بررسی وضعیت درخواست فروشنده کاربر
        seller_request = SellerRequest.objects.get(user=request.user, status='approved')
        is_seller = True
    except SellerRequest.DoesNotExist:
        is_seller = False


    from cart.models import CartItem  # واردات داخل تابع
    countcart = CartItem.objects.filter(cart__user=request.user).count()
    orders = Order.objects.filter(user=request.user)
    return render(request, 'userpanel/orders.html', {'orders': orders,'countcart':countcart,'is_seller':is_seller})

def add_product_vendor(request):
    from cart.models import CartItem  # واردات داخل تابع
    countcart = CartItem.objects.filter(cart__user=request.user).count()
    try:
        # بررسی وضعیت درخواست فروشنده کاربر
        seller_request = SellerRequest.objects.get(user=request.user, status='approved')
        is_seller = True
    except SellerRequest.DoesNotExist:
        is_seller = False

    if request.method == 'POST':
        form = TemporaryProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.product_seller_name = request.user.username  # ثبت نام کاربری کاربر وارد شده
            product.save()
            messages.success(request, 'محصول با موفقیت ثبت شد و منتظر تایید مدیر است.')
            return redirect('add_product_vendor')  # یا مسیر دیگری که مناسب است
    else:
        form = TemporaryProductForm()

    return render(request, 'userpanel/add_product.html', {'form': form, 'is_seller': is_seller, 'countcart': countcart})

def address_profile(request):
    from cart.models import CartItem  # واردات داخل تابع
    countcart = CartItem.objects.filter(cart__user=request.user).count()

    try:
        # بررسی وضعیت درخواست فروشنده کاربر
        seller_request = SellerRequest.objects.get(user=request.user, status='approved')
        is_seller = True
    except SellerRequest.DoesNotExist:
        is_seller = False


    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_dashboard')  # مسیر مناسب برای نمایش پروفایل کاربر
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'userpanel/address.html', {'form': form,'countcart':countcart,'is_seller':is_seller})









"""def user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'userpanel/profile.html', {'user_profile': user_profile})"""

