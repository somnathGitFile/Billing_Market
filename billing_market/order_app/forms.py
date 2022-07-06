from dataclasses import fields
from pyexpat import model
from .models import Orders, Products, OrderSummery
from django import forms
from inventory_app.models import Suppliers,ProductInfo,GST,ProductCategory


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

class OrderSummeryForm(forms.ModelForm):
    class Meta:
        model = OrderSummery
        fields = '__all__'

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = '__all__'



class ProductInfoForm(forms.ModelForm):
    class Meta:
        model = ProductInfo
        fields = '__all__'

class GSTForm(forms.ModelForm):
    class Meta:
        model = GST
        fields = '__all__'


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'