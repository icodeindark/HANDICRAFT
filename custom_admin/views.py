from django.shortcuts import render

# Create your views here.

def admin_login(request):
    return render(request,'admin_templates/authentication_login.html')

def admin_dashboard(request):
    return render(request,'admin_templates/index.html')