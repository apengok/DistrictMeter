# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

from . import views

app_name = 'virvo'
urlpatterns = [
    
    url(r'^$', TemplateView.as_view(template_name='virvo/stations.html'),name='virvo_home'),

    
]