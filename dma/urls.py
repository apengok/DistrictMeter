from django.conf.urls import url

from django.views.generic import TemplateView

from .views import (
    DmazoneListview,
    
    WbalanceListview,
    EconomyListview,
    StaticListview,
)
urlpatterns = [
    #url(r'^(?P<slug>[\w-]+)/edit/$', RestaurantUpdateView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/$', DmazoneListview.as_view(), name='detail'),
    url(r'^$', DmazoneListview.as_view()),
    # url(r'^(?P<slug>[\w-]+)/wbalance/$', TemplateView.as_view(template_name='dma/wbalance.html'),name='wbalance'),
    url(r'^(?P<slug>[\w-]+)/wbalance/$', WbalanceListview.as_view()),
    url(r'^(?P<slug>[\w-]+)/economy/$', EconomyListview.as_view()),
    url(r'^(?P<slug>[\w-]+)/static/$', StaticListview.as_view()),

]
