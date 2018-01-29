# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . import models

# Register your models here.

class CommunityAdmin(admin.ModelAdmin):
    list_display = ['name','districtid']


   

class WatermeterAdmin(admin.ModelAdmin):
    actions = ['change_meterstate']
    list_display = ['nodeaddr','wateraddr','rvalue','fvalue','metertype','meterstate','commstate','rtime','lastrvalue','lastrtime','dosage','islargecalibermeter']

    list_filter = ['metertype','meterstate','commstate']

    fieldsets = (
            (None,{
                'fields':(('nodeaddr','wateraddr'),)
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

    def change_meterstate(self,request,queryset):
        rows_updated = queryset.update(meterstate='正常')
        if rows_updated == 1:
            message_bit = "1 item was"
        else:
            message_bit = "%s items were" % rows_updated
        self.message_user(request, "%s successfully updated as nomal." % message_bit)
    change_meterstate.short_description = 'change meterstate' 

admin.site.register(models.District)
admin.site.register(models.Community,CommunityAdmin)
admin.site.register(models.Watermeter,WatermeterAdmin)