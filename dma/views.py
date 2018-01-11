# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .models import DmaZone,Measure
from .dmadata import static_monthly,generet_static
import random

# Create your views here.

def home(request):
	return render(request,"home.html",{"item_d":"dasfasdf"})


def main(request):
	# print request.GET
	return render(request,"main.html",{})

def test(request,var):
	# print var
	# var = request.get("var")
	return render(request,"home.html",{"item_d":var})


# def wbalance(request):
#     return render(request,"dma/wbalance.html",{})

class DmazoneListview(ListView):

    template_name = 'dma/dma_detail.html'

    def get_queryset(self):
        return DmaZone.objects.all()

    def get_context_data(self, *args, **kwargs):
        
        context = super(DmazoneListview, self).get_context_data(*args, **kwargs)
        slug=self.kwargs.get('slug')
        if slug:
            context['current_zone'] = DmaZone.objects.get(slug=slug)
        else:
            context['current_zone'] = DmaZone.objects.get(pk=1)

        context['active_detail'] = True
        return context


def generic_balance(t_in):
    totoal_in=t_in
    auth_use=random.randint(165900,t_in)
    loss=totoal_in - auth_use   #44100
    charge_auth=random.randint(157500,165900)
    uncharge_auth=auth_use - charge_auth    #8400
    charge_measure=random.randint(141750,157500)
    charge_unmeasure=charge_auth - charge_measure   #15750
    uncharge_measure=random.randint(2400,uncharge_auth)
    uncharge_unmeasure=uncharge_auth - uncharge_measure #6000
    apparent_loss=random.randint(16280,loss)
    actual_loss=loss - apparent_loss    #27820
    unauth_use=random.randint(516,apparent_loss)
    statistic_error=apparent_loss - unauth_use  #15764
    money_back=charge_auth  #157500
    money_waste=loss + uncharge_auth    #52500

    balance = {'totoal_in':totoal_in,
                    'auth_use':auth_use,
                    'loss':loss,
                    'charge_auth':charge_auth,
                    'uncharge_auth':uncharge_auth,
                    'charge_measure':charge_measure,
                    'charge_unmeasure':charge_unmeasure,
                    'uncharge_measure':uncharge_measure,
                    'uncharge_unmeasure':uncharge_unmeasure,
                    'apparent_loss':apparent_loss,
                    'actual_loss':actual_loss,
                    'unauth_use':unauth_use,
                    'statistic_error':statistic_error,
                    'money_back':money_back,
                    'money_waste':money_waste,
                }

    return balance

class WbalanceListview(ListView):

    template_name = 'dma/wbalance.html'

    def get_queryset(self):
        return DmaZone.objects.all()

    def get_context_data(self, *args, **kwargs):
        # print self.request
        
        context = super(WbalanceListview, self).get_context_data(*args, **kwargs)
        slug=self.kwargs.get('slug')
        if slug:
            current_zone = DmaZone.objects.get(slug=slug)
        else:
            current_zone = DmaZone.objects.get(pk=1)

        context['current_zone'] = current_zone
        context['active_balance'] = True
        
        context['balance'] = generic_balance(current_zone.zone_water_in)
        return context


class EconomyListview(ListView):

    template_name = 'dma/econic.html'

    def get_queryset(self):
        return DmaZone.objects.all()

    def get_context_data(self, *args, **kwargs):
        
        context = super(EconomyListview, self).get_context_data(*args, **kwargs)
        slug=self.kwargs.get('slug')
        if slug:
            context['current_zone'] = DmaZone.objects.get(slug=slug)
        else:
            context['current_zone'] = DmaZone.objects.get(pk=1)

        context['active_econic'] = True
        return context


class StaticListview(ListView):

    template_name = 'dma/static.html'

    def get_queryset(self):
        return DmaZone.objects.all()

    def get_context_data(self, *args, **kwargs):
        # print self.request
        
        context = super(StaticListview, self).get_context_data(*args, **kwargs)
        slug=self.kwargs.get('slug')
        if slug:
            context['current_zone'] = DmaZone.objects.get(slug=slug)
        else:
            context['current_zone'] = DmaZone.objects.get(pk=1)

        context['active_static'] = True
        context['static_monthly'] = generet_static()
        return context        