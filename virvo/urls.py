# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

from . import views

app_name = 'virvo'
urlpatterns = [
    
    url(r'^$', TemplateView.as_view(template_name='virvo/stations.html'),name='virvo_home'),

    url(r'gettree/',views.gettree,name='gettree'),

    url(r'station/', views.StationsView.as_view(),name='station_manager'),
    
    url(r'mapmonitor/', TemplateView.as_view(template_name='virvo/map_monitor.html'),name='map_monitor'),
]