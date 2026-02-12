from django.shortcuts import render,redirect
from AdminApp.models import CategoryData,ProductData
from WebApp.models import *
from django.shortcuts import get_object_or_404
from django.contrib import messages
import razorpay


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
    latest=ProductData.objects.order_by('-id')[:3]
    return render(request,'all-products.html',{'products':products,'category':category,'latest':latest})
def filtered_products(request,cat_name):
    category=CategoryData.objects.all()
    filtered_product=ProductData.objects.filter(CategoryName=cat_name)
    return render(request,'filtered-products.html',{'filtered_product':filtered_product,'category':category})

def single_product(request, pro_id): # Changed cat_name to pro_id to match urls.py
    product = get_object_or_404(ProductData, pk=pro_id)
    latest=ProductData.objects.order_by('-id')[:3]
    category=CategoryData.objects.all()

 
    return render(request, 'single-product.html', {
        'product': product,
        'category':category,
        'latest':latest
    })
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
            messages.success(request,"Successfully logged in")
            return redirect(home_page)
        else:
            messages.error(request,"invalid credentials")
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
    cart=CartData.objects.filter(username=request.session['username'])
    sub_total=0
    shipping_charge=0
    total_amount=0
    for i in cart:
        sub_total+=i.total
        if sub_total>100000:
            shipping_charge=0
        elif sub_total>50000:
            shipping_charge=100

        else:
            shipping_charge=250
        total_amount=sub_total+shipping_charge

    return render(request,'cart.html',{'category':category,'cart':cart,'sub_total':sub_total,'sub_total':sub_total,'shipping_charge':shipping_charge,'total_amount':total_amount})

def checkout(request):
    category=CategoryData.objects.all()
    cart=CartData.objects.filter(username=request.session['username'])
    sub_total=0
    shipping_charge=0
    total_amount=0
    for i in cart:
        sub_total+=i.total
        if sub_total>100000:
            shipping_charge=0
        elif sub_total>50000:
            shipping_charge=100

        else:
            shipping_charge=250
        total_amount=sub_total+shipping_charge

    return render(request,'checkout.html',{'category':category,'cart':cart,'sub_total':sub_total,'total_amount':total_amount,})

def save_to_cart(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pname=request.POST.get('productname')
        qty=request.POST.get('qty')
        price=request.POST.get('price')
        total=request.POST.get('total')
        obj2=CartData(username=uname,product_name=pname,qty=qty,price=price,total=total)
        obj2.save()
        messages.success(request,'Added to cart')
        return redirect(cart)


def delete(request):
    data=CartData.objects.filter(username=request.session['username'])
    data.delete()
    messages.success(request,'Item successfully removed')
    return redirect(cart)


def payment(request):
    category=CategoryData.objects.all()
    customer=BillingData.objects.order_by('-id').first()
    pay=customer.Total_Price
    amount=int(pay*100)
    pay_str=str(amount)
    if request.method=="POST":
        order_currency="INR"
        client=razorpay.Client(auth=('rzp_test_0ib0jPwwZ7I1lT','VjHNO5zKeKxz8PYe7VnzwxMR'))
        payment=client.order.create({
        'amount':amount,
        'currency':order_currency,

    })
    return render(request,'payment.html',{'category':category,
                                          'pay_str':pay_str,
                                          'amount':amount})



def save_billing_data(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        fname=request.POST.get('fname')
        pincode=request.POST.get('pincode')
        mobile=request.POST.get('mobile')
        message=request.POST.get('message')
        place=request.POST.get('place')
        email=request.POST.get('email')
        total=request.POST.get('total')
        obj2=BillingData(Fname=fname,Username=uname,Email=email,Mobile=mobile,Place=place,Total_Price=total,Message=message,Post_Code=pincode)
        obj2.save()
        return redirect(payment)


def payment_success(request):
    payment_id = request.GET.get('payment_id')

    if payment_id:
        # mark order as paid
        order = BillingData.objects.get(user=request.user, is_paid=False)
        order.is_paid = True
        order.save()

        # delete cart items
        CartData.objects.filter(user=request.user).delete()

        return render(request, 'success.html')

    return redirect('cart')
