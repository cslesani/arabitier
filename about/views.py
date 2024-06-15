from django.shortcuts import render

# Create your views here.
def aboutlindex(request):
    from cart.models import CartItem  # واردات داخل تابع
    countcart = CartItem.objects.filter(cart__user=request.user).count()
    return render(request, 'abouttemplate/abloutindex.html',{'countcart':countcart})