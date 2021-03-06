from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import orderform
from .filters import orderfilter
# Create your views here.
def home(request):
    orders = order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()

    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()

    context = {'orders':orders,'customers':customers,"total_customers":total_customers,"total_orders":total_orders,"delivered":delivered,"pending":pending,}

    return render(request,"accounts/dashboard.html",context)

def products(request):
    products = product.objects.all() 
    return render(request,"accounts/products.html",{"products":products})

def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()

    order_count = orders.count()

    myfilter = orderfilter(request.GET,queryset=orders)
    orders = myfilter.qs

    context  = {"customer":customer,"orders":orders,"order_count":order_count,"myfilter":myfilter}
    return render(request,"accounts/customer.html",context)

def createorder(request,pk):
    orderformset = inlineformset_factory(Customer,order,fields=('product','status'),extra=5)
    customer = Customer.objects.get(id=pk)
    formset = orderformset(queryset=order.objects.none(), instance=customer)
    # form  = orderform(initial={"Customer":customer})
    if request.method == 'POST':
        # print('printing post :',request.post)
        # form = orderform(request.POST)
        formset = orderformset(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset':formset}
    return render(request,'accounts/order_form.html',context)

def updateorder(request,pk):

    Order = order.objects.get(id = pk)
    form = orderform(instance=Order)

    if request.method == 'POST':
        # print('printing post :',request.post)
        form = orderform(request.POST,instance=Order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'accounts/order_form.html',context)

def deleteorder(request,pk):
    Order = order.objects.get(id = pk)
    if request.method == "POST":
        Order.delete()
        return redirect('/')
    context = {'item':Order}
    return render(request,'accounts/delete.html',context)
