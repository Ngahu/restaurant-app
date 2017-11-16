# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save
from django.core.urlresolvers import reverse


User = settings.AUTH_USER_MODEL 

class RestaurantLocation(models.Model):
    owner     =      models.ForeignKey(User)
    name      =      models.CharField(max_length=120)
    location  =      models.CharField(max_length=120,blank=True, null=True)
    category  =      models.CharField(max_length=120,blank=False, null=True)
    timestamp =      models.DateTimeField(auto_now_add=True)  #when it was created/ added
    updated   =      models.DateTimeField(auto_now=True) #when it was updated/changed
    slug      =      models.SlugField(unique=True,blank=True, null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Restaurant:restaurant-detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.name

    @property
    def title(self):
        return self.name



def restaurantlocation_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)



# def restaurantlocation_post_save_receiver(sender,instance,*args,**kwargs):
#     print("Saved.")
#     print(instance.timestamp)


pre_save.connect(restaurantlocation_pre_save_receiver,sender=RestaurantLocation)

# post_save.connect(restaurantlocation_post_save_receiver,sender=RestaurantLocation)
