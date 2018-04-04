# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

from . import views

app_name = 'virvo'
urlpatterns = [
    
    url(r'^$', TemplateView.as_view(template_name='virvo/home.html'),name='virvo_home'),

    url(r'editform/$', TemplateView.as_view(template_name='virvo/edit_form.html'),name='editform'),
    url(r'gettree/$',views.gettree,name='gettree'),
    url(r'gettreenode/$',views.gettreenode,name='gettreenode'),
    url(r'getchartd/$',views.getchartd,name='getchartd'),

    url(r'station/$', views.StationsView.as_view(),name='station_manager'),
    
    url(r'list/$', views.StationsListView.as_view(),name='station_list'),
    url(r'list/(?P<pk>\d+)/edit/$', views.StationsUpdateView.as_view(),name='station_edit'),
    
    url(r'mnf/$', views.MNFView.as_view(),name='mnf'),
    url(r'mapmonitor/$', TemplateView.as_view(template_name='virvo/map_monitor.html'),name='map_monitor'),
]