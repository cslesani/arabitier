from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
# accounts/views.py


@login_required
def Admin_view(request):
    return render(request, 'adminpanel/adminindex.html')
