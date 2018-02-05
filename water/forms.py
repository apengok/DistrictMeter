from django import forms
from django.utils.dateparse import parse_datetime
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget,AdminSplitDateTime

from . import models
import datetime

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
        print 'clean'
        self.cleaned_data['communityid'] = self.cleaned_data['community'].id
        print self.cleaned_data
        print self.cleaned_data['communityid']

    def save_existing(self, form, instance, commit=True):
        """Save and return an existing model instance for the given form."""
        print 'save_existing'
        return form.save(commit=commit)

    def save(self,commit=True):
        print self.instance,asdfasd
        instance = super(WatermeterForm, self).save(commit)
        print 'save:',instance