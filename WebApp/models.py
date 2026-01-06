from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    Username=models.CharField(max_length=30,null=True,blank=True)
    Email=models.EmailField(max_length=30,null=True,blank=True)
    Password=models.CharField(max_length=30,null=True,blank=True)
    Confirm_Password=models.CharField(max_length=30,null=True,blank=True)

class ContactUsData(models.Model):
    Name=models.CharField( max_length=50,null=True,blank=True)
    Subject=models.CharField( max_length=50,null=True,blank=True)
    Email=models.EmailField( max_length=50,null=True,blank=True)
    Phone=models.IntegerField( null=True,blank=True)
    Message=models.TextField(null=True,blank=True)