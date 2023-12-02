from django.shortcuts import render

# Create your views here.

def admin_login(request):
    return render(request,'admin_templates/authentication-login.html')

def admin_dashboard(request):
    return render(request,'admin_templates/index.html')

def product_management(request):
    return render(request,'admin_templates/product_management.html')