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

airports = ["HaNoi","HCM","DaNang","DaLat" ]
# Create your views here.
def index(request):
    
    #airports = Airport.objects.all()
    context = {'airports':airports}
    
    if request.method == 'GET':
        ticket_type = request.GET.get('ticket_type')
        class_fl = request.GET.get('class')
        seat_number = request.GET.get('seat_number')
        from_ap = request.GET.get('from')
        to_ap = request.GET.get('to')
        departure_date = request.GET.get('departure_date')
        # retrive ticket
        if ticket_type == 'one way':
            pass
        # else ticket_type = 'round trip'
        else:
            pass
            
    return render(request,'index.html',context)