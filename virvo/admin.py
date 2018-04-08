# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name','parent']



@admin.register(models.Stations)
class StationsAdmin(admin.ModelAdmin):
    list_display = ['station_name','meter_property','meter_type','meter_code','simno','caliber','belongto','big_user','focus','installed']    


@admin.register(models.DMABaseinfo)
class DMABaseinfoAdmin(admin.ModelAdmin):
    list_display = [
            'dma_no',  
            'pepoles_num',
            'acreage',    
            'user_num',    
            'pipe_texture',         
            'pipe_length',       
            'pipe_links',      
            'pipe_years',   
            'pipe_private',      
            'ifc',   
            'aznp',   
            'night_use',      
            'cxc_value',     
        ]