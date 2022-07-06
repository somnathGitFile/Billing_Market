from django.db import models
from inventory_app.models import ProductInfo

# Create your models here.
class CustomerInfo(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.IntegerField()
    customer_email = models.EmailField()
    customer_address = models.TextField()
    #class Meta:
        #managed = False
    
class Invoice(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    invoice_no = models.IntegerField(unique=True)
    invoice_datetime = models.DateTimeField()
    total_amount_without_gst = models.FloatField()
    total_amount_without_offers = models.FloatField()
    total_amount_with_gst_and_offers = models.FloatField()
    customerinfo = models.ForeignKey(CustomerInfo,on_delete=models.CASCADE)
    
class Products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_info = models.ForeignKey(ProductInfo,related_name='ordered_product',on_delete=models.CASCADE)
    product_quantity = models.FloatField()
    product_price = models.FloatField()
    product_total_price = models.FloatField()
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    
class Offers(models.Model):
    offer_id = models.IntegerField(primary_key=True)
    offer_name = models.CharField(max_length=50)
    offer_start_date = models.DateTimeField()
    offer_end_date = models.DateTimeField()
    discount_in_percentile = models.FloatField()
    discount_in_price = models.FloatField()
    productinfo = models.ManyToManyField(ProductInfo)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
	
