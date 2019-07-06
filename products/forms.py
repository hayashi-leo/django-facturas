# this file was manually created and not
# automatically added by django during 'startapp'

from django import forms
from . models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        '''
        With class Meta, we tell django which model
        should be used to create this form
        '''
        model = Product
        fields = ('title', 'code', 'description',
                  'quantity', 'unitPrice', 'barCode',
                  'unitOfMeasure', 'isSaleTaxIncluded', 'isServiceTaxIncluded',
                  'date_created', 'date_modified', 'isDiscontinued')

class NewProductForm(forms.ModelForm):

    class Meta:
        '''
        With class Meta, we tell django which model
        should be used to create this form
        '''

        model = Product
        fields = ('title', 'code', 'description',
                  'quantity', 'unitPrice', 'barCode',
                  'unitOfMeasure', 'isSaleTaxIncluded', 'isServiceTaxIncluded',)