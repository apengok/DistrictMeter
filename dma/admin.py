# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from dma.models import ZoneTree,ZoneBase,ZoneMeasure

# Register your models here.

admin.site.register(ZoneTree)
admin.site.register(ZoneBase)
admin.site.register(ZoneMeasure)