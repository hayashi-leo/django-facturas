from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Customer(models.Model):

    companyName = models.CharField(max_length=120)
    contactName = models.CharField(max_length=120)
    contactTitle = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    region = models.CharField(max_length=32)
    postalCode = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    email = models.CharField(max_length=120)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.companyName

    def __unicode__(self):
        return self.companyName

