from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Customer
from .forms import CustomerForm 

# Create your views here.

def createCustomer(request):
    form = CustomerForm()

    if request.method == 'POST':

        Customer.objects.create(
            customerID = request.POST.get('customerID'),
            name = request.POST.get('name'),
            sdt = request.POST.get('sdt'),
        )

        
        return redirect('display')

    context = {'form': form}
    return render(request, 'customer_form.html', context)


def display(request):
    i = Customer.objects.all()
    context = {"info":i}
    return render(request,"display.html",context)