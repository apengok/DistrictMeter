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

from .tables import StationsTable
from django_tables2 import RequestConfig

# from dma.fusioncharts import FusionCharts


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


def gettreenode(request):
    node = request.POST['node']
    orgs = Organization.objects.filter(name=node)
    table = StationsTable(Stations.objects.filter(belongto=orgs))
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    
    vals = {'table':table}
    return render(request,'virvo/table_station.html',vals)
    # return JsonResponse(vals)    

def getchartd(request):
    data = [random.randint(2,13), 20, 6, 10, 20, 30]

    return JsonResponse({'data':data})




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

class MNFView(TemplateView):
    """docstring for StationsView"""

    
    template_name = 'virvo/mnf.html'
    
    def get_context_data(self, *args, **kwargs):
        
        context = super(MNFView, self).get_context_data(*args, **kwargs)

        
        # if self.request.method == 'POST':
        #     form = AnalyWaterForm(self.request.POST or None)
        # else:
            
        #     form = AnalyWaterForm()
            
        # context['form'] = form

        # table = StationsTable(Stations.objects.all())
        # RequestConfig(self.request, paginate={'per_page': 10}).configure(table)
        # context['table'] = table

        
                
        return context                 