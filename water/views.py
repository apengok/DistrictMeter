# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView,FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from dma.fusioncharts import FusionCharts
from .forms import SearchForm,AnalyWaterForm,DateRangeForm

import random


def nightflow(chartid,chartname,width=600,height=400):
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
    column2d = FusionCharts("mscombi2d", chartid , width, height, chartname, "json",datasource)

    return column2d

# Create your views here.
def dma_online(request):
    return render(request,"water/dma_online.html",{'output':nightflow().render()})



class WaterListview(ListView):

    template_name = 'water/water_home.html'

    def get_queryset(self):
        return None

    def get_context_data(self, *args, **kwargs):
        
        context = super(WaterListview, self).get_context_data(*args, **kwargs)
        
        return context


class StaionMonitorView(TemplateView):
    template_name = 'water/station_monitor.html'

    def get_context_data(self, *args, **kwargs):
        
        context = super(StaionMonitorView, self).get_context_data(*args, **kwargs)

        
        
        return context

class DmaOnlineView(TemplateView):
    template_name = 'water/dma_online.html'

    def get_context_data(self, *args, **kwargs):
        
        context = super(DmaOnlineView, self).get_context_data(*args, **kwargs)

        context['output'] = nightflow("ext1","chart-1").render()
        
        return context


class RTCurveView(TemplateView):
    template_name = 'water/rt_curve.html'

    def get_context_data(self, *args, **kwargs):
        
        context = super(RTCurveView, self).get_context_data(*args, **kwargs)

        context['output'] = nightflow("ext2","chart-1").render()
        context['output2'] = nightflow("ext3","chart-2").render()
        context['output3'] = nightflow("ext4","chart-3").render()
        context['output4'] = nightflow("ext5","chart-4").render()
        
        return context                



class BigUserOnlineView(TemplateView):
    
    template_name = 'water/big_user_online.html'

    def get_context_data(self, *args, **kwargs):
        
        context = super(BigUserOnlineView, self).get_context_data(*args, **kwargs)

        form = SearchForm(self.request.POST or None)
        context['form'] = form

        # context['big_user'] = form.cleaned_data['name'] 
        
        return context       

    def post(self,request,*args,**kwargs) :
        context = self.get_context_data()

        if context['form'].is_valid():
            pass
            print (context['form'].cleaned_data['name'])
        

        return super(BigUserOnlineView,self).render_to_response(context)



#数据分析
class AnalyUsageView(TemplateView):
    template_name = 'water/analy_usage.html'        


    def get_context_data(self, *args, **kwargs):
        
        context = super(AnalyUsageView, self).get_context_data(*args, **kwargs)

        form = AnalyWaterForm(self.request.POST or None)
        context['form'] = form

        context['output'] = nightflow("ext1","chart-day_water",1100,600).render()

        range_form = DateRangeForm(self.request.POST or None)
        context['range_form'] = range_form

        contact_list = range(100)
        paginator = Paginator(contact_list, 10) # Show 25 contacts per page

        page = self.request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        context['contacts'] = contacts
                
        return context      

    def post(self,request,*args,**kwargs):
        context = self.get_context_data()

        if context['form'].is_valid():

            if "today" in self.request.POST:
                print 'query today'

            elif "prevday" in self.request.POST:
                print 'prevday'
            
            else:
                print (context['form'].cleaned_data['organization'])

        elif context['range_form'].is_valid():
            print 'daterange'

        else:
            print 'else'
        

        return super(AnalyUsageView,self).render_to_response(context)