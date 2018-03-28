# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.

class Organization(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True,on_delete=models.CASCADE, related_name='children', db_index=True)
    slug = models.SlugField()
    
    # def get_absolute_url(self):
    #     return reverse('sub_dma', kwargs={'path': self.get_path()})

    def get_absolute_url(self): #get_absolute_url
        return "/organ/{}".format(self.slug)
        # return reverse('virvo:detail', kwargs={'slug': self.slug})

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        
        unique_together = ('slug', 'parent')
        db_table = 'organization'
    

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Stations(models.Model):
    station_name = models.CharField('站点名称',max_length=50, unique=True)
    meter_property = models.CharField('用水性质',max_length=50, blank=True)
    meter_type = models.CharField('表具类型',max_length=50, blank=True)
    meter_code = models.CharField('表具编号',max_length=50, null=True)
    simno = models.CharField('SIM卡号',max_length=50, unique=True)
    caliber = models.CharField('口径',max_length=50, null=True)
    big_user = models.BooleanField('大用户',max_length=50, blank=True)
    focus = models.BooleanField('重点关注',max_length=50, blank=True)
    installed = models.DateField('安装日期',auto_now=True)

    belongto = models.ForeignKey(Organization,verbose_name='所属组织',related_name='station',on_delete=models.CASCADE)

    class Meta:
        
        unique_together = ('meter_code', 'simno')
        db_table = 'stations'

    def __unicode__(self):
        return self.station_name

    def __str__(self):
        return self.station_name
    
