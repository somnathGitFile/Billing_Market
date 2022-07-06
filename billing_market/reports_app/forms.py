from django import forms
from .models import DailySaleReport, DailyPurchaseReport


class DailySaleReportForm(forms.ModelForm):
    class Meta:
        model = DailySaleReport
        fields = '__all__'

class DailyPurchaseReportForm(forms.ModelForm):
    class Meta:
        model = DailyPurchaseReport
        fields = '__all__'   