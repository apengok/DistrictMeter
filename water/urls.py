from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

from . import views

app_name = 'water'
urlpatterns = [
    url(r'dma_online/',views.dma_online,name='dma_online'),
    url(r'^$', views.WaterListview.as_view()),
]