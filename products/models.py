from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):

    '''
    Model representing a Product (but not a specific copy of a product) on
    a User Account.
    '''
    title = models.CharField(max_length=120)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=False)
    code = models.CharField(max_length=120)
    description = models.TextField()

    quantity = models.IntegerField(default=1)
    unitPrice = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    barCode = models.IntegerField(default=1)

    unitOfMeasure = models.CharField(max_length=120)

    isSaleTaxIncluded = models.BooleanField(default=False)
    isServiceTaxIncluded = models.BooleanField(default=False)

    def __str__(self):
        '''
        String for representing the Model object
        '''
        return self.title

    def __unicode__(self):
        return self.title