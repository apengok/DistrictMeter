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

from mptt.utils import get_cached_trees
from mptt.templatetags.mptt_tags import cache_tree_children

# from .fusioncharts import FusionCharts

# Create your views here.


def recursive_node_to_dict(node):
    result = {
        'id': node.pk,
        'name': node.name,
    }
    
    children = [recursive_node_to_dict(c) for c in node.get_children()]
    try:
        sats = node.station.all()
        for s in sats:
            children.append({'name':s.station_name})
        # children.append({'name':})
    except:
        pass

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