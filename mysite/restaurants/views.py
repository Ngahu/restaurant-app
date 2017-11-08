# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from django.shortcuts import render
from .models import RestaurantLocation
from django.db.models import Q

def restaurant_listview(request):
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list":queryset,
        "title":"THIS IS THE HOME PAGE"
    }
    template_name = 'list.html'
    return render(request,template_name,context)


class RestaurantListView(ListView):
    template_name = 'list.html'
    def get_queryset(self):
        #print(self.kwargs)
        slug  = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
            Q(category__iexact=slug) |
            Q(category__contains=slug) 
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset

