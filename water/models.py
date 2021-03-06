# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.html import format_html

# Create your models here.
class District(models.Model):
    pid = models.IntegerField(db_column='Id',primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=128, blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = True
        db_table = 'district'        
        
    
    def __unicode__(self):
        return self.name


'''
Django In postgresql legacy database, bind model with table primary key to autoincrement
1.add new sequence
create sequence public.Community_id_seq
    start 1
    increment 1
    NO MAXVALUE
    CACHE 1;
ALTER TABLE public.Community_id_seq
OWNER TO scada;

 If there is no data in the table, leave the sequence as it is, don't make any changes. Just save it. If there is existing data, add the last or highest value in the primary key column to the Current value

2.add the line nextval('your_sequence_name'::regclass) to the Default value in your primary key
'''        

class Community(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=128, blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.
    # districtid = models.IntegerField(db_column='DistrictId', blank=True, null=True)  # Field name made lowercase.
    districtid = models.ForeignKey(District,db_column='DistrictId', blank=True, null=True,on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'community'


    def __unicode__(self):
        return self.name


class FlowShareDayTax(models.Model):
    pid = models.AutoField(db_column='PID', primary_key=True)  # Field name made lowercase.
    readtime = models.DateTimeField(db_column='ReadTime', max_length=20)  # Field name made lowercase.
    simid = models.CharField(db_column='SIMID', max_length=20)  # Field name made lowercase.
    flux = models.FloatField(db_column='Flux', blank=True, null=True)  # Field name made lowercase.
    plustotalflux = models.FloatField(db_column='PlusTotalFlux', blank=True, null=True)  # Field name made lowercase.
    reversetotalflux = models.FloatField(db_column='ReverseTotalFlux', blank=True, null=True)  # Field name made lowercase.
    warning = models.CharField(db_column='Warning', max_length=50)  # Field name made lowercase.
    warningdesc = models.CharField(db_column='WarningDesc', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'flow_share_day_tax'

    def __unicode__(self):
        return self.simid

    # @property
    # def extra(self):
    #     label_str = '''
    #         <button type = "button" class = "btn btn-primary"><a href="?pid=%s">Alter</a></button>
    #     ''' % (str(self.pid))
    #     return format_html(label_str)


class PressShareDayTax(models.Model):
    pid = models.AutoField(db_column='PID', primary_key=True)  # Field name made lowercase.
    readtime = models.DateTimeField(db_column='ReadTime', max_length=20)  # Field name made lowercase.
    simid = models.CharField(db_column='SIMID', max_length=20)  # Field name made lowercase.
    pressure = models.FloatField(db_column='Pressure', blank=True, null=True)  # Field name made lowercase.
    warning = models.CharField(db_column='Warning', max_length=50)  # Field name made lowercase.
    warningdesc = models.CharField(db_column='WarningDesc', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'press_share_day_tax'

    def __unicode__(self):
        return self.simid


class Tblfminfo(models.Model):
    precinctname = models.CharField(db_column='PrecinctName', max_length=50)  # Field name made lowercase.
    filialename = models.CharField(db_column='FilialeName', max_length=50)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=20)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=20)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.
    useraddress = models.CharField(db_column='UserAddress', max_length=50)  # Field name made lowercase.
    simid = models.CharField(db_column='SIMID', primary_key=True, max_length=20)  # Field name made lowercase.
    fmtype = models.CharField(db_column='FMType', max_length=50)  # Field name made lowercase.
    fmaddress = models.CharField(db_column='FMAddress', max_length=20)  # Field name made lowercase.
    installdate = models.DateField(db_column='InstallDate', max_length=20)  # Field name made lowercase.
    install_jd = models.CharField(db_column='Install_JD', max_length=10)  # Field name made lowercase.
    install_wd = models.CharField(db_column='Install_WD', max_length=10)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime', max_length=20)  # Field name made lowercase.
    lastreadtime = models.DateTimeField(db_column='LastReadTime', max_length=20)  # Field name made lowercase.
    lastflux = models.FloatField(db_column='LastFlux', blank=True, null=True)  # Field name made lowercase.
    lasttotalflux = models.FloatField(db_column='LastTotalFlux', blank=True, null=True)  # Field name made lowercase.
    lastpressure = models.FloatField(db_column='LastPressure', blank=True, null=True)  # Field name made lowercase.
    lastwarning = models.CharField(db_column='LastWarning', max_length=50)  # Field name made lowercase.
    lastwarningdesc = models.CharField(db_column='LastWarningDesc', max_length=20)  # Field name made lowercase.
    lastwarningtime = models.DateTimeField(db_column='LastWarningTime', max_length=20)  # Field name made lowercase.
    lastreadpressuretime = models.DateTimeField(db_column='LastReadPressureTime', max_length=20)  # Field name made lowercase.
    lastreadfluxtime = models.DateTimeField(db_column='LastReadFluxTime', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblfminfo'
        
    def __unicode__(self):
        return self.username


class Watermeter(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.DateTimeField(db_column='RTime',  blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.DateTimeField(db_column='LastRTime', blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    # communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    communityid = models.ForeignKey(Community,db_column='CommunityId',blank=True, null=True,on_delete=models.CASCADE) 
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'watermeter'
        unique_together = (('nodeaddr', 'wateraddr'),)

    def __unicode__(self):
        return '%s%s'%(self.buildingname,self.roomname)


class HdbTianhouBig(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.DateTimeField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    watermeterid = models.ForeignKey(Watermeter,db_column='WaterMeterId', blank=True, null=True,on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'hdb_tianhou_big'

    def __unicode__(self):
        return self.watermeterid

