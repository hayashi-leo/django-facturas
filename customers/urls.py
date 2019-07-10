## customers.url.py

from django.urls import path, include
from . import views as customers_views

urlpatterns = [
    path('customer/', customers_views.customer_list, name='customer_list'),
    path('customer/<int:pk>', customers_views.customer_detail, name='customer_detail'),
    path('customer/new', customers_views.customer_new, name='customer_new'),
    path('customer/<int:pk>/edit/', customers_views.customer_edit, name='customer_edit'),
]