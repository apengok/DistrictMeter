# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.dateparse import parse_datetime
from django.db import models as dj_models
from . import models
from .forms import WatermeterForm

from .widgets import StringDateTimeWidget,StringSplitDateTime

# Register your models here.

class CommunityAdmin(admin.ModelAdmin):
    list_display = ['name','districtid']

    fields = ('name','districtid')


@admin.register(models.Tblfminfo)
class TblfminfoAdmin(admin.ModelAdmin):
    list_display = ['precinctname','filialename','usertype','userid','username','simid']


    formfield_overrides = {
        dj_models.DateTimeField: {'widget': StringSplitDateTime},
    }


class FlowShareDayTaxAdmin(admin.ModelAdmin):

    # date_hierarchy = 'readtime'
    list_filter = ['warning','warningdesc']

    list_display = ['readtime','simid','flux','plustotalflux','reversetotalflux','warning','warningdesc']

    formfield_overrides = {
        dj_models.DateTimeField: {'widget': StringSplitDateTime},
    }

    # def save_model(self, request, obj, form, change):
    #     print 'FlowShareDayTaxAdmin::',obj.readtime
    #     print 'form.cleaned_data',form.cleaned_data['readtime']
    #     obj.readtime = obj.readtime[:20]
    #     print 'FlowShareDayTaxAdmin::',obj.readtime
    #     super(FlowShareDayTaxAdmin,self).save_model(request, obj, form, change)

   
@admin.register(models.Watermeter)
class WatermeterAdmin(admin.ModelAdmin):
    # form = WatermeterForm
    actions = ['change_meterstate','change_datetime']
    list_display = ['id','communityid','buildingname','roomname','nodeaddr','wateraddr','rvalue','fvalue','metertype','meterstate','commstate','rtime','lastrvalue','lastrtime','dosage','islargecalibermeter']

    list_filter = ['metertype','meterstate','commstate']

    formfield_overrides = {
        dj_models.DateTimeField: {'widget': StringSplitDateTime},
    }

    fieldsets = (
            (None,{
                'fields':(('nodeaddr','wateraddr'),)
                }),
            ('Community',{
                'fields':('communityid',('buildingname','roomname'),)
                }),
            ('Values',{
                'fields':(('rvalue','fvalue'),'metertype','meterstate','commstate','rtime')
                }),
            ('Last read',{
                'fields':('lastrvalue','lastrtime')
                }),
            ('Others',{
                'fields':('dosage','islargecalibermeter')
                }),
        )



    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     extra_context = extra_context or {}
    #     # extra_context['osm_data'] = self.get_osm_info()
    #     print 'here?',object_id,extra_context
    #     print 'request:',request
    #     return super(WatermeterAdmin,self).change_view(
    #     request, object_id, form_url, extra_context=extra_context,
    #     )

    # def changelist_view(self, request, extra_context=None):
    #     response = super(WatermeterAdmin,self).changelist_view(request, extra_context)

    #     try:
    #         qs = response.context_data['cl'].queryset

    #     except (AttributeError, KeyError):
    #         return response
    #     # rtime_tmp = response.context['rtime']

    #     metrics = {
    #         'rtime': parse_datetime('rtime'),
    #         'lastrtime': parse_datetime('lastrtime'),
    #     }
    #     # response.context_data['summary'] = list(
    #     #     qs.values('product__name').annotate(**metrics)
    #     # )
    #     # response.context_data['summary_total'] = dict(
    #     #     qs.aggregate(**metrics)
    #     # )
    #     return response

        
    def save_model(self, request, obj, form, change):
        # print 'communityid:',obj.communityid
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            
            instance.save()
            formset.save_m2m()

    def change_meterstate(self,request,queryset):
        rows_updated = queryset.update(meterstate='正常')
        if rows_updated == 1:
            message_bit = "1 item was"
        else:
            message_bit = "%s items were" % rows_updated
        self.message_user(request, "%s successfully updated as nomal." % message_bit)
    change_meterstate.short_description = 'change meterstate' 


    def change_datetime(self,request,queryset):
        
        rows_updated = queryset.update(rtime=parse_datetime('rtime'),
            lastrtime=parse_datetime('lastrtime'))
        if rows_updated == 1:
            message_bit = "1 item was"
        else:
            message_bit = "%s items were" % rows_updated
        self.message_user(request, "%s successfully updated ." % message_bit)
    change_datetime.short_description = 'alter timestr to datetime' 

admin.site.register(models.District)
admin.site.register(models.Community,CommunityAdmin)
# admin.site.register(models.Watermeter)
admin.site.register(models.FlowShareDayTax,FlowShareDayTaxAdmin)