from django.shortcuts import render

from .models import *
from store.models import *



def basket_summary(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		print(customer, order, items)
	else:
		items = []
		order={'get_cart_total':0}

	context = {'items': items, 'order':order}
	return render(request, 'store/cart.html', context)


def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		print(customer, order, items)
	else:
		items = []
		order={'get_cart_total':0}

	context = {'items': items, 'order':order}
	return render(request, 'store/checkout.html', context)
