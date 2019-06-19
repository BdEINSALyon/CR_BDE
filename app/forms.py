from django.forms import ModelForm
from app.models import Report


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['date', 'media', 'type', 'year', 'is_public']