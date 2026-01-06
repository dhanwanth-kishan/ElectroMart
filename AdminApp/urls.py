from django.urls import path
from AdminApp import views
urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('add_categories/',views.add_categories,name="add_categories"),
    path('save_category/',views.save_category,name="save_category"),
    path('display_categories/',views.display_categories,name="display_categories"),
    path('edit_category/<int:category_id>/',views.edit_category,name="edit_category"),
    path('update_category/<int:category_id>/',views.update_category,name="update_category"),
    path('delete_category/<int:category_id>',views.delete_category,name="delete_category"),
    path('add_product/',views.add_product,name="add_product"),
    path('save_product/',views.save_product,name="save_product"),
    path('display_products/',views.display_products,name="display_products"),
    path('delete_product/<int:product_id>',views.delete_product,name="delete_product"),
    path('edit_product/<int:product_id>',views.edit_product,name="edit_product"),
    path('update_product/<int:product_id>',views.update_product,name="update_product"),
    path('login_page/',views.login_page,name="login_page"),
    path('login_fn/',views.login_fn,name="login_fn"),
    path('logout_fn/',views.logout_fn,name="logout_fn"),
    path('contact_details/',views.contact_details,name="contact_details"),

]