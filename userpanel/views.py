from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from cart.models import Order
from .models import UserProfile
from .forms import UserProfileForm


# Create your views here.
# accounts/views.py


@login_required
def Admin_view(request):
    return render(request, 'userpanel/useindex.html')

@login_required
def user_orders(request):
    from cart.models import CartItem  # واردات داخل تابع
    countcart = CartItem.objects.filter(cart__user=request.user).count()
    orders = Order.objects.filter(user=request.user)
    return render(request, 'userpanel/orders.html', {'orders': orders,'countcart':countcart})



def address_profile(request):
    from cart.models import CartItem  # واردات داخل تابع
    countcart = CartItem.objects.filter(cart__user=request.user).count()
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_dashboard')  # مسیر مناسب برای نمایش پروفایل کاربر
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'userpanel/address.html', {'form': form,'countcart':countcart})


"""def user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'userpanel/profile.html', {'user_profile': user_profile})"""

