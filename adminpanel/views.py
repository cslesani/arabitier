from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from nafishome.models import Product
from .serializers import ProductSerializer
from .forms import ProductForm
# Create your views here.
# accounts/views.py


@login_required
def Admin_view(request):
    return render(request, 'adminpanel/adminindex.html')

"""@api_view(['POST'])
def add_product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""


from .forms import ProductForm

def product_create_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminpanel')  # جایگزین کنید با URL مناسب
    else:
        form = ProductForm()
    return render(request, 'adminpanel/product/add_product.html', {'form': form})


@login_required
def page_1(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminpanel')  # جایگزین کنید با URL مناسب
    else:
        form = ProductForm()
    return render(request, 'adminpanel/product/add_product.html', {'form': form})

@login_required
def page_2(request):
    return render(request, 'dashboard/page_2.html')