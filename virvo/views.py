# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib import messages
from . models import Organization,Stations
from django.views.generic import ListView
import json
import random
from datetime import datetime

# from .fusioncharts import FusionCharts

# Create your views here.

def gettree(request):
    organs = Organization.objects.all()
    root = organs[0]
    print root.name

    sub_dis = []
    tmp = {}
    tmp['name'] = root.name
    tmp['open'] = 'true'
    tmp['children']=[]
    for o in root.children.all():
        print o.name,o.id,o.parent.id
        tmp1={}
        tmp1['name']=o.name
        tmp1['url'] = "/virvo/station/"+str(o.id)
        tmp1['target'] = "_self"
        tmp1['children'] = []
        for d in o.children.all():
            tmp2={}
            tmp2['name'] = d.name
            tmp1['children'].append(tmp2)

        tmp['children'].append(tmp1)
        
        
    sub_dis.append(tmp)
        
    trees={'name':root.name, 'open':'true', 'children':sub_dis}
    
    return JsonResponse({'trees':sub_dis})