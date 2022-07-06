from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=50)
    
class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    state_name = models.CharField(max_length=50)
    
class City(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)
    

class UserInfo(AbstractUser):
    
    mobile_no = PhoneNumberField()
    city=models.ForeignKey(City, on_delete=models.CASCADE)
    current_address = models.TextField()
    permanent_address = models.TextField()
    
    
    


    
    
    
    
    
    
