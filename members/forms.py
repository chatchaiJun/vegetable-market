from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from . models import *
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role_choices = [('admin', 'Admin'), ('customer', 'Customer'), ('employee', 'Employee')]
    role = forms.ChoiceField(choices=role_choices, required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(max_length=20, required=True)


    class Meta:
        model = User
        fields = ["first_name", "last_name","username", "email", "password1", "password2","role","phone_number"]
    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("An user with this email already exists!")
        return email   

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street','district','city','postal_code']