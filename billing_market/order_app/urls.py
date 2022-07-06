

from django.urls import path
from .views import OrderView,ShowOrderView,SupplierView,ShowSupplierView,SupplierUpdateview,SupplierDeleteview,ProductView,ProductInfoView,GSTView,ProductCategoryView,ShowProductView

urlpatterns =[
    path('ov/', OrderView.as_view(), name='order_url'),
    path('sv/',SupplierView.as_view(),name='suplier_url'),
    path('so/', ShowOrderView.as_view(), name='showorder_url'),
    path('ss/',ShowSupplierView.as_view(),name='showsupplier_url'),
    path('up/<int:pk>/',SupplierUpdateview.as_view(),name='update_url'),
    path('dl/<int:pk>/',SupplierDeleteview.as_view(),name='delete_url'),
    path('product/',ProductView.as_view(),name='product_url'),
    path('showproduct/',ShowProductView.as_view(),name='showproduct_url'),



    path('productinfo/',ProductInfoView.as_view(),name='productinfo_url'),
    path('gst/',GSTView.as_view(),name='gst_url'),
    path('productcategory/',ProductCategoryView.as_view(),name='productcategory_url'),




] 