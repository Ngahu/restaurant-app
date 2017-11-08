# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth import get_user_model
# Register your models here.


User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = User



admin.site.register(User,UserAdmin)


#ToDo  got to where i was to create a modeladmin