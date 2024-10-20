from django.db import models

# Create your models here.
class AdminLogin(models.Model):
    user=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    
class Contact(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=45)
    emailaddress=models.CharField(max_length=50)
    msgarea=models.TextField()
    enquirydate=models.CharField(max_length=30)