from django.shortcuts import render

# Create your views here.
def ruleslindex(request):
    from cart.models import CartItem  # واردات داخل تابع
    countcart = CartItem.objects.filter(cart__user=request.user).count()
    return render(request, 'rules/rulesindex.html',{'countcart':countcart})