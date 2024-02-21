import json
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from carts.cart import Cart
from products.models import Product
from . forms import *
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from formtools.wizard.views import SessionWizardView

# Create your views here.

# def login_user(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         passowrd =  request.POST['password']
#         user =  authenticate(request,username = username, password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             messages.success(request,("There was An Error login"))
#             return redirect('login')
#     else:
#         return render(request,'members/login.html',{})
def login_user(request):
    form = LoginForm()
    
    if request.method == "POST":
   
        form = LoginForm(request,data=request.POST)
        # cart_data = json.loads(request.POST.get('cart_data'))
        if form.is_valid():
            cart_json =json.loads(request.POST.get('cart_data'))     
            quantity = 0
            product_id = 0
            for pid, qty in cart_json.items():
                product_id = pid
                quantity = qty
            product = get_object_or_404(Product, id=pid)
            cart = Cart(request)
            cart.add(product, quantity)
            username = request.POST.get('username')
            password = request.POST.get('password')
            user =  authenticate(request,username = username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
#         else:
#             messages.success(request,("There was An Error login"))
#             return redirect('login')
    return render(request,'members/login.html',{'loginform':form})


class RegistrationWizard(SessionWizardView):
    form_list = [RegisterForm, AddressForm]
    template_name = 'members/register.html'

    def done(self, form_list, **kwargs):
        # User in django Framework
        address_form = form_list[1] 
        user_form = form_list[0]
        user = user_form.save(commit=False)
        user.email = user_form.cleaned_data['email']
        user.first_name = user_form.cleaned_data['first_name']
        user.last_name = user_form.cleaned_data['last_name']
        user.save()

        # Save account information
        phone_number = user_form.cleaned_data['phone_number']
        role = user_form.cleaned_data['role']
        account = Account.objects.create(user=user, phone_number=phone_number, role=role)

        # Save address information
        address = address_form.save(commit=False)
        address.account = account
        address.save()
        return  redirect('home')
    
def register(request):
    wizard_view = RegistrationWizard.as_view()
    return wizard_view(request)

def logout_user(request):
    auth.logout(request)
    return redirect("home")