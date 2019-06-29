from django.contrib import admin
from .models import Product

# Register your models here.

# To allow django admin to create/update/delete/modify your models
# we must first register them under 'admin.py'.
#
# Simplest way to register them is
#
# admin.site.register(myModel)
#
# or
#
# for model in [Author, Genre, Book]:
#    admin.site.register(model)

admin.site.register(Product)