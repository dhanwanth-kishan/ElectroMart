from django.urls import path
from WebApp import views
urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('about_us/',views.about_us,name="about_us"),
    path('contact_us/',views.contact_us,name="contact_us"),
    path('all_products/',views.all_products,name="all_products"),
    path('filtered_products/<cat_name>/',views.filtered_products,name="filtered_products"),
    path('single_product/<int:pro_id>/',views.single_product,name="single_product"),
    path('signin_signup/',views.signin_signup,name="signin_signup"),
    path('save_user/',views.save_user,name="save_user"),
    path('user_login/',views.user_login,name="user_login"),
    path('logout_fn/',views.logout_fn,name="logout_fn"),
    path('save_contact_us/',views.save_contact_us,name="save_contact_us"),
    path('support/',views.support,name="support"),
    path('help/',views.help,name="help"),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),

    
]
