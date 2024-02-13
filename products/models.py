from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_cover = models.ImageField(upload_to='product_pictures',blank=True)
    stock_quantity = models.IntegerField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Picture(models.Model):
    project = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pictures', default=1)
    image = models.ImageField(upload_to='product_pictures')
    description = models.TextField(blank=True)
    def __str__(self):
        return f"Picture {self.id} for Project {self.project.title}"