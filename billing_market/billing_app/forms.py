from django import forms
from.models import CustomerInfo,Invoice,Products,Offers

class CustomerInfoForm(forms.ModelForm):
    class Meta:
        model=CustomerInfo
        fields=['customer_id','customer_name','customer_contact','customer_email','customer_address']
        widgets={
             'customer_id':forms.TextInput(attrs={'class':'form-control','id':'customerid'}),
            'customer_name':forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
            'customer_contact':forms.NumberInput(attrs={'class':'form-control','id':'contactid'}),
            'customer_email':forms.EmailInput(attrs={'class':'form-control','id':'emailid'}),
            'customer_address':forms.TextInput(attrs={'class':'form-control','id':'addressid'}),            
        }

class OffersForm(forms.ModelForm):
    class Meta:
        model=Offers
        fields='__all__'

class InvoiceForm(forms.ModelForm):
    class Meta:
        model=Invoice
        fields=['invoice_no','total_amount_without_gst','total_amount_without_offers','total_amount_with_gst_and_offers','customerinfo']
        widgets={
            'invoice_no':forms.NumberInput(attrs={'class':'form-control','id':'inumberid'}),
            'invoice_datetime':forms.DateInput(attrs={'class':'form-control','id':'dateid'}),
            'total_amount_without_gst':forms.NumberInput(attrs={'class':'form-control','id':'totalwithoutgstid'}),
            'total_amount_without_offers':forms.NumberInput(attrs={'class':'form-control','id':'totalwithoutofferid'}),
            'total_amount_with_gst_and_offers':forms.NumberInput(attrs={'class':'form-control','id':'totalwithgstandofferid'}),
                   
        }

class ProductsForm(forms.ModelForm):
    class Meta:
        model=Products
        fields='__all__'
        widgets={
            'product_id':forms.NumberInput(attrs={'class':'form-control','id':'productid'}),
            'product_quantity':forms.NumberInput(attrs={'class':'form-control','id':'quantityid'}),
            'product_price':forms.NumberInput(attrs={'class':'form-control','id':'priceid'}),
            'product_total_price':forms.NumberInput(attrs={'class':'form-control','id':'totalpriceid'}),
        }
