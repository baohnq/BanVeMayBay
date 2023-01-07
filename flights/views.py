from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, When, F
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerForm, UserForm
from .models import Airport, Flight, Ticket, Brand, Schedule, User, Customer

from datetime import datetime
# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
            return redirect('main')
        
    
    # page = 'login'
    username = ''
    password = ''
    context = {}

    if request.method == 'POST':
        # form
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        # check_user = User.objects.filter(username=username, password=password)

        try:
            # database
            user = User.objects.filter(username=username, password=password)
            
        except:      
            messages.add_message(request, messages.ERROR, 'No account found')

        user = authenticate(request, username=username, password=password)
        

        context['username'] = username
        context['password'] = password
        # context['role'] = rl

        if user is not None:
            login(request, user)
            return redirect('main')

        else:
            
            messages.add_message(request, messages.ERROR, 'Wrong username or password')
            # return render(request, 'login.html', context)

    return render(request, 'login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def createUser(request):
    user_form = UserForm()

    if request.method == 'POST':

        User.objects.create(
            username = request.POST.get('username'),
            password = request.POST.get('password'),
            role = request.POST.get('role'),
            name = request.POST.get('name'),
        )

        return redirect('index')

    context = {'user_form': user_form}
    return render(request, 'user_form.html', context)


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

def main(request):
    return render(request,"main.html",)
#irports = ["HaNoi","HCM","DaNang","DaLat" ]
# Create your views here.
def index(request):
    
    airports = Airport.objects.all()
    schedules = {}
    departure_date = ''
    is_search = 0
    if request.method == 'GET':
        ticket_type = request.GET.get('ticket_type')
        class_fl = request.GET.get('class')
        if request.GET.get('seat_number') != None:
            seat_number = int(request.GET.get('seat_number'))
        from_ap = request.GET.get('from')
        to_ap = request.GET.get('to')
        if not (request.GET.get('departure_date') is None):
            departure_date = datetime.strptime(request.GET.get('departure_date'),'%Y-%m-%d').date() 
        # retrive ticket
        if ticket_type == 'one way':
            schedules = Schedule.objects.filter(
                Q(date=departure_date),
                Q(flId__fromAp__apId__contains=from_ap),
                Q(flId__toAp__apId__contains=to_ap)
            )
            
            if class_fl=='economy':
                schedules = schedules.filter(Q(firstClassRest__gte=seat_number))
            else:
                schedules = schedules.filter(Q(secondClassRest__gte=seat_number))
            
            is_search = 1
        # else ticket_type = 'round trip'
        else:
            pass
    context = {
                'airports':airports,
                'schedules': schedules,
                'departure_date':departure_date,
                'is_search':is_search,
            }
    return render(request,'index.html',context)