from multiprocessing import context
from re import template
from django.views import View
from django.shortcuts import render,redirect
from .forms import OrderForm, ProductForm, OrderSummeryForm, SupplierForm,ProductInfoForm,GSTForm,ProductCategoryForm
from .models import Orders,Suppliers,Products,GST,ProductInfo,ProductCategory

# Create your views here.
class OrderView(View):
    template_name = 'order_app/purchaseorder.html'
    form1 = OrderForm


    def get(self, request):
        form1 = self.form1()
        context = {'form1': form1}
        return render(request, self.template_name, context)

    def post(self, request):
        form1 = self.form1(request.POST)
        if form1.is_valid():
            form1.save()
        context = {'form1': form1}
        return render(request, self.template_name, context)


class SupplierView(View):
    template_name = 'order_app/addsupplier.html'
    form = SupplierForm

    def get(self, request):
        form = self.form()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form}
        return render(request, self.template_name, context)

class ShowOrderView(View):
    template_name='order_app/ShowOrder.html'

    def get(self,request):

        obj = Orders.objects.all()
        context = {'obj':obj}
        return render(request,self.template_name,context)



class ShowSupplierView(View):
    template_name='order_app/ShowSupplier.html'

    def get(self,request):

        obj = Suppliers.objects.all()
        context = {'obj':obj}
        return render(request,self.template_name,context)



class SupplierUpdateview(View):
    template_name='order_app/addsupplier.html'
    form = SupplierForm

    def get(self,request,pk):
        obj=Suppliers. objects.get(pk=pk)
        form = self.form(instance=obj)
        context={'form':form}
        return render(request,self.template_name,context)

    def post(self,request,pk):
        obj = Suppliers.objects.get(pk=pk)
        form = self.form(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showsupplier_url')
        context={'form':form}
        return render(request,self.template_name,context)

class SupplierDeleteview(View):
    template_name='order_app/confirmation.html'
    def get(self,request,pk):
        obj=Suppliers.objects.get(pk=pk)
        context={'obj':obj}
        return render(request,self.template_name,context)

    def post(self,request,pk):
        obj=Suppliers.objects.get(pk=pk)
        obj.delete()
        context={'obj':obj}
        return redirect('showsupplier_url')



class ProductView(View):
    template_name = 'order_app/productadd.html'
    form = ProductForm

    def get(self, request):
        form = self.form()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
        return render(request, self.template_name, context)


class ShowProductView(View):
    template_name='order_app/ShowProduct.html'

    def get(self,request):

        obj = Products.objects.all()
        context = {'obj':obj}
        return render(request,self.template_name,context)


class ProductInfoView(View):
    template_name = 'order_app/productInfo.html'
    form = ProductInfoForm

    def get(self, request):
        form = self.form()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
        return render(request, self.template_name, context)



class GSTView(View):
    template_name = 'order_app/gst.html'
    form = GSTForm

    def get(self, request):
        form = self.form()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
        return render(request, self.template_name, context)





class ProductCategoryView(View):
    template_name = 'order_app/ProductCategory.html'
    form = ProductCategoryForm

    def get(self, request):
        form = self.form()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
        return render(request, self.template_name, context)






'''
class OrderSummeryView(View):
    template_name = 'order_app/purchaseorder.html'
    form = OrderSummeryForm

    def get(self, request):
        form = self.form()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
        return render(request, self.template_name, context)
        '''