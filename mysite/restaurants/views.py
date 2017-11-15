# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView,CreateView
from django.shortcuts import render,get_object_or_404
from .models import RestaurantLocation
from django.db.models import Q
from .forms import RestaurantLocationCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your models here.




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

    # def get_object(self,*args,**kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation,id=rest_id)
    #     return obj



class RestaurantCreateView(LoginRequiredMixin,CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/form.html'
    success_url = "/restaurants/"


    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView,self).form_valid(form)


#FIXME:4:36:58
