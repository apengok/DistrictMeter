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

from django.template.loader import render_to_string
from django.shortcuts import render,HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView,FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .tables import StationsTable
from django_tables2 import RequestConfig

from django.urls import reverse_lazy
from .forms import DMABaseinfoForm,CreateDMAForm,TestForm,StationsCreateManagerForm,StationsForm

import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
# from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin




# from dma.fusioncharts import FusionCharts


# from .fusioncharts import FusionCharts

# Create your views here.


def recursive_node_to_dict(node,url_cat):
    result = {
        'id':node.pk,
        'name': node.name,
        'open':'true',
        'url':'/virvo/dma/{}/{}'.format(node.pk,url_cat),
        'target':'_self',
        'icon':"/static/virvo/images/站点管理/u842_1.png",
    }
    
    children = [recursive_node_to_dict(c,url_cat) for c in node.get_children()]
    
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

def get_stationtree(request):
    organs = Organization.objects.all()
    
    top_nodes = get_cached_trees(organs)

    dicts = []
    for n in top_nodes:
        dicts.append(recursive_node_to_dict(n,'station'))

    
    # print json.dumps(dicts, indent=4)

    
    
    return JsonResponse({'trees':dicts})


def get_dmatree(request):
    organs = Organization.objects.all()
    
    top_nodes = get_cached_trees(organs)

    dicts = []
    for n in top_nodes:
        dicts.append(recursive_node_to_dict(n,''))

    
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



class StationsView(ListView):
    """docstring for StationsView"""

    model = Stations
    template_name = 'virvo/stations_list.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk') or 1
        orgs = Organization.objects.get(pk=pk)
        print(pk,orgs)
        return Stations.objects.all() #Stations.objects.filter(belongto=orgs)
    
    def get_context_data(self, *args, **kwargs):
        # print(self.kwargs)
        # print(args)
        # print(self.request)
        context = super(StationsView, self).get_context_data(*args, **kwargs)

        form = StationsForm(self.request.POST or None)
            
        context['form'] = form
        context['station_list'] = self.get_queryset()
        
                
        return context     

    def post(self,request,*args,**kwargs) :
        context = self.get_context_data(*args, **kwargs)
        print('sadjfkkjasdfasd8fas6df6')
        form = context['form']
        if form.is_valid():
            print(self.request.POST)
            form.save()
            
        if form.errors:
            print(form.errors)

        return super(StationsView,self).render_to_response(context)



def create_station(request):
    print('create_station...')
    form = CreateStationForm(request.POST or None)
    if form.is_valid():
        form.save()
        # return HttpResponseRedirect("/virvo/dma/1/")
    if form.errors:
        print(form.errors)
    return render(request,'virvo/station_list.html',{'form':form})
    
class StationFormUpdateView(UpdateView):
    model = Stations
    form_class = StationsForm
    template_name = 'virvo/edit_form.html'

    def dispatch(self, *args, **kwargs):
        print('dispatch..')
        print(kwargs)
        self.pk = kwargs['pk']
        return super(StationFormUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        item = Item.objects.get(id=self.pk)
        return HttpResponse(render_to_string('virvo/item_edit_form_success.html', {'item': item}))

    def get_queryset(self):
        return Stations.objects.all()  

class StationsListView(UpdateView):
    template_name = 'virvo/edit_form_inner.html'
    form_class = StationsForm

    def get_queryset(self):
        return Stations.objects.all()        

    def get_form_kwargs(self):
        print (self.kwargs)
        kwargs = super(StationsListView, self).get_form_kwargs()
        # kwargs['user'] = self.request.user
        print (kwargs)
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super(StationsListView, self).get_context_data(*args, **kwargs)
        context['title'] = 'DMA 管理'

        # context['station_list'] = Stations.objects.all()

        

        return context

    def form_valid(self,form):
        orgs = form.cleaned_data.get('orgs')
        print(orgs,type(orgs))
        print (form.instance)
        
        # form.instance.dma.parent = orgs
        # form.instance.dma.save()

        return super(StationsListView,self).form_valid(form)




# 


"""
Stations creation, manager
"""
class StationsCreateMangerView(CreateView):
    model = Stations
    template_name = 'virvo/stations_create_manager.html'
    form_class = StationsCreateManagerForm
    success_url = reverse_lazy('stations_list_manager');

    # @method_decorator(permission_required('virvo.change_stations'))
    def dispatch(self, *args, **kwargs):
        return super(StationsCreateMangerView, self).dispatch(*args, **kwargs)


"""
Stationss list, manager
"""
class StationsListMangerView(ListView):
    model = Stations
    template_name = 'virvo/stations_list_manager.html'

    # @method_decorator(permission_required('virvo.change_stations'))
    def dispatch(self, *args, **kwargs):
        return super(StationsListMangerView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        # user = self.request.user
        # manager_group = Group.objects.get(name=settings.BANCOAUSILI_MANAGER_GROUP)
        # if manager_group in user.groups.all():
        #     manager = Manager.objects.get(user=user)
        #     return Stations.objects.filter(centre__in=manager.centres.all())
        # else:
        #     return Stations.objects.all()
        return Stations.objects.all()

"""
Stations edit, manager
"""
class StationsUpdateManagerView(UpdateView):
    model = Stations
    form_class = StationsForm
    template_name = 'virvo/stations_edit_manager.html'

    # @method_decorator(permission_required('virvo.change_stations'))
    def dispatch(self, *args, **kwargs):
        self.stations_id = kwargs['pk']
        return super(StationsUpdateManagerView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        form.save()
        stations = Stations.objects.get(id=self.stations_id)
        return HttpResponse(render_to_string('virvo/stations_edit_manager_success.html', {'stations': stations}))

    def get_context_data(self, **kwargs):
        context = super(StationsUpdateManagerView, self).get_context_data(**kwargs)
        return context
