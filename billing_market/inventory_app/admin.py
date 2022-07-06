from django.contrib import admin
from .models import ProductInfo,ProductCategory,Suppliers,GST

# Register your models here.
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['product_category_id','product_category_name']
admin.site.register(ProductCategory,ProductCategoryAdmin)


class SuppliersAdmin(admin.ModelAdmin):
    list_display = ['supplier_id','supplier_name','supplier_address','supplier_contact','supplier_email','supplier_company']
admin.site.register(Suppliers,SuppliersAdmin)


class GSTAdmin(admin.ModelAdmin):
    list_display = ['gst_id','gst_no','cgst','sgst','igst']
admin.site.register(GST,GSTAdmin)


class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ['product_id','product_category','product_name','product_hsn','manufacturer','date_of_manufacturing','product_description','country_of_origin','product_price_without_gst','product_quantity','gst','suppliers']
admin.site.register(ProductInfo,ProductInfoAdmin)
