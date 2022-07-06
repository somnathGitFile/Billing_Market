from django.urls import path
from . import views

urlpatterns = [
    path('salerep/', views.DailySaleReportView),

    
]