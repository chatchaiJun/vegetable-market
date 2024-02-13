from django.contrib import admin
from .  models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


@admin.register(Address)
class Address(admin.ModelAdmin):
    list_display = ('street','district','city','postal_code')


class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'

class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInline,)
admin.site.unregister(User,)
admin.site.register(User, CustomizedUserAdmin)

@admin.register(Account)
class Account(admin.ModelAdmin):
    list_display = ('user','role',)
