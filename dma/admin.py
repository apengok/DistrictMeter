# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from dma.models import DmaZone,Measure

# Register your models here.

admin.site.register(DmaZone)
admin.site.register(Measure)