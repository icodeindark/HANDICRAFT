from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse

from .basket import Basket

from store.models import Product

# Create your views here.
def basket_summary(request):
    return render(request,'store/cart.html')

def basket_add(request):
    basket = Basket(request)

    if request.POST.get('action') == 'POST':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product)
        response = JsonResponse({'test' : 'data'})
        return response
    else:
        # You might want to add a response for non-POST requests
        return JsonResponse({'error': 'Invalid request method'})
