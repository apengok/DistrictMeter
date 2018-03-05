# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#from django.core.urlresolvers import reverse
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class ZoneTree(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True,on_delete=models.CASCADE, related_name='children', db_index=True)
    slug = models.SlugField()
    
    # def get_absolute_url(self):
    #     return reverse('sub_dma', kwargs={'path': self.get_path()})

    def get_absolute_url(self): #get_absolute_url
        #return f"/restaurants/{self.slug}" 
        return reverse('dma:detail', kwargs={'slug': self.slug})

    class MPTTMeta:
        order_insertion_by = ['name']
        
    class Meta:
        
        unique_together = ('slug', 'parent')
        db_table = 'zonetree'
    

    def __unicode__(self):
        return self.name


class ZoneBase(models.Model):
    dma_id 						= models.AutoField(primary_key=True)

    zonetree                    = models.ForeignKey(ZoneTree,blank=True, null=True,related_name='zbase',on_delete=models.CASCADE)
    # parent                      = TreeForeignKey('self', null=True, blank=True,on_delete=models.CASCADE, related_name='children', db_index=True)
    zone_name 					= models.CharField('分区名称',unique=True, max_length=64, blank=True, null=True)
    zone_area 					= models.FloatField('分区面积（平方公里）',blank=True, null=True)
    zone_water_in 				= models.FloatField('分区进水量（ m3）',blank=True, null=True)
    registed_user 				= models.FloatField('注册用户总数（万户）',blank=True, null=True)
    pipeline_length 			= models.FloatField('管线长度（ km）',blank=True, null=True)
    
    online_presspoint_num 		= models.FloatField('在线压力点数量（个）',blank=True, null=True)
    online_flowmeter_num 		= models.FloatField('在线流量计数量（个）',blank=True, null=True)
    online_water_quality_m_num 	= models.FloatField('在线水质监测点数量（个）',blank=True, null=True)
    
    charge_watermeter_num 		= models.FloatField('收费用远传水表数量（只）',blank=True, null=True)
    sub_zone_num 				= models.FloatField('下一级分区数量（个）',blank=True, null=True)
    dma_num 					= models.FloatField('分区中 DMA 数量（个）',blank=True, null=True)
    
    timestamp       			= models.DateTimeField(auto_now_add=True)
    updated         			= models.DateTimeField(auto_now=True)

    
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        db_table = 'zonebase'

    # class MPTTMeta:
    #     order_insertion_by = ['zone_name']
        
    def __unicode__(self):
        return self.zone_name

    def __str__(self):
        return self.zone_name

    def get_absolute_url(self): #get_absolute_url
        #return f"/restaurants/{self.slug}" 
        return reverse('dma:detail', kwargs={'slug': self.slug})


class ZoneMeasure(models.Model):
    zone_base           		= models.ForeignKey(ZoneBase,related_name='zmeasure',on_delete=models.CASCADE) # class_instance.model_set.all()
    measure_per_actual 			= models.FloatField('水表抄见率（ %）',blank=True, null=True)
    measure_precision 			= models.FloatField('抄表准确率（ %）',blank=True, null=True)
    zone_sale 					= models.FloatField('分区销售水量（ m3）',blank=True, null=True)
    nightflow_min 				= models.FloatField('夜间最小流量（ m3）',blank=True, null=True)
    charge_waterwater_percent 	= models.FloatField('收费用远传水表水量占分区销 水量比（ %）',blank=True, null=True)
    zone_detect_leak_num 		= models.FloatField('分区探出漏点总数（个）',blank=True, null=True)
    leak_water 					= models.FloatField('漏失水量（ m3）',blank=True, null=True)
    leak_obscur_water 			= models.FloatField('暗漏水量（ m3）',blank=True, null=True)
    leak_obvious_water 			= models.FloatField('明漏水量（ m3）',blank=True, null=True)
    leak_rate 					= models.FloatField('漏损率（ %）',blank=True, null=True)
    pressure_quality 			= models.FloatField('压力合格率（ %）',blank=True, null=True)
    water_quality 				= models.FloatField('水质合格率（ %）',blank=True, null=True)
    zone_inner_pressure 		= models.FloatField('分区内压力（ MPa）',blank=True, null=True)

    timestamp       			= models.DateTimeField() #auto_now_add=True
    updated         			= models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'zonemeasure'

    def __unicode__(self):
        return self.zone_base.zone_name



