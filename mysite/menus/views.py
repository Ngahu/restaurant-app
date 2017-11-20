# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import *
from django.views.generic import * #ListView, DetailView,CreateView,UpdateView
from .forms import ItemForm

# Create your views here.


class ItemListView(ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemDetailView(DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemCreateView(LoginRequiredMixin,CreateView):
    form_class = ItemForm
    template_name = 'menus/form.html'

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ItemCreateView,self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ItemCreateView,self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)



class ItemUpdateView(LoginRequiredMixin,UpdateView):
    form_class = ItemForm
    template_name = 'menus/detail-update.html'

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
    def get_form_kwargs(self):
        kwargs = super(ItemUpdateView,self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
     

