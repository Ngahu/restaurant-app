# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
)
# Create your models here.


class User(AbstractBaseUser):
    email     =     models.EmailField(max_length=255,unique=True)
    active    =     models.BooleanField(default=True) # can login or not 
    staff     =     models.BooleanField(default=False) # staff user non super user
    admin     =     models.BooleanField(default=False) #super user 
    timestamp =     models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

    USERNAME_FIELD = 'email'

    @property
    def is_staff(self):
        return self.staff


    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

