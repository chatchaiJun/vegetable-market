from django.shortcuts import render,redirect
from members.models import Account
from .models import Product
from .forms import *
def product(request):
    account = None
    if request.user.is_authenticated:
        try:
            account = Account.objects.get(user=request.user)
        except Account.DoesNotExist:
            pass  # Handle the case where the Account object does not exist

    products = Product.objects.all()

    return render(request, 'products/product.html', {"products": products, "account": account})

def addProduct(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = AddProductForm(request.POST,request.FILES)
        cat =  Category.objects.get(name=request.POST.get('cat'))
        if form.is_valid():
            product_instance = form.save(commit=False)  # Get the unsaved model instance
            product_instance.category = cat  # Assign the category to the product instance
            product_instance.save()  # Save the product instance with the category
            # Redirect to a success page or do something else
            return redirect('product')
    else:
        form = AddProductForm()

    return render(request, 'products/addproduct.html', {'productforms': form,'categorys':category})
