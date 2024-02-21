from django.shortcuts import render,get_object_or_404
from datetime import datetime, timedelta
from .cart import Cart
from products.models import Product
from django.http import JsonResponse
import json

# Create your views here.
def summaryCart(request):
    # Get the Cart
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    return render(request, "carts/summarycart.html", {"cart_products": cart_products, "quantities": quantities})
def addCart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_qty = request.POST.get('product_qty')
        product = get_object_or_404(Product, id=product_id)
        cart = Cart(request)
        cart.add(product, product_qty)

        # Return a JSON response indicating success
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})
def deleteCart(request):
    pass
def updateCart(request):
    pass
