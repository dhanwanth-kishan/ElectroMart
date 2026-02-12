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


class CartData(models.Model):
    product_name=models.CharField(max_length=30,null=True,blank=True)
    username=models.CharField(max_length=30,null=True,blank=True)
    qty=models.IntegerField(null=True)
    price=models.IntegerField(null=True,blank=True)
    total=models.IntegerField(null=True,blank=True)


class BillingData(models.Model):
    Fname=models.CharField(max_length=30,null=True)
    Email=models.EmailField(max_length=30,null=True)
    Mobile=models.IntegerField()
    Place=models.CharField(max_length=30,null=True,blank=True)
    Post_Code=models.IntegerField()
    Username=models.CharField(max_length=30,null=True)
    Total_Price=models.IntegerField(null=True,blank=True)
    Message=models.CharField(max_length=30,null=True,blank=True)

