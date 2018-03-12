
from django import forms

from .models import ZoneTree,ZoneBase,ZoneMeasure

from .widgets import CustomZoneWidget
# from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget,AdminSplitDateTime
from django.contrib.postgres.forms.ranges import DateRangeField, RangeWidget

class JoinForm(forms.Form):
    email   = forms.EmailField()
    name    = forms.CharField(max_length=120)
    test_date = forms.DateField(widget=AdminDateWidget)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email == 'apengok@163.com1':
            raise forms.ValidationError("this is super man")
        return email



class MeasureForm(forms.ModelForm):
    """docstring for MeasureForm""" 
    # zone_base=forms.ModelChoiceField(queryset=ZoneBase.objects.all())

    class Meta:
        model = ZoneMeasure
        fields = [
            'zone_base',
            'measure_per_actual',      
            'measure_precision',       
            'zone_sale',
            'nightflow_min',
            'charge_waterwater_percent',
            'zone_detect_leak_num',
            'leak_water',
            'leak_obscur_water',
            'leak_obvious_water',
            'leak_rate',
            'pressure_quality',
            'water_quality',
            'zone_inner_pressure',
            'timestamp'
        ]

        widgets = {
            #'zone_base':CustomZoneWidget(ZoneBase), #Textarea(attrs={'cols': 80, 'rows': 20})
            'timestamp':AdminDateWidget
        }
    def __init__(self, *args,**kwargs):
        super(MeasureForm, self).__init__(*args,**kwargs)#http://127.0.0.1:1080/pac?t=201801191012346085
        slug=kwargs.get('slug')
        if slug:
            current_zone = ZoneTree.objects.get(slug=slug)
        else:
            current_zone = ZoneTree.objects.first()

        
        self.fields['zone_base'].queryset = ZoneBase.objects.all()    #filter(zonetree=current_zone)# .exclude(item__isnull=False)