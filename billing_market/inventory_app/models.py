from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class ProductCategory(models.Model):
    product_category_id = models.IntegerField(primary_key=True)
    product_category_name = models.CharField(max_length=50)
 
class Suppliers(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    supplier_name = models.CharField(max_length=50)
    supplier_address = models.TextField()
    supplier_contact = PhoneNumberField()
    supplier_email = models.EmailField()
    supplier_company = models.CharField(max_length=50)
    
    
class GST(models.Model):
    gst_id = models.IntegerField(primary_key=True)
    gst_no = models.IntegerField()
    cgst = models.FloatField()
    sgst = models.FloatField()
    igst = models.FloatField()
    
    
class ProductInfo(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_hsn = models.IntegerField()
    manufacturer = models.CharField(max_length=50)
    date_of_manufacturing = models.DateTimeField()
    product_description = models.CharField(max_length=50)
    country_of_origin = models.CharField(max_length=50)
    product_price_without_gst = models.FloatField()
    product_quantity = models.FloatField()
    gst = models.ForeignKey(GST,on_delete=models.CASCADE)
    suppliers = models.ForeignKey(Suppliers,on_delete=models.CASCADE)
    

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
