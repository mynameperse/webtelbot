from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product

# Create your views here.
# List Of Products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'webtelbot/product_list.html', {'products': products})

# Detail Of Product
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'webtelbot/product_detail.html', {'product': product})
