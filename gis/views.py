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



def return_feature_collection(cur):
    """
    Execute a JSON-returning SQL and return HTTP response
    :type sql: SQL statement that returns a a GeoJSON Feature
    """
    

    def generate():
        yield '{ "type": "FeatureCollection", "features": ['
        for idx, row in enumerate(cur):
            
            if idx > 0:
                yield ','
            yield '{ "type":"Feature","geometry":'
            yield row 
            yield '}'
        yield ']}'
        
    return HttpResponse(generate())

def get_table_by_name(tablename):
    cls = None
    rets = "no such gist table %s "% tablename
    for k,v in scada_classes_all.items():
        try:
            if v._meta.db_table == tablename:
                cls = v
        except:
            continue
    
    return cls
    

def index(request):
    
    return render(request,'gis/index.html')
    
    

def getGeom(request):
    #messages.info(request,'getGeom')
    if request.method == 'GET':
        left = request.GET.get('left')
        top = request.GET.get('top')
        right = request.GET.get('right')
        bottom = request.GET.get('bottom')
        layerName = request.GET.get('layerName') or ''
    
    if request.method == 'POST':
        left = request.POST.get('left')
        top = request.POST.get('top')
        right = request.POST.get('right')
        bottom = request.POST.get('bottom')
        layerName = request.POST.get('layerName') or ''
    
    tablename = 'g_cloudlayer_meta_'+layerName
    cls = get_table_by_name(tablename)
    
    
    
    #(x0, y0, x0, y1, x1, y1, x1, y0, x0, y0)
    bbox = (left,top,right,bottom)
    geom = Polygon.from_bbox(bbox)
    
    if cls is None:
        return HttpResponse('cant find table:%s '%(tablename,) )
    
    #return HttpResponse(geom)
    geodata=cls.objects.filter(geomdata__intersects=geom)
    gd = [ d.geomdata.json for d in geodata]
    
    
    return return_feature_collection(gd)
    
def countries(request):
    jsonfile = os.path.join(os.path.dirname(os.path.abspath(__file__)),"templates","gis","data","geojson", "countries.geojson")
    d = open(jsonfile).read()
    data = json.loads(d)    # loads a string of json and converts the data to a python dict

    return HttpResponse(json.dumps(data), content_type='application/json')
    
    