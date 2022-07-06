from multiprocessing import context
from django.shortcuts import render
from .forms import CustomerInfoForm,ProductsForm,InvoiceForm,OffersForm
from .models import *

# Create your views here.

def CreateInvoice(request):
    form=CustomerInfoForm()
    form1=InvoiceForm()
    form2=ProductsForm()
    template_name='CreateInovice.html'
    if request.method == 'POST':
        form=CustomerInfoForm(request.POST)
        if form.is_valid():
            form.save()
    if request.method == 'POST':        
        form1=InvoiceForm(request.POST)
        if form1.is_valid():
            form1.save()
    if request.method == 'POST':        
        form2=ProductsForm(request.POST)
        
        
        if form2.is_valid():
            form2.save()

    context={'form':form,'form1':form1,'form2':form2}
    return render(request,template_name,context)