# -*- coding: utf-8 -*-

from django import forms
from django.utils.dateparse import parse_datetime
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget,AdminSplitDateTime
from django.contrib.postgres.forms.ranges import DateRangeField, RangeWidget

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout

from . import models
from .models import Stations
import datetime

class CreateDMAForm(forms.Form):

    dma_no      = forms.CharField(label='分区编号',max_length=20)
    dma_name    = forms.CharField(label='分区名称',max_length=20)
    creator     = forms.CharField(label='负责人',max_length=20)
    create_date  = forms.DateField(label='建立日期')



# class CreateStationForm(forms.ModelForm):
#     """docstring for CreateStationForm"""

#     class Meta:
#         model = models.Stations
#         fields= '__all__'

#     # def __init__(self, arg):
#     #     super(CreateStationForm, self).__init__()
#     #     self.arg = arg
        

# class StationsForm(forms.ModelForm):

#     station_desc = forms.CharField(max_length=256)
#     longitude = forms.CharField(max_length=20)
#     latitude = forms.CharField(max_length=20)
#     geopos  = forms.ChoiceField(choices=enumerate(['室外地上','室外底下','室内']))

#     class Meta:
#         model = models.Stations
#         fields = [
#             'station_name',  
#             'meter_property',
#             'meter_type',    
#             'meter_code',    
#             'simno',         
#             'caliber',       
#             'big_user',      
#             # 'focus',   
#             'belongto'      
#             # 'installed',     
#         ]

#     def __init__(self, *args, **kwargs):
#         # user = kwargs.pop('user','')
#         # instance = kwargs['instance']
        
#         super(StationsForm, self).__init__(*args, **kwargs)
#         self.fields['belongto']=forms.ModelChoiceField(queryset=models.Organization.objects.all())
#         qs = models.Stations.objects.all()
#         qs1 = qs.order_by('meter_property').values_list('meter_property', flat=True)
#         # self.fields['meter_property']=forms.ModelChoiceField(queryset=qs1.distinct())
#         self.fields['meter_property'].choices=enumerate(['工业用水','商业用水','特种行业用水','行政事业用水','绿化用水'])
#         qs2 = qs.order_by('meter_type').values_list('meter_type',flat=True).distinct()
        
#         self.fields['meter_type']=forms.ChoiceField(choices=enumerate(qs2), widget=forms.RadioSelect())
#         # self.fields['unique_code']=forms.CharField(max_length=15)

#     def clean_staion_desc(self):
#         station_desc = self.cleaned_data.get('station_desc')
#         print (station_desc)
#         return station_desc

#     def clean_longitude(self):
#         longitude = self.cleaned_data.get('longitude')
        
#         return longitude
    

#     # def save(self,commit=True):
        
#     #     instance = super(StationsForm, self).save(commit=False)

        
#     #     return instance


class DMABaseinfoForm(forms.ModelForm):

    orgs = forms.ModelChoiceField(label='所属组织',queryset=models.Organization.objects.all())

    class Meta:
        model = models.DMABaseinfo
        fields = [
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

    def __init__(self, *args, **kwargs):
        super(DMABaseinfoForm, self).__init__(*args, **kwargs)
        if self.instance.dma.parent:
            self.fields['orgs'].initial = self.instance.dma.parent.pk
        else:
            self.fields['orgs'].initial =  1


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

    # @property
    # def helper(self):
    #     helper = FormHelper()
    #     helper.form_tag = False # don't render form DOM element
    #     helper.render_unmentioned_fields = True # render all fields
    #     helper.label_class = 'col-md-2'
    #     helper.field_class = 'col-md-10'
    #     return helper        


"""
Stations creation, manager
"""
class StationsCreateManagerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StationsCreateManagerForm, self).__init__(*args, **kwargs)
        # self.fields['invoice_date'].widget.attrs['class'] = 'calendar'
    class Meta:
        model = Stations
        fields= '__all__'

"""
Stations edit, manager
"""
class StationsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StationsForm, self).__init__(*args, **kwargs)
        # self.fields['invoice_date'].widget.attrs['class'] = 'calendar'
    class Meta:
        model = Stations    
        fields= '__all__'