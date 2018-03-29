# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib import messages
from . models import Organization,Stations
import json
import random
from datetime import datetime

from mptt.utils import get_cached_trees
from mptt.templatetags.mptt_tags import cache_tree_children


from django.shortcuts import render,HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView,FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from dma.fusioncharts import FusionCharts
import django_tables2 as tables
from django_tables2 import RequestConfig
from django.db import connection
from django.utils.html import format_html
from django.utils.safestring import mark_safe

# from .fusioncharts import FusionCharts

# Create your views here.


def recursive_node_to_dict(node):
    result = {
        'name': node.name,
        'open':'true',
        'icon':"/static/virvo/images/站点管理/u842_1.png",
    }
    
    children = [recursive_node_to_dict(c) for c in node.get_children()]
    
    # get each node's station if exist
    # try:
    #     sats = node.station.all()
    #     for s in sats:
    #         children.append({'name':s.station_name})
    #     # children.append({'name':})
    # except:
    #     pass

    if children:
        result['children'] = children
    
    return result

def gettree(request):
    organs = Organization.objects.all()
    
    top_nodes = get_cached_trees(organs)

    dicts = []
    for n in top_nodes:
        dicts.append(recursive_node_to_dict(n))

    
    # print json.dumps(dicts, indent=4)

    
    
    return JsonResponse({'trees':dicts})


class StationsTable(tables.Table):
    selected = tables.CheckBoxColumn(accessor="id")
    btn_del  = tables.Column(accessor="id")  #empty_values=()
    class Meta:
        model = Stations
        template_name = 'django_tables2/bootstrap.html'
        attrs = {
            'id':'tb_stations',
            'class':'table',
        }


    def render_selected(self,record):    
        return format_html('<input class="nameCheckBox" name="name[]" type="checkbox" />')
        # if record.id:
        #     return mark_safe('<input class="nameCheckBox" name="name[]" type="checkbox" checked/>')
        # else:   
        #     return mark_safe('<input class="nameCheckBox" name="name[]" type="checkbox"/>')

    def render_btn_del(self,value):
        return format_html('<button type = "button" value="{}" class = "btnAlter" data-toggle = "modal" data-target = "#myModal">Alter</button><button type = "button" class = "btnDelete">Delete</button>',value)



class StationsView(TemplateView):
    """docstring for StationsView"""

    
    template_name = 'virvo/station_manager.html'
    
    def get_context_data(self, *args, **kwargs):
        
        context = super(StationsView, self).get_context_data(*args, **kwargs)

        
        # if self.request.method == 'POST':
        #     form = AnalyWaterForm(self.request.POST or None)
        # else:
            
        #     form = AnalyWaterForm()
            
        # context['form'] = form

        table = StationsTable(Stations.objects.all())
        RequestConfig(self.request, paginate={'per_page': 10}).configure(table)
        context['table'] = table

        
                
        return context         