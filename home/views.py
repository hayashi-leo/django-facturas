from django.shortcuts import render
from dashboard import views as dashboard_views
from products import views as products_views

# Create your views here.

def home_page(request):
    context = {
        'title': 'Hello World',
        'content': 'Welcome to the homepage',
    }

    # user.is_authenticated() as function has been dropped in django 2.0
    if request.user.is_authenticated:
        #return dashboard_views.home(request)
        return products_views.product_list(request)

    return render(request, 'home_page.html', context)

