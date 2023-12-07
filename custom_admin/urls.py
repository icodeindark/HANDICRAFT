from django.urls import path

from . import views


app_name = 'custom_admin'


urlpatterns = [
    path('',views.admin_login,name='admin_login'),
    path('dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('product_management/', views.product_management, name='product_management'),
    path('product_management/<slug:category_slug>/', views.product_admin, name='product_admin'),

    path('create_category/',views.createCategory,name='create_category'),
    path('create_product/',views.createProduct,name='create_product'),

    path('update_product/<str:pk>/',views.updateProduct,name='update_product'),
    path('delete_product/<str:pk>/',views.deleteProduct,name='delete_product'),
    path('edit_category/<str:pk>/',views.editCategory,name='edit_category'),
    path('delete_category/<str:pk>/',views.deleteCategory,name='delete_category'),

    


]
