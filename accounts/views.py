from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    orders = order.objects.all()
    customers = Customer.objects.all()

    context = {'orders':orders,'customers':customers}

    return render(request,"accounts/dashboard.html",context)

def products(request):
    products = product.objects.all() 
    return render(request,"accounts/products.html",{"products":products})

def customer(request):
    return render(request,"accounts/customer.html")
