from django import forms
from django.forms.widgets import SplitDateTimeWidget
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget,AdminSplitDateTime

from django.utils.translation import ugettext as _

class StringDateTimeWidget(SplitDateTimeWidget):

    def __init__(self, attrs=None, date_format=None, time_format=None):
        
        super(StringDateTimeWidget, self).__init__()

    def decompress(self,value):
        #allowed datetime string render in datatiemfield pengwl 2018.02.05
        if isinstance(value,unicode) or isinstance(value,str):
            return [value[:10],value[11:19]]
        if value:
            value = to_current_timezone(value)
            return [value.date(), value.time().replace(microsecond=0)]
        return [None, None]




class StringSplitDateTime(StringDateTimeWidget):
    """
    A SplitDateTime Widget that has some admin-specific styling.
    """
    template_name = 'admin/widgets/split_datetime.html'

    def __init__(self, attrs=None):
        widgets = [AdminDateWidget, AdminTimeWidget]
        # Note that we're calling MultiWidget, not SplitDateTimeWidget, because
        # we want to define widgets.
        forms.MultiWidget.__init__(self, widgets, attrs)

    def get_context(self, name, value, attrs):
        context = super(StringSplitDateTime, self).get_context(name, value, attrs)
        context['date_label'] = _('Date:')
        context['time_label'] = _('Time:')
        return context        