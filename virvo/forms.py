# -*- coding: utf-8 -*-

from django import forms
from django.utils.dateparse import parse_datetime
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget,AdminSplitDateTime
from django.contrib.postgres.forms.ranges import DateRangeField, RangeWidget


from . import models
import datetime


class StationsForm(forms.ModelForm):

    class Meta:
        model = models.Stations
        fields = [
            'station_name',  
            'meter_property',
            'meter_type',    
            'meter_code',    
            'simno',         
            'caliber',       
            'big_user',      
            'focus',         
            # 'installed',     
        ]