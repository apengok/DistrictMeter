# -*- coding: utf-8 -*-

from django import forms
from django.utils.dateparse import parse_datetime
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget,AdminSplitDateTime
from django.contrib.postgres.forms.ranges import DateRangeField, RangeWidget


from . import models
import datetime


class SearchForm(forms.Form):
    name = forms.CharField(max_length=120,initial='shenzhen')


class AnalyWaterForm(forms.Form):
    organization = forms.ChoiceField()
    station      = forms.ModelChoiceField(queryset=models.Tblfminfo.objects.all(),to_field_name='simid')
    readdate     = forms.ChoiceField()
    date         = forms.DateField(widget=AdminDateWidget())

    def __init__(self, *args, **kwargs):
        super(AnalyWaterForm, self).__init__(*args, **kwargs)

        organs = models.Tblfminfo.objects.all().distinct('filialename')
        fns = [f.filialename for f in organs]
        self.fields['organization'].choices = tuple(enumerate(fns))

        press_all = models.PressShareDayTax.objects.all().distinct('simid')

        pr_rtime = [x.readtime[:10] for x in press_all]
        self.fields['readdate'].choices = tuple(enumerate(pr_rtime))

        self.fields['organization'].initial = fns[1]
        self.fields['station'].initial = models.Tblfminfo.objects.first()
        self.fields['readdate'].initial = pr_rtime[0][:10]
        self.fields['date'].initial = pr_rtime[0][:10]

        # flows_all = models.FlowShareDayTax.objects.all().distinct('simid')

class DateRangeForm(forms.Form):
    date_range = DateRangeField(widget=RangeWidget(AdminDateWidget()))


class WatermeterForm(forms.ModelForm):
    the_id = forms.IntegerField(widget=forms.HiddenInput)
    # rtime = forms.DateField(widget=AdminSplitDateTime())
    # lastrtime = forms.DateField(widget=AdminSplitDateTime())
    
    class Meta:
        fields = ('nodeaddr','wateraddr','rvalue','fvalue','metertype','meterstate','commstate','rtime','lastrvalue','lastrtime','dosage','islargecalibermeter')
        model = models.Watermeter
        widgets = {
            'rtime':widgets.AdminSplitDateTime(),
            'lastrtime':widgets.AdminSplitDateTime()
        }

    def __init__(self, *args, **kwargs):
        super(WatermeterForm, self).__init__(*args, **kwargs)

        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields["the_id"].initial = instance.id

            # print self.instance.rtime,type(self.instance.rtime),instance.lastrtime
            # if isinstance(instance.rtime,unicode):
            #     self.fields['rtime'].initial = parse_datetime(instance.rtime)
            #     self.fields['lastrtime'].initial = parse_datetime(instance.lastrtime)

            #     print self.instance.rtime,type(self.instance.rtime),instance.rtime
        # self.initial['rtime'] = parse_datetime(self.instance.rtime)
        # self.instance.rtime = parse_datetime(self.instance.rtime)

        # print self.instance.rtime,type(self.instance.rtime)

    def clean(self):
        
        self.cleaned_data['communityid'] = self.cleaned_data['community'].id
        

    def save_existing(self, form, instance, commit=True):
        """Save and return an existing model instance for the given form."""
        
        return form.save(commit=commit)

    def save(self,commit=True):
        
        instance = super(WatermeterForm, self).save(commit)
        