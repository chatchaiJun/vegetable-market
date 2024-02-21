from django.shortcuts import get_object_or_404
from products.models import Product
# class Cart():
#     def __init__(self,request):
#         self.session = request.session

#     #Get the current session key if it exists
#         cart = self.session.get('session_key')

#     # if the user is new, no session key! createone!
#         if 'session_key' not in request.session:
#             cart = self.session['session_key']={}
#     #make sure cart is available on all pages of site
#         self.cart= cart
    
#     def add(self,product, quantity):
#         product_id = str(product.id)
#         product_qty = str(quantity)
#         if product_id in self.cart:
#             pass
#         else:
#             # self.cart[product_id] = {'price':str(product.price)}
#             self.cart[product_id] = int(product_qty)
#         self.session.modified =True

#     def __len__(self):
#         return len(self.cart)
    
#     def get_prods(self):
#         # at the  self.cart[product_id] = {'price':str(product.price)} mean key is product ID
#         product_ids = self.cart.keys()
#         products = Product.objects.filter(id__in=product_ids)
#         return products
#     def get_quants(self):
#         quantities = self.cart
#         return quantities
import json

class Cart():
    def __init__(self, request):
        self.request = request
        self.cart_name = 'cart'

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        cart = self.get_cart()
        if product_id in cart:
            cart[product_id] += int(product_qty)
        else:
            cart[product_id] = int(product_qty)
        self.save_cart(cart)

    def __len__(self):
        return len(self.get_cart())

    def get_cart(self):
        cart_str = self.request.session.get(self.cart_name, '{}')
        cart = json.loads(cart_str)
        return cart

    def save_cart(self, cart):
        cart_str = json.dumps(cart)
        self.request.session[self.cart_name] = cart_str

    def get_prods(self):
        cart = self.get_cart()
        product_ids = cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products

    def get_quants(self):
        return self.get_cart()
    
    def update_cart_from_localstorage(self, cart_data):
        cart = json.loads(cart_data)
        for product_id, quantity in cart.items():
            product = get_object_or_404(Product, pk=product_id)
            self.add(product, quantity)