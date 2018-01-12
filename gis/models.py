# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.db import models
from django.contrib.gis.db import models

# Create your models here.


class AlarmShareDayTax(models.Model):
    pid = models.IntegerField(primary_key=True)
    readtime = models.CharField(max_length=20)
    simid = models.CharField(max_length=20)
    flux = models.FloatField(blank=True, null=True)
    totalflux = models.FloatField(blank=True, null=True)
    pressure = models.FloatField(blank=True, null=True)
    warning = models.CharField(max_length=50)
    warningdesc = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'alarm_share_day_tax'


class Amrsparam(models.Model):
    paramkey = models.CharField(primary_key=True, max_length=64)
    paramvalue = models.CharField(max_length=64)

    class Meta:
        managed = True
        db_table = 'amrsparam'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DmDeviceType(models.Model):
    typename = models.CharField(primary_key=True, max_length=100)
    tablename = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = True
        db_table = 'dm_device_type'


class DmEnumConfig(models.Model):
    tablename = models.CharField(primary_key=True, max_length=100)
    fieldname = models.CharField(max_length=100)
    itemid = models.IntegerField()
    itemcaption = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'dm_enum_config'
        unique_together = (('tablename', 'fieldname', 'itemid'),)


class DmFieldsConfig(models.Model):
    tablename = models.CharField(primary_key=True, max_length=100)
    fieldname = models.CharField(max_length=100)
    fieldcaption = models.CharField(max_length=100, blank=True, null=True)
    fieldlength = models.IntegerField(blank=True, null=True)
    fieldtype = models.IntegerField()
    fieldisrequired = models.CharField(max_length=1)
    fieldisunique = models.CharField(max_length=1, blank=True, null=True)
    fieldisprimary = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dm_fields_config'
        unique_together = (('tablename', 'fieldname'),)


class DmGlobalDevice(models.Model):
    deviceid = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    type = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dm_global_device'


class FlowShareDayTax(models.Model):
    pid = models.IntegerField(primary_key=True)
    readtime = models.CharField(max_length=20)
    simid = models.CharField(max_length=20)
    flux = models.FloatField(blank=True, null=True)
    plustotalflux = models.FloatField(blank=True, null=True)
    reversetotalflux = models.FloatField(blank=True, null=True)
    warning = models.CharField(max_length=50)
    warningdesc = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'flow_share_day_tax'


class GCloudlayer(models.Model):
    layername = models.CharField(max_length=200)
    tablename = models.CharField(max_length=200)
    layerdesc = models.CharField(max_length=250, blank=True, null=True)
    fastquery = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer'


class GCloudlayerMetaDlzxc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_dlzxc'


class GCloudlayerMetaDmdc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_dmdc'


class GCloudlayerMetaDmxc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_dmxc'


class GCloudlayerMetaDwjcdc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_dwjcdc'


class GCloudlayerMetaFzdc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_fzdc'


class GCloudlayerMetaFzxc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_fzxc'


class GCloudlayerMetaGxdc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_gxdc'


class GCloudlayerMetaGxxc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_gxxc'


class GCloudlayerMetaJmddc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_jmddc'


class GCloudlayerMetaJmdmc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_jmdmc'


class GCloudlayerMetaJmdxc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_jmdxc'


class GCloudlayerMetaJtdc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_jtdc'


class GCloudlayerMetaJtmc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_jtmc'


class GCloudlayerMetaJtxc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_jtxc'


class GCloudlayerMetaMczjc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_mczjc'


