from django.shortcuts import redirect, render
from .models import ProductCategory, Suppliers, GST ,ProductInfo
from django.views import View
from .forms import ProductInfoForm,ProductCategoryForm,GSTForm,SuppliersForm
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView


# Create your views here.

class ProductCategoryView(View):
    template_name = 'inventory_app/procat_form.html'
    form = ProductCategoryForm

    def get(self, request):
        form = self.form()
        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_urls')
        
        context = {'form':form}
        print(".................")
        return render(request, self.template_name, context)


class ShowProductCategory(View):
    template_name = 'inventory_app/show_procat.html'
    def get(self, request):

        obj = ProductCategory.objects.all()
        template_name = 'inventory_app/show_procat.html'
        context = {'obj':obj}
        return render(request, template_name, context)

class UpdateProductcategory(View):
    template_name = 'inventory_app/procat_form.html'

    def get(self, request, pk):
        obj = ProductCategory.objects.get(product_category_id = pk)
        form = ProductCategoryForm(instance = obj)
        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request,pk):
        obj = ProductCategory.objects.get(product_category_id = pk)
        form = ProductCategoryForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_urls')
        context = {'form':form}
        return render(request, self.template_name, context)
    

class DeleteProductCategory(View):
    template_name = 'inventory_app/procat_confirmation.html'

    def get(self, request, pk):
        obj = ProductCategory.objects.get(product_category_id = pk)
        context = {'obj':obj}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        obj = ProductCategory.objects.get(product_category_id = pk)
        obj.delete()
        return redirect('show_urls')

       
        

class SuppliersView(View):
    template_name = 'inventory_app/suppliers_form.html'
    form = SuppliersForm

    def get(self, request):
        form=self.form()
        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showsuppliers_url')
        context = {'form':form}
        return render(request, self.template_name, context)


class ShowSuppliers(View):

    def get(self, request):

        obj = Suppliers.objects.all()
        template_name = 'inventory_app/show_suppliers.html'
        context = {'obj':obj}
        return render(request, template_name, context)

class UpdateSuppliers(View):
    template_name = 'inventory_app/suppliers_form.html'
    

    def get(self, request, pk):
        obj = Suppliers.objects.get(supplier_id= pk)
        form = SuppliersForm(instance = obj)
        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request,pk):
        obj = Suppliers.objects.get(supplier_id = pk)
        form = SuppliersForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showsuppliers_url')
        context = {'form':form}
        return render(request, self.template_name, context)


class DeleteSuppliers(View):
    template_name = 'inventory_app/suppliers_confirmation.html'

    def get(self, request, pk):
        obj = Suppliers.objects.get(supplier_id = pk)
        context = {'obj':obj}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        obj = Suppliers.objects.get(supplier_id = pk)
        obj.delete()
        return redirect('showsuppliers_url')

class ProductInfoView(View):
    template_name = 'inventory_app/productinfo_form.html'
    form = ProductInfoForm

    def get(self, request):
        form=self.form()
        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showProductInfo_url')
        context = {'form':form}
        return render(request, self.template_name, context)


class ShowProductInfo(View):

    def get(self, request):
        obj = ProductInfo.objects.all()
        template_name = 'inventory_app/showproductinfo.html'
        context = {'obj':obj}
        return render(request, template_name, context)

class UpdateProductInfo(View):
    template_name = 'inventory_app/productinfo_form.html'

    def get(self, request, pk):
        obj = ProductInfo.objects.get(product_id = pk)
        form =  ProductInfoForm(instance = obj)
        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        obj =  ProductInfo.objects.get(product_id = pk)
        form = ProductInfoForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showProductInfo_url')
        context = {'form':form}
        return render(request, self.template_name, context)


class DeleteProductInfo(View):
    template_name = 'inventory_app/productinfo_confirmation.html'

    def get(self, request, pk):
        obj = ProductInfo.objects.get(product_id = pk)
        context = {'obj':obj}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        obj = ProductInfo.objects.get(product_id = pk)
        obj.delete()
        return redirect('showProductInfo_url')

class GstView(ListView):
    model=GST
    fields='__all__'

class AddGst(CreateView):
    model=GST
    fields='__all__'
    success_url = reverse_lazy('showgst_url')

class UpdateGst(UpdateView):
    model=GST
    fields='__all__'
    success_url= reverse_lazy('showgst_url')

class DeleteGst(DeleteView):
    model=GST
    fields='__all__'
    success_url = reverse_lazy('showgst_url')
