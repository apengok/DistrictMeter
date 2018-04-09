# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib import messages
from . models import Organization,Stations,DMABaseinfo
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

from django.urls import reverse_lazy
from .forms import StationsForm,DMABaseinfoForm,CreateDMAForm,TestForm

import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
# from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin




# from dma.fusioncharts import FusionCharts


# from .fusioncharts import FusionCharts

# Create your views here.


def recursive_node_to_dict(node):
    result = {
        'id':node.pk,
        'name': node.name,
        'open':'true',
        'url':'/virvo/dma/{}'.format(node.pk),
        'target':'_self',
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
    
    orgs = Organization.objects.filter(name=node).first()
    
    table = StationsTable(Stations.objects.filter(belongto=orgs))
    
    # table = StationsTable(orgs.station_set.all())
    
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


class AjaxTemplateMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
        if request.is_ajax():
            self.template_name = self.ajax_template_name
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)


class TestFormView(SuccessMessageMixin, AjaxTemplateMixin, FormView):
    template_name = 'virvo/test_form.html'
    form_class = TestForm
    success_url = reverse_lazy('home')
    success_message = "Way to go!"        



class StationsListView(ListView):

    def get_queryset(self):
        return Stations.objects.all()


# class StationsUpdateView(AjaxTemplateMixin,UpdateView):
class StationsUpdateView(UpdateView):    
    template_name = 'virvo/edit_form.html'
    form_class = StationsForm        
    success_url = reverse_lazy('virvo:station_list')


    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        # request.POST['some_key'] = 'some_value'
        
        ret =  super(StationsUpdateView, self).post(request, **kwargs)
        

    def form_valid(self,form):
        obj = form.save(commit=False)
        
        lon = form.cleaned_data['longitude']
        alti = form.cleaned_data['altitude']
        gpos = form.cleaned_data['geopos']
        
        return super(StationsUpdateView,self).form_valid(form)

    def get_queryset(self):
        return Stations.objects.all()

    def get_form_kwargs(self):
        # print (self.kwargs)
        kwargs = super(StationsUpdateView, self).get_form_kwargs()
        # kwargs['user'] = self.request.user
        # print (kwargs)
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super(StationsUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Item'
        return context

def create_dma(request):
    
    print(request.POST)
    # if request.method == 'POST':
        # dma_no = request.POST.get('dma_no')
        # dma_name = request.POST.get('dma_name')
        # creator = request.POST.get('creator')
        # create_date = request.POST.get('create_date')
    form = CreateDMAForm(request.POST or None)
    if form.is_valid():
        parent = Organization.objects.first()
        orgs = Organization.objects.create(name=form.cleaned_data.get('dma_name'),parent=parent)

        obj = DMABaseinfo.objects.create(dma_no=form.cleaned_data.get('dma_no'),dma=orgs)
        # return HttpResponseRedirect("/virvo/dma/1/")
    if form.errors:
        print(form.errors)
    return render(request,'virvo/dma_manager.html',{'dma_form':form})

class DMAListView(UpdateView):
    template_name = 'virvo/dma_manager.html'
    form_class = DMABaseinfoForm
    # success_url = '/virvo/dma/1'

    def get_queryset(self):
        return DMABaseinfo.objects.all()

    def get_form_kwargs(self):
        print (self.kwargs)
        kwargs = super(DMAListView, self).get_form_kwargs()
        # kwargs['user'] = self.request.user
        print (kwargs)
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super(DMAListView, self).get_context_data(*args, **kwargs)
        context['title'] = 'DMA 管理'

        context['station_list'] = Stations.objects.all()

        create_dma_form = CreateDMAForm()
        context['dma_form'] = create_dma_form

        return context

    def form_valid(self,form):
        orgs = form.cleaned_data.get('orgs')
        print(orgs,type(orgs))
        print (form.instance)
        print(form.instance.dma)
        # print(form.instance.dma.parent)
        form.instance.dma.parent = orgs
        form.instance.dma.save()

        return super(DMAListView,self).form_valid(form)