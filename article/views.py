from django.shortcuts import render
from .models import Article
# Create your views here.
def Articlindex(request):
    dataarticle = Article.objects.all()
    from cart.models import CartItem  # واردات داخل تابع
    countcart = CartItem.objects.filter(cart__user=request.user).count()

    return render(request, 'article/index.html', {'dataarticle': dataarticle,'countcart':countcart})