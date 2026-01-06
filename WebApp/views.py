from django.shortcuts import render,redirect
from AdminApp.models import CategoryData,ProductData
from WebApp.models import *

# Create your views here.
def home_page(request):
    category=CategoryData.objects.all()
    return render(request,'home.html',{'category':category})
def about_us(request):
    category=CategoryData.objects.all()
    return render(request,'about-us.html',{'category':category})
def contact_us(request):
    product=ProductData.objects.all()
    category=CategoryData.objects.all()
    return render(request,'contact-us.html',{'category':category,'product':product})
def all_products(request):
    products=ProductData.objects.all()
    category=CategoryData.objects.all()
    return render(request,'all-products.html',{'products':products,'category':category})
def filtered_products(request,cat_name):
    category=CategoryData.objects.all()
    filtered_product=ProductData.objects.filter(CategoryName=cat_name)
    return render(request,'filtered-products.html',{'filtered_product':filtered_product,'category':category})

def single_product(request,pro_id):
    product=ProductData.objects.get(id=pro_id)
    category=ProductData.objects.all()
    return render(request,'single-product.html',{'product':product,'category':category})

def signin_signup(request):
    return render(request,'signin-signup.html')

def save_user(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if UserRegistration.objects.filter(Username=uname).exists():
            return redirect(signin_signup)
        elif UserRegistration.objects.filter(Email=email).exists():
            return redirect(signin_signup)
        else:

            obj1=UserRegistration(Username=uname,Password=password,Email=email,Confirm_Password=confirm_password)
            obj1.save()
        return redirect(signin_signup)
    
def user_login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        password=request.POST.get('password')


        if UserRegistration.objects.filter(Username=uname,Password=password).exists():
            request.session['username']=uname
            request.session['password']=password
            return redirect(home_page)
        else:
            return redirect(signin_signup)
    else:
            return redirect(signin_signup)
    

def logout_fn(request):
    del request.session['username']
    del request.session['password']
    return redirect(home_page)



def save_contact_us(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        subject=request.POST.get('subject')
        
        obj3=ContactUsData(Name=name,Phone=phone,Email=email,Message=message,Subject=subject)
        obj3.save()
        return redirect(contact_us)
    
def support(request):
    product=ProductData.objects.all()
    category=CategoryData.objects.all()
    return render(request,'support.html',{'product':product,'category':category})
def help(request):
    product=ProductData.objects.all()
    category=CategoryData.objects.all()
    return render(request,'help.html',{'product':product,'category':category})
def cart(request):
    category=CategoryData.objects.all()
    return render(request,'cart.html',{'category':category})

def checkout(request):
    category=CategoryData.objects.all()
    return render(request,'checkout.html',{'category':category})