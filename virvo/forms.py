# -*- coding: utf-8 -*-

from django import forms
from django.utils.dateparse import parse_datetime
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget,AdminSplitDateTime
from django.contrib.postgres.forms.ranges import DateRangeField, RangeWidget

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

from . import models
import datetime


class StationsForm(forms.ModelForm):

    staion_desc = forms.CharField(max_length=256)
    longitude = forms.CharField(max_length=20)
    latitude = forms.CharField(max_length=20)
    geopos  = forms.ChoiceField(choices=enumerate(['室外地上','室外底下','室内']))

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
            'belongto'      
            # 'installed',     
        ]

    def __init__(self, *args, **kwargs):
        # user = kwargs.pop('user','')
        super(StationsForm, self).__init__(*args, **kwargs)
        self.fields['belongto']=forms.ModelChoiceField(queryset=models.Organization.objects.all())
        qs = models.Stations.objects.all()
        qs1 = qs.order_by('meter_property').values_list('meter_property', flat=True)
        self.fields['meter_property']=forms.ModelChoiceField(queryset=qs1.distinct())
        qs2 = qs.order_by('meter_type').values_list('meter_type',flat=True).distinct()
        print(qs2)
        self.fields['meter_type']=forms.ChoiceField(choices=enumerate(qs2), widget=forms.RadioSelect())
        # self.fields['unique_code']=forms.CharField(max_length=15)




class TestForm(forms.ModelForm):

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

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # don't render form DOM element
        helper.render_unmentioned_fields = True # render all fields
        helper.label_class = 'col-md-2'
        helper.field_class = 'col-md-10'
        return helper        