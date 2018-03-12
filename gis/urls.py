from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name = 'gis'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^getGeom',views.getGeom,name='getGeom'),
    url(r'^country/', TemplateView.as_view(template_name='gis/country.html')),
    url(r'^data/geojson/countries.geojson',views.countries,name='countries'),
    # url(r'^data/geojson/countries.geojson',TemplateView.as_view(template_name='data/geojson/countries.geojson')),

    url(r'^cookbook/$', TemplateView.as_view(template_name='gis/cookb/cookbook.html')),
    url(r'^cookbook/ch01',views.ch01,name='fullscreen'),
    url(r'^cookbook/map-layer', TemplateView.as_view(template_name='gis/cookb/map-layers.html')),
]