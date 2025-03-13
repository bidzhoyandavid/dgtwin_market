from django.shortcuts import render
from .models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'market/product_list.html', {'products': products})

def signup(request):
    return render(request, 'market/signup.html')

def buyer_signup(request):
    return render(request, 'market/buyer_signup.html')
