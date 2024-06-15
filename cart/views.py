from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem
import jdatetime
from .models import Cart, CartItem, Order, OrderItem
from django.http import JsonResponse

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

"""@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    countcart = CartItem.objects.filter(cart__user=request.user).count()
    if not cart_items.exists():
        return render(request, 'cart/empty_cart.html')
    else:
        return render(request, 'cart/view_cart.html', {'cart_items': cart_items,'countcart':countcart})"""


@login_required
def view_cart(request):
    total_price = 0
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    countcart = CartItem.objects.filter(cart__user=request.user).count()
    current_date_jalali = jdatetime.datetime.now().strftime('%Y/%m/%d')
    if not cart_items.exists():
        return render(request, 'cart/empty_cart.html')
    else:
        products_in_cart = []
        for item in cart_items:
            product = item.product
            product_info = {
                'id': product.id,
                'name': product.product_name,
                'brand': product.product_brandname,
                'contry': product.product_contry,
                'number': product.product_number,
                'price': product.product_price,
                'stock': product.product_stock,
                'view': product.product_view,
                'width': product.product_width,
                'diameter': product.product_Diameter,
                'layer': product.product_layer,
                'weight': product.product_weight,
                'speed': product.product_speed,
                'discountpercent_total': product.product_discountpercent_total,
                'discountpercent_this': product.product_discountpercent_this,
                'discount_price': product.product_discount_price,
                'profitpercent': product.product_profitpercent,
                'price_final': product.product_price_final,
                'type': product.product_type,
                'image': product.product_image.url if product.product_image else None,
                'quantity': item.quantity,

                # اضافه کردن سایر فیلدهای مورد نیاز از مدل Product
            }
            products_in_cart.append(product_info)
            total_price += product.product_price * item.quantity

        context = {
            'products_in_cart': products_in_cart,
            'countcart': countcart,
            'total_price': total_price,
            'current_date_jalali': current_date_jalali,
        }

        return render(request, 'cart/view_cart.html', context)



@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if cart_item.cart.user == request.user:
        cart_item.delete()
    return redirect('view_cart')


@login_required
def create_order(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    if request.method == 'POST':
        order = Order.objects.create(user=request.user,
                                     total_price=sum(item.product.product_price * item.quantity for item in cart_items))

        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity,
                                     price=item.product.product_price)

        cart_items.delete()

        # Redirect to payment gateway
        return redirect('payment_gateway', order_number=order.order_number)

    return render(request, 'cart/checkout.html', {'cart_items': cart_items, 'total_price': sum(
        item.product.product_price * item.quantity for item in cart_items)})

@login_required
def payment_gateway(request, order_number):
    order = Order.objects.get(order_number=order_number)
    # اطلاعات مورد نیاز برای اتصال به درگاه پرداخت را تنظیم کنید
    # این بخش به درگاه پرداخت خاصی که استفاده می‌کنید بستگی دارد
    return render(request, 'cart/payment_gateway.html', {'order': order})


def get_cart_item_count(request):
    # دریافت تعداد محصولات موجود در سبد خرید
    count = CartItem.objects.filter(cart__user=request.user).count()
    # برگرداندن تعداد به صورت JSON
    return JsonResponse({'count': count})
