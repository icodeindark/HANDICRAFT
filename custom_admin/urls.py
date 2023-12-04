from django.urls import path

from . import views


app_name = 'custom_admin'


urlpatterns = [
    path('',views.admin_login,name='admin_login'),
    path('dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('product_management/', views.product_management, name='product_management'),
    path('product_management/<slug:category_slug>/', views.product_admin, name='product_admin'),

    path('update_product/<str:pk>/',views.updateProduct,name='update_product'),


]
