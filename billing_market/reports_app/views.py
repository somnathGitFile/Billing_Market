from django.shortcuts import render
from .forms import DailySaleReportForm
from .models import DailySaleReport

# Create your views here.
def DailySaleReportView(request):
    form = DailySaleReportForm()
    template_name = 'dailysalereport.html'
    context = {'form': form}
    return render(request, template_name, context)
