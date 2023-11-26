from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    description = models.TextField()
    image1 = models.ImageField(upload_to='uploads/products')
    image2 = models.ImageField(upload_to='uploads/products')
    image3 = models.ImageField(upload_to='uploads/products')

    def __str__(self):
        return self.name
