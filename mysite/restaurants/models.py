# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):
    name      =      models.CharField(max_length=120)
    location  =      models.CharField(max_length=120,blank=True, null=True)
    category  =      models.CharField(max_length=120,blank=False, null=True)
    timestamp =      models.DateTimeField(auto_now_add=True)  #when it was created/ added
    updated   =      models.DateTimeField(auto_now=True) #when it was updated/changed
    slug      =      models.SlugField(unique=True)


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    @property
    def title(self):
        return self.name