from django.shortcuts import render,get_object_or_404

from store.models import Category,Product
from .forms import ProductForm,CategoryForm

# Create your views here.

def admin_login(request):
    return render(request,'admin_templates/authentication-login.html')

def admin_dashboard(request):
    return render(request,'admin_templates/product_management.html')

'''
def product_admin(request):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context= {'category': category, 'products': products}
    return render(request,'admin_templates/product_managment.html',context)
'''


def product_management(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'admin_templates/product_management.html',context)