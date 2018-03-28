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