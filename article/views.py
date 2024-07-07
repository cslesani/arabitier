from django.shortcuts import render, get_object_or_404
from .models import Article
# Create your views here.
def Articlindex(request):
    dataarticle = Article.objects.all()
    from cart.models import CartItem  # واردات داخل تابع
    countcart = CartItem.objects.filter(cart__user=request.user).count()

    return render(request, 'article/index.html', {'dataarticle': dataarticle,'countcart':countcart})


def article_detail(request, article_id):

    dataarticledetailtotal = Article.objects.all().order_by('-id')[:4]
    from cart.models import CartItem  # واردات داخل تابع
    countcart = CartItem.objects.filter(cart__user=request.user).count()
    article_detail = get_object_or_404(Article, id=article_id)
    return render(request, 'article/article_detail.html', {'article_detail':article_detail,'dataarticledetailtotal': dataarticledetailtotal,'countcart':countcart})