from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20) 
    create_date = models.DateField(auto_now_add=True)
    birth_date = models.DateField(auto_now_add=True)
    
