from .models import ProductInfo,ProductCategory,Suppliers,GST
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class SuppliersForm(forms.ModelForm):
    supplier_contact=PhoneNumberField(max_length=13,widget=PhoneNumberPrefixWidget(initial='IN'))
    class Meta:
        model = Suppliers
        fields = '__all__'
        labels = {

            'supplier_id': 'SUPPLIER ID',
            'supplier_name': 'SUPPLIER NAME',
            'supplier_address': 'SUPPLIER ADDRESS',
            'supplier_contact': 'SUPPLIER CONTACT',
            'supplier_email': 'SUPPLIER EMAIL',
            'supplier_company':'SUPPLIER COMPANY'
        }

class GSTForm(forms.ModelForm):
    class Meta:
        model = GST
        fields = '__all__'

class ProductInfoForm(forms.ModelForm):
    class Meta:
        model = ProductInfo
        fields = '__all__'
       
