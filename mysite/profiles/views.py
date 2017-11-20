# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView
from  django.http import Http404

User = get_user_model()

class ProfileDetailView(DetailView):
    template_name = 'profiles/user.html'

    def get_object(self):
        full_name = self.kwargs.get("full_name")
        if full_name is None:
            raise Http404
        return get_object_or_404(User,full_name=full_name,active=True)



#Fixme:6:02:18