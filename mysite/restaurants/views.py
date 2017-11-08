# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView
from django.shortcuts import render,get_object_or_404
from .models import RestaurantLocation
from django.db.models import Q

def restaurant_listview(request):
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list":queryset,
        "title":"THIS IS THE HOME PAGE"
    }
    template_name = 'restaurants/list.html'
    return render(request,template_name,context)


class RestaurantListView(ListView):
    template_name = 'restaurants/list.html'
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



class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    # def get_context_data(self,*args, **kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantDetailView, self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context

    def get_object(self,*args,**kwargs):
        rest_id = self.kwargs.get('rest_id')
        obj = get_object_or_404(RestaurantLocation,id=rest_id)
        return obj