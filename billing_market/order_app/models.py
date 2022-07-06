from django.db import models
from inventory_app.models import Suppliers,ProductInfo


# Create your models here.

class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_status = models.CharField(max_length=50)
    total_quantity_of_products = models.IntegerField()
    total_price_of_products_without_gst = models.FloatField()
    total_price_of_products_with_gst  = models.FloatField()
    supplier = models.ForeignKey(Suppliers,on_delete=models.CASCADE)
    
    
class Products(models.Model):
    product_id  = models.IntegerField(primary_key=True)
    product_info = models.ForeignKey(ProductInfo,on_delete=models.CASCADE)
    product_quantity =models.IntegerField()
    product_price_per_unit  = models.FloatField()
    total_product_price = models.FloatField()
    order = models.ForeignKey(Orders,on_delete=models.CASCADE)
    

class OrderSummery (models.Model):
    order_summery_id = models.IntegerField(primary_key=True)
    order_delivery_date = models.DateTimeField()
    order = models.ForeignKey(Orders,on_delete=models.CASCADE)
    
    
    
    
    
    
    
    
    
    