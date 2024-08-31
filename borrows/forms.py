from django.forms import ModelForm
from .models import Report


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['titel','description']

