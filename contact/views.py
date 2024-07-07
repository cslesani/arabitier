from django.shortcuts import render

# Create your views here.
def contactlindex(request):
    from cart.models import CartItem  # واردات داخل تابع
    countcart = CartItem.objects.filter(cart__user=request.user).count()
    return render(request, 'contact/contactindex.html',{'countcart':countcart})

# views.py
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    from cart.models import CartItem  # واردات داخل تابع
    countcart = CartItem.objects.filter(cart__user=request.user).count()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main-view')  # پس از ذخیره اطلاعات به صفحه موفقیت هدایت می‌شود
    else:
        form = ContactForm()
    return render(request, 'contact/contactindex.html', {'form': form,'countcart':countcart})
