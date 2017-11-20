# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView,CreateView,UpdateView
from django.shortcuts import render,get_object_or_404
from .models import RestaurantLocation
from django.db.models import Q
from .forms import RestaurantLocationCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your models here.



class RestaurantListView(LoginRequiredMixin,ListView):
    template_name = 'restaurants/list.html'
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)



class RestaurantDetailView(LoginRequiredMixin,DetailView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

    # def get_object(self,*args,**kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation,id=rest_id)
    #     return obj



class RestaurantCreateView(LoginRequiredMixin,CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/form.html'
    #success_url = "/restaurants/"


    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView,self).form_valid(form)


class RestaurantUpdateView(LoginRequiredMixin,UpdateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/detail-update.html'
    #success_url = "/restaurants/"
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)




def about(request):
    context = {
        "title":"THIS IS THE ABOUT PAGE"
    }
    template_name = 'restaurants/about.html'
    return render(request,template_name,context)
    


def home(request):
    context = {
        "title":"THIS IS THE HOME PAGE"
    }
    template_name = 'restaurants/home.html'
    return render(request,template_name,context)