# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView,FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from dma.fusioncharts import FusionCharts
from .forms import SearchForm,AnalyWaterForm,DateRangeForm
from .models import FlowShareDayTax,PressShareDayTax,Tblfminfo
import django_tables2 as tables
from django_tables2 import RequestConfig
from django.db import connection
from django.utils.html import format_html
from django.utils.safestring import mark_safe

import random

import logging

log = logging.getLogger("error_logger")

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
                pass

            elif "prevday" in self.request.POST:
                pass
            
            else:
                pass

        elif context['range_form'].is_valid():
            pass

        else:
            pass
        

        return super(AnalyUsageView,self).render_to_response(context)


def ajax_load_station(request):
    organization = request.GET.get('organization')
    # print 'organization',organization

    stations = Tblfminfo.objects.filter(filialename__icontains=organization)
    return render(request,'water/stations_list.html',{'stations':stations})

class AnalyFlowPressView(TemplateView):
    template_name = 'water/analy_flow_press.html'        


    def draw_chart(self,chartid,chartname,width,height,flow_list):
        # Create an object for the column2d chart using the FusionCharts class constructor
        flow_list=flow_list
        
        if len(flow_list)>0:
            subc = flow_list[0].readtime[:10]
        else:
            subc = "day"

        cates = [{"label":v.readtime[11:]} for v in flow_list ]
        values0 = [{"value":10} for v in flow_list ]
        values = [{"value":v.flux} for v in flow_list ]
        datasource = {}
        datasource["chart"] = {
            "caption": "夜间最小流量",
            "subcaption": subc,
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

    def get_context_data(self, *args, **kwargs):
        
        context = super(AnalyFlowPressView, self).get_context_data(*args, **kwargs)

        if self.request.method == 'POST':
            form = AnalyWaterForm(self.request.POST or None)
        else:
            
            form = AnalyWaterForm()
            
        context['form'] = form

        # print form['organization'].value(), form['station'].value(),form['readdate'].value(),form['date'].value()

        context['output'] = nightflow("ext1","chart-day_water",1100,600).render()

        
                
        return context      



    def post(self,request,*args,**kwargs):
        context = self.get_context_data()

        if context['form'].is_valid():

            if "today" in self.request.POST:
                pass

            elif "prevday" in self.request.POST:
                pass
            
            else:
                ix=context['form'].cleaned_data['organization']
                
                st = context['form'].cleaned_data['station']
                simid = st.simid
                rtime = context['form'].cleaned_data['readdate']

                log.error(simid)


                
                flow_list=FlowShareDayTax.objects.filter(simid=simid).filter(readtime__icontains=rtime)
                press_list=PressShareDayTax.objects.filter(simid=simid).filter(readtime__icontains=rtime)
                
                # print len(flow_list),flow_list[0].readtime
                # for fl in flow_list:
                #     print fl.simid,fl.readtime

                if len(flow_list)>0:
                    subc = flow_list[0].readtime[:10]
                else:
                    subc = "day"
                cates = [{"label":v.readtime[11:]} for v in flow_list ]
                if len(press_list) == 0:
                    values0 = [{"value":1} for v in flow_list ]
                else:
                    values0 = [{"value":v.pressure} for v in press_list ]
                values = [{"value":v.flux} for v in flow_list ]
                datasource = {}
                datasource["chart"] = {
                    "caption": "flow day data",
                    "subcaption": subc,
                    "xaxisname": "Time",
                    "yaxisname": "watermeter flow",
                    "numberprefix": "$",
                    "theme": "ocean"
                }
                datasource["categories"] = [{
                    "category": cates
                }]

                datasource["dataset"] = [ {
                        "seriesname": "press ceiling",
                        "renderas": "line",
                        "showvalues": "0",
                        "data": values0
                    }, {
                        "seriesname": "flows flow",
                        "renderas": "line",
                        "showvalues": "0",
                        "data": values
                    }
                ]
                column2d = FusionCharts("mscombi2d", "ext1" , "1100", "600", "chart-day_water", "json",datasource)

                context['output'] = column2d.render()    #self.draw_chart("ext1","chart-day_water",1100,600,flow_list).render()
        

        return super(AnalyFlowPressView,self).render_to_response(context)        


class ExtraMixin(tables.Table):
    extra = tables.Column()

class FlowMeterTable(tables.Table):
    selected = tables.CheckBoxColumn(accessor="pid")
    btn_del  = tables.Column(accessor="pid")  #empty_values=()
    class Meta:
        model = FlowShareDayTax
        template_name = 'django_tables2/bootstrap.html'
        attrs = {
            'id':'tb_flowmeter',
            'class':'table',
        }


    def render_selected(self,record):    
        # return format_html('<input class="nameCheckBox" name="name[]" type="checkbox" checked/>')
        if record.pid:
            return mark_safe('<input class="nameCheckBox" name="name[]" type="checkbox" checked/>')
        else:   
            return mark_safe('<input class="nameCheckBox" name="name[]" type="checkbox"/>')

    def render_btn_del(self,value):
        return format_html('<button type = "button" value="{}" class = "btnAlter" data-toggle = "modal" data-target = "#myModal">Alter</button><button type = "button" class = "btnDelete">Delete</button>',value)


def blocker(*args):
    raise Exception('No database access allowed here.')

class FlowMeterView(TemplateView):
    """docstring for FlowMeterView"""

    
    template_name = 'water/device_flowmeter.html'
    
    def get_context_data(self, *args, **kwargs):
        
        context = super(FlowMeterView, self).get_context_data(*args, **kwargs)

        #may use in django2.0
        # with connection.execute_wrapper(blocker):
        #     return render(self.request,'main.html',context)

        if self.request.method == 'POST':
            form = AnalyWaterForm(self.request.POST or None)
        else:
            
            form = AnalyWaterForm()
            
        context['form'] = form

        table = FlowMeterTable(FlowShareDayTax.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table

        

        
                
        return context     
                        