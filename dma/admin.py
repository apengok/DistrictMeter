# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from dma.models import ZoneTree,ZoneBase,ZoneMeasure



class ZoneBaseInline(admin.TabularInline):
    model = ZoneBase


class ZoneTreeManager(admin.ModelAdmin):
    inlines = [ZoneBaseInline]

class ZoneMeasureManager(admin.ModelAdmin):
    model = ZoneMeasure

    list_display = ('zone_base',
            'measure_per_actual',      
            'measure_precision',       
            'zone_sale',
            'nightflow_min',
            'charge_waterwater_percent',
            'zone_detect_leak_num',
            'leak_water',
            'leak_obscur_water',
            'leak_obvious_water',
            'leak_rate',
            'pressure_quality',
            'water_quality',
            'zone_inner_pressure',)

# Register your models here.

admin.site.register(ZoneTree,ZoneTreeManager)
# admin.site.register(ZoneBase)
admin.site.register(ZoneMeasure,ZoneMeasureManager)