# members/models.py
from django.db import models
from django.contrib.auth.models import  User

class Address(models.Model):
    street = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    account = models.ForeignKey('Account', related_name='addresses', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.street}"

class Account(models.Model):
    CUSTOMER = 'customer'
    EMPLOYEE = 'employee'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (EMPLOYEE, 'Employee'),
        (ADMIN, 'Admin'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default=CUSTOMER)
    phone_number = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
