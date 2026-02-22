from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100 ,null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2 ,null=False)
    quantity = models.IntegerField(null=False)
    category_id = models.IntegerField(null=True)
    image = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
