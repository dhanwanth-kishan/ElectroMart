from django.db import models

# Create your models here.
class CategoryData(models.Model):
    Category_Name=models.CharField(max_length=30,null=True,blank=True)
    Category_Description=models.CharField(max_length=30,null=True,blank=True)
    Category_Image=models.ImageField(upload_to="category_image",null=True,blank=True)


class ProductData(models.Model):
    CategoryName=models.CharField(max_length=30,null=True,blank=True)
    Product_Name=models.CharField(max_length=30,null=True,blank=True)
    Brand=models.CharField(max_length=30,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Short_Description=models.TextField(null=True,blank=True)
    Detailed_Description=models.TextField(null=True,blank=True)
    Product_Image1=models.ImageField(upload_to="Product Images", null=True,blank=True)
    Product_Image2=models.ImageField(upload_to="Product Images", null=True,blank=True)
    Product_Image3=models.ImageField(upload_to="Product Images", null=True,blank=True)
