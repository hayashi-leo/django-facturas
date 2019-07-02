from django.shortcuts import render

from products.models import Product
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    '''
    View for dashboard home page
    '''
    num_products = Product.objects.all().count()

    num_products += 1
    context = {
        'num_products': num_products,
    }

    return render(request, 'dashboard/home.html', context)

