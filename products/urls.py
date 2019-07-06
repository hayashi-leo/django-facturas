

## products.urls.py
from django.urls import path, include
from . import views as products_views

urlpatterns = [
    path('product/', products_views.product_list, name='product_list'),
    path('product/<int:pk>', products_views.product_detail, name='product_detail'),
    path('product/new', products_views.product_new, name='product_new'),
    path('product/<int:pk>/edit/', products_views.product_edit, name='product_edit')
]