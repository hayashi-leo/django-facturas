from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.utils import timezone
from .forms import ProductForm, NewProductForm, EditProductForm

# Create your views here.

LOGIN_URL = '/' # redirect to this URL when user is not authenticated, in our case, the home_page

all_units_of_measure = (
    'Set', 'Roll', 'Square', 'Meter',
    'Bag', 'Box', 'Dozen', 'Half Dozen',
    'Kilograms',
)

@login_required(login_url=LOGIN_URL)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'all_products':products})

@login_required(login_url=LOGIN_URL)
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product)
    return render(request, 'products/product_detail.html', {'form' : form })

@login_required(login_url=LOGIN_URL)
def product_new(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, initial={"UnitOfMeasure":"Set"})

        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.date_created = timezone.now()
            product.date_modified = timezone.now()
            product.isDiscontinued = False
            product.save()
            return redirect('product_detail', pk=product.pk)

    else:
        form = NewProductForm()
    return render(request, 'products/product_edit.html', {'form': form,
                                                          'title': 'New Product',
                                                          'all_units_of_measure': all_units_of_measure})

@login_required(login_url=LOGIN_URL)
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
         form = EditProductForm(request.POST, instance=product)
         if form.is_valid():
              print('product_edit POST is valid')
              product = form.save(commit=False)
              product.user = request.user
              product.date_modified = timezone.now()
              product.save()
              return redirect('product_detail', pk=product.pk)
    else:
         form = EditProductForm(instance=product)
    return render(request, 'products/product_edit.html', {'form':form,
                                                          'title': 'Edit Product',
                                                          'all_units_of_measure': all_units_of_measure})


