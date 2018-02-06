# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView,FormView

# Create your views here.
def dma_online(request):
    return render(request,"water/dma_online.html",{})



class WaterListview(ListView):

    template_name = 'water/water_home.html'

    def get_queryset(self):
        return None

    def get_context_data(self, *args, **kwargs):
        
        context = super(WaterListview, self).get_context_data(*args, **kwargs)
        
        return context