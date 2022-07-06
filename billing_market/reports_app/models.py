from django.db import models

# Create your models here.

class DailySaleReport(models.Model):
    daily_sale_product_quantity = models.IntegerField()
    daily_sale_product_total_price = models.FloatField()
    daily_sale_total_customers = models.FloatField()
    
class DailyPurchaseReport(models.Model):
    daily_purchase_orders = models.CharField(max_length=50)
    daily_purchase_product_quantity = models.FloatField()
    daily_purchase_product_total_price = models.FloatField()
    daily_purchase_total_suppliers = models.FloatField()
    
    
class DailyExpensesReport(models.Model):
    daily_expenses_id = models.IntegerField(primary_key=True)
    daily_expenses_total_amount = models.FloatField()
     
    
class Expenses(models.Model):
    expense_id = models.IntegerField(primary_key=True)
    expense_use_for = models.CharField(max_length=50)
    expense_amount = models.FloatField()
    expense_datetime = models.DateTimeField()
    dailyexpensesreport = models.ForeignKey(DailyExpensesReport,on_delete=models.CASCADE)
    
    
    

