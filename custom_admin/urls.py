from django.urls import path

from . import views


app_name = 'custom_admin'


urlpatterns = [
    path('',views.admin_login,name='admin_login'),
    path('dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('product_management/', views.product_management, name='product_management'),


]
