# @brief: Extend existing django User model using one-to-one link.
# to do this, we create our own User model named 'Profile'
# having its own database table witch should hold a one-to-one
# relationship with django User Model.

'''
@from django docs.django.project.com
https://docs.djangoproject.com/en/2.2/topics/db/examples/one_to_one/

How One-to-One relationships works.  Example.

from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=True)

    def __str__(self):
        return "%s the restaurant" % self.place.name

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)

when you instantiate a restaurant, you pass in a already created
instance of place object as argument to Restaurants' constructor

r = Restaurant(place=p1, serves_hot_dogs=True, serves_pizza=False)

## restaurants can access its' place attribute
r.place

## now, place can access its associated restaurant
p1.restaurant  ## How??  This is achieved by django 'related_name'
see https://docs.djangoproject.com/en/2.2/topics/db/examples/one_to_one/

getting back to our example:

from a restaurant object, you can do r.place.  But if you want the
restaurant given the place object, How would you do that?  That's where
'related_name' or the 'reverse relationship' comes in.

Django by default gives you a default 'related_name' which is the ModelName
(in lowercase).  However, you can override it by specifying a 'related_name'
in the OneToOneField().  Here is its signature

a = models.OneToOneField(A, related_name='foobar')

# ...
a.foobar

for ForeignKey(), it returns a list of related objects

a = models.OneToOneField(A, related_name='profiles')

# ...
a.profiles.all()
a.profiles_set()
a.profiles_get()

for more details: https://stackoverflow.com/questions/11088901/django-onetoone-reverse-access

'''

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# django signals tells us when to update our
# Profile model when instances of django User
# model are created or updated.

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'auth_profile'

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)


