from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

from . import views

app_name = 'water'
urlpatterns = [
    
    url(r'^$', views.WaterListview.as_view(),name='home'),
    url(r'dma_online/',views.DmaOnlineView.as_view(),name='dma_online'),
    url(r'rt_curve/',views.RTCurveView.as_view(),name='rt_curve'),
    url(r'big_user_online/',views.BigUserOnlineView.as_view(),name='big_user_online'),
]