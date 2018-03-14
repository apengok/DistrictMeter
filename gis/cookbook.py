# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.contrib.gis.geos import Polygon
import json
from gis import models as gis_model
import os
#from models import *
# Create your views here.

scada_classes_all = dict([(name, cls) for name, cls in gis_model.__dict__.items() if isinstance(cls, type)])


def ch01(request):
    
    return render(request,'gis/cookb/full-screen-map.html')

def ch01_map_controls(request):
    return render(request,'gis/cookb/ch01_map_controls.html')