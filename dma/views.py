# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView,FormView

from .models import ZoneTree,ZoneBase,ZoneMeasure
from .dmadata import static_monthly,generet_static
from .fusioncharts import FusionCharts
from .forms import JoinForm,MeasureForm

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

class HomeView(View):
    def get(self,request):
        form = JoinForm()
        return render(request,"home.html",{'form':form})

class JoinFormView(FormView):
    form_class = JoinForm
    template_name = "home.html"
    success_url = '/form_success/'

    def form_invalid(self,form):
        response = super(JoinFormView,self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors,status=400)
        else:
            return response

    def form_valid(self,form):
        response = super(JoinFormView,self).form_valid(form)
        if self.request.is_ajax():
            print(form.cleaned_data)
            data = {
                'message':"successfully submit form data!"
            }
            return JsonResponse(data)
        else:
            return response

# def wbalance(request):
#     return render(request,"dma/wbalance.html",{})

class DmazoneListview(ListView):

    template_name = 'dma/dma_detail.html'

    def get_queryset(self):
        return ZoneTree.objects.all()

    def get_context_data(self, *args, **kwargs):
        
        context = super(DmazoneListview, self).get_context_data(*args, **kwargs)
        slug=self.kwargs.get('slug')
        if slug:
            current_zone = ZoneTree.objects.get(slug=slug)
        else:
            current_zone = ZoneTree.objects.first()

        context['current_zone'] = current_zone
        context['active_detail'] = True
        context['active_balance'] = False
        context['active_econic'] = False
        context['active_static'] = False
        context['nodes'] = ZoneTree.objects.all()

        context['output'] = self.nightflow().render()   #column2d.render(),
        return context

    def nightflow(self):
        # Create an object for the column2d chart using the FusionCharts class constructor
        flow_list=[random.randint(1,5) for _ in range(20)]
        
        cates = [{"label":n} for n in range(20) ]
        values0 = [{"value":10} for v in flow_list ]
        values = [{"value":v} for v in flow_list ]
        datasource = {}
        datasource["chart"] = {
            "caption": "夜间最小流量",
            "subcaption": 'day',
            "xaxisname": "Time",
            "yaxisname": "watermeter flow",
            "numberprefix": "$",
            "theme": "ocean"
        }
        datasource["categories"] = [{
            "category": cates
        }]

        datasource["dataset"] = [ {
                "seriesname": "flow ceiling",
                "renderas": "line",
                "showvalues": "0",
                "data": values0
            }, {
                "seriesname": "meter flow",
                "renderas": "line",
                "showvalues": "0",
                "data": values
            }
        ]
        column2d = FusionCharts("mscombi2d", "ex3" , "600", "400", "chart-1", "json",datasource)

        return column2d
        


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

class WbalanceListview(DmazoneListview):

    template_name = 'dma/wbalance.html'

    
    def get_context_data(self, *args, **kwargs):
        # print self.request
        
        context = super(WbalanceListview, self).get_context_data(*args, **kwargs)
        
        context['active_detail'] = False
        context['active_balance'] = True
        t_in = 1000000
        context['balance'] = generic_balance(t_in)
        return context


class EconomyListview(DmazoneListview):

    template_name = 'dma/econic.html'

    
    def get_context_data(self, *args, **kwargs):
        
        context = super(EconomyListview, self).get_context_data(*args, **kwargs)
        
        context['active_detail'] = False
        context['active_econic'] = True
        return context


class StaticListview(DmazoneListview):

    template_name = 'dma/static.html'

    def get_context_data(self, *args, **kwargs):
        # print self.request
        context = super(StaticListview, self).get_context_data(*args, **kwargs)
        
        context['active_detail'] = False
        context['active_static'] = True
        context['static_monthly'] = generet_static()
        return context        


def press_value(request):
    if request.method == 'GET':
        id = request.GET.get('pid')
            
    if request.method == 'POST':
        id = request.POST.get('pid')
        
    
    # pp=PressShareDayTax.objects.filter(pid=id)[0]
    sv_list={'lsl':random.randint(1,10),
        'cxc':random.randint(1,10),
        'dgc':random.randint(1,10),
        'jll':random.randint(1,10),
        'bll':random.randint(1,10),
        'nyl':random.randint(1,10), #pp.pressure,
        'dts':random.randint(1,10),}
    #results = [random.randint(1,10),]
    return JsonResponse({'press':sv_list})        

class MeasureCreateView( CreateView):
    template_name = 'dma/dma-edit.html'
    success_url = '/dma/'
    form_class = MeasureForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        # obj.user = self.request.user
        return super(MeasureCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(MeasureCreateView, self).get_form_kwargs()
        # kwargs['user'] = self.request.user

        return kwargs

    # def get_queryset(self):
    #     return Item.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(MeasureCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create Item'
        context['nodes'] = ZoneTree.objects.all()
        return context


class MeasureUpdateView( UpdateView):
    template_name = 'dma/dma-edit.html'
    form_class = MeasureForm

    def get_queryset(self,**kwargs):
        print self.request
        slug=self.kwargs.get('slug')
        if slug:
            current_zone = ZoneTree.objects.get(slug=slug)
        else:
            current_zone = ZoneTree.objects.first()

        print '1.',current_zone
        print '2.',current_zone.zbase
        
        pk = int(self.kwargs.get('pk'))
        print '4.',pk
        return ZoneMeasure.objects.first()

    def get_context_data(self, *args, **kwargs):
        context = super(MeasureUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Item'
        context['nodes'] = ZoneTree.objects.all()
        return context

    def get_form_kwargs(self):
        kwargs = super(MeasureUpdateView, self).get_form_kwargs()
        # kwargs['current_zone'] = self.request.current_zone
        return kwargs