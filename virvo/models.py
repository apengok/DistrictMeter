# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.

class Organization(MPTTModel):
    name    = models.CharField(max_length=50, unique=True)
    parent  = TreeForeignKey('self', null=True, blank=True,on_delete=models.CASCADE, related_name='children', db_index=True)
    # slug    = models.SlugField()
    
    # def get_absolute_url(self):
    #     return reverse('sub_dma', kwargs={'path': self.get_path()})

    def get_absolute_url(self): #get_absolute_url
        return "/organ/{}".format(self.pk)
        # return reverse('virvo:detail', kwargs={'slug': self.slug})

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        
        # unique_together = ('slug', 'parent')
        db_table = 'organization'
    

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class DMABaseinfo(models.Model):
    dma_no        = models.CharField('分区编号',max_length=50, unique=True)
    pepoles_num   = models.CharField('服务人口',max_length=50, null=True,blank=True)
    acreage       = models.CharField('服务面积',max_length=50, null=True,blank=True)
    user_num      = models.CharField('用户数量',max_length=50, null=True,blank=True)
    pipe_texture  = models.CharField('管道材质',max_length=50, null=True, blank=True)
    pipe_length   = models.CharField('管道总长度(m)',max_length=50, null=True, blank=True)
    pipe_links    = models.CharField('管道连接总数(个)',max_length=50,null=True, blank=True)
    pipe_years    = models.CharField('管道最长服务年限(年)',max_length=50,null=True, blank=True)
    pipe_private  = models.CharField('私人拥有水管长度(m)',max_length=50,blank=True,null=True)
    ifc           = models.CharField('IFC参数',max_length=250, null=True, blank=True)
    aznp          = models.CharField('AZNP',max_length=250,null=True, blank=True)
    night_use     = models.CharField('正常夜间用水量',max_length=50,null=True, blank=True)
    cxc_value     = models.CharField('产销差目标值',max_length=50, null=True, blank=True)

    dma = models.OneToOneField(
        Organization,
        on_delete=models.CASCADE,
        # primary_key=True,
    )

    class Meta:
        
        unique_together = ('dma_no', )
        db_table = 'dmabaseinfo'

    def get_absolute_url(self): #get_absolute_url
        # return "/organ/{}".format(self.pk)
        return reverse('virvo:dma_manager', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.dma_no

    def __str__(self):
        return self.dma_no


class Stations(models.Model):
    station_name    = models.CharField('站点名称',max_length=50, unique=True)
    station_type    = models.CharField('类型',max_length=50, unique=True)
    meter_property  = models.CharField('用水性质',max_length=50,  null=True, blank=True)
    meter_type      = models.CharField('表具类型',max_length=50,  null=True, blank=True)
    meter_code      = models.CharField('表具编号',max_length=50,  null=True, blank=True)
    simno           = models.CharField('SIM卡号',max_length=50,  null=True, blank=True)
    caliber         = models.CharField('口径',max_length=50,  null=True, blank=True)
    big_user        = models.BooleanField('大用户',max_length=50, blank=True)
    focus           = models.BooleanField('重点关注',max_length=50, blank=True)
    installed       = models.DateField('安装日期',auto_now=True)

    belongto        = models.ForeignKey(Organization,verbose_name='所属组织',related_name='station',on_delete=models.CASCADE) #class_instance.model_set.all()

    

    class Meta:
        
        unique_together = ('meter_code', 'simno')
        db_table = 'stations'

    def __unicode__(self):
        return self.station_name

    def __str__(self):
        return self.station_name
    

