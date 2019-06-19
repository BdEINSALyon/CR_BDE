from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput
from .models import Report
from django.utils import timezone


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['date', 'file', 'type', 'year', 'is_public']
        widgets = {'date':DatePickerInput(format='%d/%m/%Y', options={
        "showClose": False,
        "showClear": False,
        "showTodayButton": False,
        "locale": "fr",
        "defaultDate": timezone.now().isoformat()})}