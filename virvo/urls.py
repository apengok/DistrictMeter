# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

from . import views

app_name = 'virvo'
urlpatterns = [
    
    url(r'^$', TemplateView.as_view(template_name='virvo/test_home.html'),name='virvo_home'),

    url(r'editform/$', TemplateView.as_view(template_name='virvo/edit_form.html'),name='editform'),
    url(r'getstationtree/$',views.get_stationtree,name='getstationtree'),
    url(r'getdmatree/$',views.get_dmatree,name='getdmatree'),

    url(r'gettreenode/$',views.gettreenode,name='gettreenode'),
    url(r'getchartd/$',views.getchartd,name='getchartd'),

    url(r'createdma/$',views.create_dma,name='create_dma'),
    url(r'dma/(?P<pk>\d+)/$', views.DMAListView.as_view(),name='dma_manager'),

    url(r'station/$', views.StationsView.as_view(),name='station_home'),
    url(r'station/(?P<pk>\d+)$', views.StationsListView.as_view(),name='station_manager'),
    url(r'createstation/$',views.create_station,name='create_station'),
    
    # url(r'list/(?P<pk>\d+)/edit/$', views.StationsUpdateView.as_view(),name='station_edit'),
    
    url(r'mnf/$', views.MNFView.as_view(),name='mnf'),
    url(r'mapmonitor/$', TemplateView.as_view(template_name='virvo/map_monitor.html'),name='map_monitor'),

    url(r'^test-form/$', views.TestFormView.as_view(), name="test-form"),
]