from django.shortcuts import render,get_object_or_404
from .cart import Cart
from products.models import Product
from django.http import JsonResponse
# Create your views here.
def summaryCart(request):
    # Get the Cart
    cart = Cart(request)
    cart_products =  cart.get_prods
    return render(request,"carts/summarycart.html",{"cart_products":cart_products})
def addCart(request):
    #Get the cart
    cart = Cart(request)
    #test for POST
    if request.POST.get('action') =='post':
        #Get stuff
        product_id = int(request.POST.get('product_id'))
        #lookup product in DB
        product = get_object_or_404(Product,id=product_id)
        # Save to session
        cart.add(product=product)
        cart_quantity = cart.__len__()
        #response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty':cart_quantity})
        return response
def deleteCart(request):
    pass
def updateCart(request):
    pass
