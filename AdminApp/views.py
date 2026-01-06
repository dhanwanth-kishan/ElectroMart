from django.shortcuts import render,redirect
from AdminApp.models import *

from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


from WebApp.models import *

# Create your views here.
def dashboard(request):
    categories=CategoryData.objects.all()
    products=ProductData.objects.all()

    return render(request,'dashboard.html',{'categories':categories,'products':products})

def add_categories(request):
    return render(request,'add-categories.html')
def save_category(request):
    if request.method=="POST":
        name=request.POST.get('category_name')
        description=request.POST.get('category_name')
        image=request.FILES['category_image']
        obj1=CategoryData(Category_Image=image,Category_Name=name,Category_Description=description)
        obj1.save()
        return redirect(display_categories)

def display_categories(request):
    categories=CategoryData.objects.all()
    return render(request,'display-categories.html',{'categories':categories})

def edit_category(request,category_id):
    category=CategoryData.objects.get(id=category_id)
    return render(request,'edit-category.html',{'category':category})
def update_category(request,category_id):
    if request.method=="POST":
        name=request.POST.get('category_name')
        description=request.POST.get('category_description')
        try:
            image=request.FILES['category_image']
            fs=FileSystemStorage()
            file=fs.save(image.name,image)
        except MultiValueDictKeyError:
            file=CategoryData.objects.get(id=category_id).Category_Image
        CategoryData.objects.filter(id=category_id).update(Category_Image=file,Category_Name=name,Category_Description=description)
        return redirect(display_categories)

def delete_category(request,category_id):
    data=CategoryData.objects.filter(id=category_id)
    data.delete()
    return redirect(display_categories)

def add_product(request):
    categories=CategoryData.objects.all()
    return render(request,'add-products.html',{'categories':categories})


def save_product(request):
    if request.method=="POST":
        category_name=request.POST.get('category_name')
        product_name=request.POST.get('product_name')
        price=request.POST.get('price')
        brand=request.POST.get('brand')
        short_description=request.POST.get('short_description')
        detailed_description=request.POST.get('detailed_description')
        image1=request.FILES['product_image1']
        image2=request.FILES['product_image2']
        image3=request.FILES['product_image3']
        obj2=ProductData(CategoryName=category_name,Product_Name=product_name,Price=price,Brand=brand,Short_Description=short_description,Detailed_Description=detailed_description,Product_Image1=image1,Product_Image2=image2,Product_Image3=image3)
        obj2.save()
        return redirect(display_products)
    
def display_products(request):
    products=ProductData.objects.all()
    return render(request,'display-products.html',{'products':products})
def edit_product(request,product_id):
    categories=CategoryData.objects.all()
    product=ProductData.objects.get(id=product_id)
    return render(request,'edit-product.html',{'product':product,'categories':categories})
def update_product(request,product_id):
    if request.method=="POST":
        category_name=request.POST.get('category_name')
        product_name=request.POST.get('product_name')
        price=request.POST.get('price')
        brand=request.POST.get('brand')
        short_description=request.POST.get('short_description')
        detailed_description=request.POST.get('detailed_description')
        try:
            image1=request.FILES['product_image1']
            fs1=FileSystemStorage()
            file1=fs1.save(image1.name,image1)
        except MultiValueDictKeyError:
            file1=ProductData.objects.get(id=product_id).Product_Image1
        
        try:
            image2=request.FILES['product_image2']
            fs2=FileSystemStorage()
            file2=fs2.save(image2.name,image2)
        except MultiValueDictKeyError:
            file2=ProductData.objects.get(id=product_id).Product_Image2
        
        try:
            image3=request.FILES['product_image3']
            fs3=FileSystemStorage()
            file3=fs3.save(image3.name,image3)
        except MultiValueDictKeyError:
            file3=ProductData.objects.get(id=product_id).Product_Image3
        ProductData.objects.filter(id=product_id).update(CategoryName=category_name,
                                                         Product_Name=product_name,Price=price,
                                                         Brand=brand,Short_Description=short_description,
                                                         Detailed_Description=detailed_description,
                                                         Product_Image1=file1,Product_Image2=file2,
                                                         Product_Image3=file3)
        return redirect(display_products)
    
def delete_product(request,product_id):
    data=ProductData.objects.filter(id=product_id)
    data.delete()
    return redirect(display_products)
        
def login_page(request):
    return render(request,'login-page.html')
def login_fn(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        pswd=request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            data=authenticate(username=uname,password=pswd)
            if data is not None:
                login(request,data)
                request.session['username']=uname
                request.session['password']=pswd
                return redirect(dashboard)
            else:
                return redirect(login_page)
        else:
            return redirect(login_page)
def logout_fn(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_page)


def contact_details(request):
    data=ContactUsData.objects.all()
    return render(request,'contact-details.html',{'data':data})