class GCloudlayerMetaSxGsWsConcentrator(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.GeometryField(srid=0)
    user_define = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sx_gs_ws_concentrator'


class GCloudlayerMetaSxGsWsConnector(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.GeometryField(srid=0)
    user_define = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sx_gs_ws_connector'


class GCloudlayerMetaSxGsWsDrainValve(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.GeometryField(srid=0)
    user_define = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sx_gs_ws_drain_valve'


class GCloudlayerMetaSxGsWsExEquipment(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.GeometryField(srid=0)
    user_define = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sx_gs_ws_ex_equipment'


class GCloudlayerMetaSxGsWsFireHydrant(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.GeometryField(srid=0)
    user_define = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sx_gs_ws_fire_hydrant'


class GCloudlayerMetaSxGsWsFlowMeter(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.GeometryField(srid=0)
    user_define = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sx_gs_ws_flow_meter'


class GCloudlayerMetaSxGsWsForcePump(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.GeometryField(srid=0)
    user_define = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sx_gs_ws_force_pump'


class GCloudlayerMetaSxGsWsMetabox(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.GeometryField(srid=0)
    user_define = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sx_gs_ws_metabox'


class GCloudlayerMetaSxGsWsPipe(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.GeometryField(srid=0)
    user_define = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sx_gs_ws_pipe'


class GCloudlayerMetaSxGsWsSourceWater(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.GeometryField(srid=0)
    user_define = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sx_gs_ws_source_water'


class GCloudlayerMetaSxGsWsValve(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.GeometryField(srid=0)
    user_define = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sx_gs_ws_valve'


class GCloudlayerMetaSxGsWsValveWell(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.GeometryField(srid=0)
    user_define = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sx_gs_ws_valve_well'


class GCloudlayerMetaSxGsWsVentValve(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.GeometryField(srid=0)
    user_define = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sx_gs_ws_vent_valve'


class GCloudlayerMetaSxGsWsWaterMeter(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.GeometryField(srid=0)
    user_define = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sx_gs_ws_water_meter'


class GCloudlayerMetaSxGsWsWatermeterBasin(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.GeometryField(srid=0)
    user_define = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sx_gs_ws_watermeter_basin'


class GCloudlayerMetaSxQdzdtMapLayer(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    user_define = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sx_qdzdt_map_layer'


class GCloudlayerMetaSxdc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sxdc'


class GCloudlayerMetaSxmc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sxmc'


class GCloudlayerMetaSxxc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sxxc'


class GCloudlayerMetaSxzxc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_sxzxc'


class GCloudlayerMetaZbdc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_zbdc'


class GCloudlayerMetaZbmc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_zbmc'


class GCloudlayerMetaZbxc(models.Model):
    metaid = models.IntegerField(primary_key=True)
    metaname = models.CharField(max_length=200, blank=True, null=True)
    bounds_size = models.FloatField(blank=True, null=True)
    blockdata = models.BinaryField(blank=True, null=True)
    bounds_geom = models.PolygonField(srid=0)
    geomdata = models.GeometryField(srid=0, blank=True, null=True)
    geomjson = models.TextField(blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    user_define = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'g_cloudlayer_meta_zbxc'


class HdbTianhouBig(models.Model):
    id = models.IntegerField(primary_key=True)
    rvalue = models.CharField(max_length=30, blank=True, null=True)
    fvalue = models.CharField(max_length=30, blank=True, null=True)
    meterstate = models.CharField(max_length=30, blank=True, null=True)
    commstate = models.CharField(max_length=30, blank=True, null=True)
    rtime = models.CharField(max_length=30, blank=True, null=True)
    lastrvalue = models.CharField(max_length=30, blank=True, null=True)
    lastrtime = models.CharField(max_length=30, blank=True, null=True)
    dosage = models.CharField(max_length=30, blank=True, null=True)
    user_watermeter_id = models.CharField(max_length=32)

    class Meta:
        managed = True
        db_table = 'hdb_tianhou_big'


class Hdbrecord(models.Model):
    id = models.IntegerField(primary_key=True)
    hdate = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hdbrecord'


class PressShareDayTax(models.Model):
    pid = models.IntegerField(primary_key=True)
    readtime = models.CharField(max_length=20)
    simid = models.CharField(max_length=20)
    pressure = models.FloatField(blank=True, null=True)
    warning = models.CharField(max_length=50)
    warningdesc = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'press_share_day_tax'


class UserWatermeter(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    numbersth = models.CharField(max_length=30, blank=True, null=True)
    roomname = models.CharField(max_length=128, blank=True, null=True)
    nodeaddr = models.CharField(max_length=30, blank=True, null=True)
    wateraddr = models.CharField(max_length=30, blank=True, null=True)
    rvalue = models.CharField(max_length=30, blank=True, null=True)
    metertype = models.CharField(max_length=30, blank=True, null=True)
    fvalue = models.CharField(max_length=30, blank=True, null=True)
    meterstate = models.CharField(max_length=30, blank=True, null=True)
    commstate = models.CharField(max_length=30, blank=True, null=True)
    rtime = models.CharField(max_length=30, blank=True, null=True)
    lastrvalue = models.CharField(max_length=30, blank=True, null=True)
    lastrtime = models.CharField(max_length=30, blank=True, null=True)
    dosage = models.CharField(max_length=30, blank=True, null=True)
    islargecalibermeter = models.IntegerField(blank=True, null=True)
    metering_equipment_id = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'user_watermeter'



class WsConcentrator(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    community = models.CharField(unique=True, max_length=128, blank=True, null=True)
    address = models.CharField(unique=True, max_length=128, blank=True, null=True)
    commdev = models.CharField(max_length=30, blank=True, null=True)
    devaddr = models.CharField(max_length=30, blank=True, null=True)
    commmodel = models.CharField(max_length=64, blank=True, null=True)
    commparam = models.CharField(max_length=64, blank=True, null=True)
    tel = models.CharField(max_length=30, blank=True, null=True)
    netparam = models.CharField(max_length=30, blank=True, null=True)
    manufacturer = models.CharField(max_length=32, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_concentrator'


class WsConnector(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_connector'


class WsDrainValve(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_drain_valve'


class WsExEquipment(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_ex_equipment'


class WsExResourceProperty(models.Model):
    tablename = models.CharField(primary_key=True, max_length=128)
    fieldname = models.CharField(max_length=128)
    fieldtype = models.IntegerField(blank=True, null=True)
    fieldlength = models.IntegerField(blank=True, null=True)
    caption = models.CharField(unique=True, max_length=128, blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    mapping_column_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_ex_resource_property'
        unique_together = (('tablename', 'fieldname'),)


class WsExResourcePropertyEnumDefine(models.Model):
    tablename = models.CharField(primary_key=True, max_length=128)
    fieldname = models.CharField(max_length=128)
    enumvalue = models.IntegerField()
    enumcaption = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'ws_ex_resource_property_enum_define'
        unique_together = (('tablename', 'fieldname', 'enumvalue'),)


class WsExResourceType(models.Model):
    tablename = models.CharField(primary_key=True, max_length=128)
    caption = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_ex_resource_type'


class WsFireHydrant(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_fire_hydrant'


class WsFlowMeter(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    simid = models.CharField(max_length=20, blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_flow_meter'


class WsForcePump(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_force_pump'


class WsMetabox(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    buildingno = models.CharField(max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    concentrator_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_metabox'


class WsPipe(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    pipe_first = models.CharField(max_length=20, blank=True, null=True)
    pipe_end = models.CharField(max_length=20, blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    buried = models.FloatField(blank=True, null=True)
    start_depth = models.FloatField(blank=True, null=True)
    end_depth = models.FloatField(blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    start_altitude = models.FloatField(blank=True, null=True)
    end_altitude = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_pipe'


class WsPipeType(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_pipe_type'


class WsProjectInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    number = models.CharField(max_length=64)
    project_name = models.CharField(max_length=255)
    manager_unit = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    completion_time = models.CharField(max_length=20, blank=True, null=True)
    measurement_unit = models.CharField(max_length=64, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    input_staff_id = models.CharField(max_length=32, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    minx = models.FloatField(blank=True, null=True)
    miny = models.FloatField(blank=True, null=True)
    maxx = models.FloatField(blank=True, null=True)
    maxy = models.FloatField(blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff_id = models.CharField(max_length=32, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_project_info'
        unique_together = (('id', 'number'),)


class WsProjectMeasurementRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    project_id = models.CharField(max_length=32)
    equipement_id = models.CharField(max_length=20)
    type = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'ws_project_measurement_record'


class WsResource(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    tablename = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'ws_resource'


class WsSourceWater(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_source_water'


class WsUserOpCascadeLog(models.Model):
    id = models.IntegerField(primary_key=True)
    op_mode = models.IntegerField(blank=True, null=True)
    topo_old = models.CharField(max_length=62, blank=True, null=True)
    topo_old_points = models.CharField(max_length=255, blank=True, null=True)
    topo_new = models.CharField(max_length=62, blank=True, null=True)
    topo_new_points = models.CharField(max_length=255, blank=True, null=True)
    attr_id = models.CharField(max_length=20, blank=True, null=True)
    attr_tablename = models.CharField(max_length=128, blank=True, null=True)
    meta_id = models.IntegerField(blank=True, null=True)
    meta_tablename = models.CharField(max_length=128, blank=True, null=True)
    op_cascade_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_user_op_cascade_log'


class WsValve(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_valve'


class WsValveWell(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_valve_well'


class WsVentValve(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_vent_valve'


class WsWaterMeter(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_water_meter'


class WsWatermeterBasin(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ws_watermeter_basin'
