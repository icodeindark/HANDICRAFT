
from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('summary/',views.basket_summary,name='basket_summary'),
    path('checkout/',views.checkout,name='checkout'),
    

    
]
