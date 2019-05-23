# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.contrib.gis.geos import Polygon
from django.views.generic import TemplateView
from django.template import TemplateDoesNotExist
from django.http import Http404

import json
from gis import models as gis_model
import os
#from models import *
# Create your views here.

scada_classes_all = dict([(name, cls) for name, cls in gis_model.__dict__.items() if isinstance(cls, type)])


class StaticView(TemplateView):
    def get(self, request, page, *args, **kwargs):
        self.template_name = page
        print(page)
        response = super(StaticView, self).get(request, *args, **kwargs)
        try:
            return response.render()
        except TemplateDoesNotExist:
            raise Http404()


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

def getgeojson(request):
    pgeojson = {"type":"FeatureCollection","features":[{"type":"Feature","geometry":{"type":"Polygon","coordinates":[[[-11862500.221591014,3921338.452036796],[-11846533.373609068,3910467.407495644],[-11853837.35527513,3885667.837281932],[-11881694.40662025,3889404.76073825],[-11896744.01026277,3907953.478824563],[-11877040.243489852,3921712.145082231],[-11862500.221591014,3921338.452036796]]]},"properties":"null"}]}

    # pgeojson = '{\"type\":\"FeatureCollection\",\"features\":[{\"type\":\"Feature\",\"geometry\":{\"type\":\"Polygon\",\"coordinates\":[[[-11888590.72569057,3901328.9348180657],[-11861922.698414044,3926128.506198114],[-11832876.627665678,3917635.5016297945],[-11841709.349897442,3881285.449215365],[-11863111.717817292,3881795.0262937024],[-11884344.225155914,3889948.3108659033],[-11888590.72569057,3901328.9348180657]]]},\"properties\":null}]}'
    pgeojson = {"type":"FeatureCollection","features":[{"type":"Feature","geometry":{"type":"Polygon","coordinates":[[[13178892.355395831,3489944.851357296],[13181281.012238158,3490454.4314972665],[13181822.4413829,3488777.063506157],[13180803.280811375,3487460.647792236],[13178648.181393484,3487938.3792190184],[13178202.298825681,3489021.2372169197],[13178892.355395831,3489944.851357296]]]},"properties":"null"}]}
    return JsonResponse(pgeojson)
    
def getFeatureEx(request):
    # return getGeom(request)

    nodes = '''{
        "features":[
        {
            "geometry":{
                "coordinates":[
                    118.39236,
                    29.88531
                ],
                "type":"Point"
            },
            "properties":{
                "angle":0,
                "caliber":0,
                "className":"ws_flow_meter",
                "endAltitude":0,
                "endDepth":0,
                "id":"00000011000000200",
                "industryCode":"JSKZ00020",
                "length":0,
                "lineWidth":0,
                "startAltitude":0,
                "startDepth":0
            },
            "type":"Feature"
        },
        {
            "geometry":{
                "coordinates":[
                    118.39530,
                    29.88569
                ],
                "type":"Point"
            },
            "properties":{
                "angle":0,
                "caliber":0,
                "className":"ws_flow_meter",
                "endAltitude":0,
                "endDepth":0,
                "id":"00000011000000200",
                "industryCode":"JSKZ00021",
                "length":0,
                "lineWidth":0,
                "startAltitude":0,
                "startDepth":0
            },
            "type":"Feature"
        },
        {
            "geometry":{
                "coordinates":[
                    118.39767484,
                    29.882346264
                ],
                "type":"Point"
            },
            "properties":{
                "angle":0,
                "caliber":0,
                "className":"ws_flow_meter",
                "endAltitude":0,
                "endDepth":0,
                "id":"00000011000000200",
                "industryCode":"JSKZ00020",
                "length":0,
                "lineWidth":0,
                "startAltitude":0,
                "startDepth":0
            },
            "type":"Feature"
        },
        {
            "geometry":{
                "coordinates":[
                    118.39977133,
                    29.883191412
                ],
                "type":"Point"
            },
            "properties":{
                "angle":0,
                "caliber":0,
                "className":"ws_flow_meter",
                "endAltitude":0,
                "endDepth":0,
                "id":"00000011000000200",
                "industryCode":"JSKZ00021",
                "length":0,
                "lineWidth":0,
                "startAltitude":0,
                "startDepth":0
            },
            "type":"Feature"
        },
            {
                "geometry":{
                    "coordinates":[
                        [
                            118.39237074,
                            29.885314617
                        ],
                        [
                            118.39534361,
                            29.885658422
                        ]
                    ],
                    "type":"LineString"
                },
                "properties":{
                    "angle":0,
                    "caliber":0,
                    "className":"ws_pipe",
                    "endAltitude":0,
                    "endDepth":0,
                    "id":"00000001000076520",
                    "length":0,
                    "lineWidth":0,
                    "startAltitude":0,
                    "startDepth":0
                },
                "type":"Feature"
            },
            {
                "geometry":{
                    "coordinates":[
                        [
                            118.39116966,
                            29.887703719
                        ],
                        [
                            118.39237074,
                            29.885314617
                        ]
                    ],
                    "type":"LineString"
                },
                "properties":{
                    "angle":0,
                    "caliber":0,
                    "className":"ws_pipe",
                    "endAltitude":0,
                    "endDepth":0,
                    "id":"00000001000076510",
                    "length":0,
                    "lineWidth":0,
                    "startAltitude":0,
                    "startDepth":0
                },
                "type":"Feature"
            },
            {
                "geometry":{
                    "coordinates":[
                        [
                            118.39767484,
                            29.882346264
                        ],
                        [
                            118.39977133,
                            29.883191412
                        ]
                    ],
                    "type":"LineString"
                },
                "properties":{
                    "angle":0,
                    "caliber":0,
                    "className":"ws_pipe",
                    "endAltitude":0,
                    "endDepth":0,
                    "id":"00000001000076550",
                    "length":0,
                    "lineWidth":0,
                    "startAltitude":0,
                    "startDepth":0
                },
                "type":"Feature"
            },
            {
                "geometry":{
                    "coordinates":[
                        [
                            118.39534361,
                            29.885658422
                        ],
                        [
                            118.39638227,
                            29.884213138
                        ]
                    ],
                    "type":"LineString"
                },
                "properties":{
                    "angle":0,
                    "caliber":0,
                    "className":"ws_pipe",
                    "endAltitude":0,
                    "endDepth":0,
                    "id":"00000001000076530",
                    "length":0,
                    "lineWidth":0,
                    "startAltitude":0,
                    "startDepth":0
                },
                "type":"Feature"
            },
            {
                "geometry":{
                    "coordinates":[
                        [
                            118.39638227,
                            29.884213138
                        ],
                        [
                            118.39767484,
                            29.882346264
                        ]
                    ],
                    "type":"LineString"
                },
                "properties":{
                    "angle":0,
                    "caliber":0,
                    "className":"ws_pipe",
                    "endAltitude":0,
                    "endDepth":0,
                    "id":"00000001000076540",
                    "length":0,
                    "lineWidth":0,
                    "startAltitude":0,
                    "startDepth":0
                },
                "type":"Feature"
            }
        ],
        "type":"FeatureCollection"
    }'''

    return HttpResponse(nodes)

