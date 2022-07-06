from django.urls import path
from . import views
# from inventory_app.views import GstView,AddGst,UpdateGst,DeleteGst,GstDetails

urlpatterns = [
    path('add_procat/',views.ProductCategoryView.as_view(), name='procat_urls'),
    path('show_cat/',views.ShowProductCategory.as_view(), name='show_urls'),
    path('update_cat/<int:pk>/',views.UpdateProductcategory.as_view(), name='procat_update_urls'),
    path('delete_cat/<int:pk>/',views.DeleteProductCategory.as_view(), name='procat_delete_urls'),
    

    path('add_pro/',views.ProductInfoView .as_view(), name='AddProductInfo_url'),
    path('show_pro/',views.ShowProductInfo.as_view(), name='showProductInfo_url'),
    path('update_pro/<int:pk>/',views.UpdateProductInfo .as_view(), name='updatepro_url'),
    path('delete_pro/<int:pk>/',views.DeleteProductInfo.as_view(), name='deletepro_url'),

   
    path('add_supp/',views.SuppliersView.as_view(), name="suppliers_url"),
    path('show_supp/',views.ShowSuppliers.as_view(), name='showsuppliers_url'),
    #path('show_supp/<int:page>/',views.ShowSuppliers.as_view(), name='showsuppliers_url'),
    path('update_supp/<int:pk>/',views.UpdateSuppliers.as_view(), name='updatesupplier_url'),
    path('del_supp/<int:pk>/',views.DeleteSuppliers.as_view(), name='deletesupplier_url'),

    path('add_gst/',views.AddGst.as_view(),name='gst_url'),
    path('show_gst/',views.GstView .as_view(),name='showgst_url'),
    path('gp/<int:pk>/',views.UpdateGst .as_view(),name='gstupdate_url'),
    path('gd/<int:pk>/',views.DeleteGst.as_view(),name='gstdelete_url')
    
]

    