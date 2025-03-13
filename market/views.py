from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import UserRegistrationForm

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'market/product_list.html', {'products': products})

def signup(request):
    return render(request, 'market/signup.html')

def buyer_signup(request):
    return render(request, 'market/buyer_signup.html')

def email_signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('market:my_account')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    return render(request, 'market/email_signup.html', {'form': form})

@login_required
def my_account(request):
    return render(request, 'market/my_account.html')
