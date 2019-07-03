from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product

# Create your views here.

@login_required(login_url='/') # redirect when user is not authenticated, in this case, the home_page
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'all_products':products})
