# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from django.shortcuts import render
from .models import RestaurantLocation

# Create your views here.

def restaurant_listview(request):
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list":queryset
    }
    template = 'list.html'
    return render(request,template,context)


class RestaurantListView(ListView):
    queryset = RestaurantLocation.objects.all()
    