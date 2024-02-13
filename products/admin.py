from django.contrib import admin
from .models import *
# Register your models here.
class PictureInline(admin.TabularInline):
    model = Picture

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at','product_cover')
    inlines = [PictureInline]

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'image', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')


