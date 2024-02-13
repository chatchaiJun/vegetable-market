from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from . models import *
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_cover','name','description','price',"stock_quantity",]