def getGeom(request):
    #messages.info(request,'getGeom')
    if request.method == 'GET':
        left = request.GET.get('left')
        top = request.GET.get('top')
        right = request.GET.get('right')
        bottom = request.GET.get('bottom')
        className = request.GET.get('layerName') or ''
    
    if request.method == 'POST':
        left = request.POST.get('left')
        top = request.POST.get('top')
        right = request.POST.get('right')
        bottom = request.POST.get('bottom')
        className = request.POST.get('layerName') or ''
    
    print(left,top,right,bottom,className)
    tablename = 'g_cloudlayer_meta_'+className
    cls = get_table_by_name(tablename)
    
    
    
    #(x0, y0, x0, y1, x1, y1, x1, y0, x0, y0)
    bbox = (left,top,right,bottom)
    geom = Polygon.from_bbox(bbox)
    
    if cls is None:
        tablename = 'g_cloudlayer_meta_sx_gs_'+className
        cls = get_table_by_name(tablename)
        if cls is None:
            return HttpResponse('cant find table:%s '%(tablename,) )
    
    #return HttpResponse(geom)
    geodata=cls.objects.filter(geomdata__intersects=geom)
    gd = [ d.geomdata.json for d in geodata]
    
    # print("\t\r\ngd:",gd)
    return return_feature_collection(gd)
    
def countries(request):
    jsonfile = os.path.join(os.path.dirname(os.path.abspath(__file__)),"templates","gis","data","geojson", "countries.geojson")
    d = open(jsonfile).read()
    data = json.loads(d)    # loads a string of json and converts the data to a python dict

    return HttpResponse(json.dumps(data), content_type='application/json')
    
    

def getTopoByNode(request):

    node = '''{
        "features":[
            {
                "geometry":{
                    "coordinates":[
                        118.39767484,
                        29.882346264
                    ],
                    "type":"Point"
                },
                "properties":{
                    "angle":0,
                    "caliber":0,
                    "className":"ws_flow_meter",
                    "endAltitude":0,
                    "endDepth":0,
                    "id":"00000011000000200",
                    "industryCode":"JSKZ00020",
                    "length":0,
                    "lineWidth":0,
                    "startAltitude":0,
                    "startDepth":0
                },
                "type":"Feature"
            },
            {
                "geometry":{
                    "coordinates":[
                        118.39977133,
                        29.883191412
                    ],
                    "type":"Point"
                },
                "properties":{
                    "angle":0,
                    "caliber":0,
                    "className":"ws_flow_meter",
                    "endAltitude":0,
                    "endDepth":0,
                    "id":"00000011000000200",
                    "industryCode":"JSKZ00021",
                    "length":0,
                    "lineWidth":0,
                    "startAltitude":0,
                    "startDepth":0
                },
                "type":"Feature"
            },
            {
                "geometry":{
                    "coordinates":[
                        [
                            118.39767484,
                            29.882346264
                        ],
                        [
                            118.39977133,
                            29.883191412
                        ]
                    ],
                    "type":"LineString"
                },
                "properties":{
                    "angle":0,
                    "caliber":0,
                    "className":"ws_pipe",
                    "endAltitude":0,
                    "endDepth":0,
                    "id":"00000001000076550",
                    "industryCode":"JS07655",
                    "length":223.13662508062242,
                    "lineWidth":0,
                    "startAltitude":0,
                    "startDepth":0
                },
                "type":"Feature"
            }
        ],
        "type":"FeatureCollection"
    }'''

    return HttpResponse(node)