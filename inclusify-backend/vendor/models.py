from django.db import models

# Create your models here.
class Vendor(models.Model):
    name=models.CharField(max_length=255,default="vendor")
    address=models.TextField(default="this is my address")
    
    