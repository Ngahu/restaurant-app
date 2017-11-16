# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from restaurants.models import RestaurantLocation


# Create your models here.

class Item(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant  = models.ForeignKey(RestaurantLocation)
    name        = models.CharField(max_length=300)
    contents    = models.TextField(help_text='Separate each item by Comma')
    excludes    = models.TextField(blank=True, null=True,help_text='Separate each item by Comma')
    public      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)  #when it was created/ added
    updated     = models.DateTimeField(auto_now=True) #when it was updated/changed

    class Meta:
        ordering = ['-updated','-timestamp']
    
    def get_contents(self):
        return self.contents.split(",")

    def get_excludes(self):
        return self.excludes.split(",")
