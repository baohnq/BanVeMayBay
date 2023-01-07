from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, When, F
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Schedule
from .forms import CustomerForm, TicketForm
from .models import Airport, Flight, Ticket, Brand, Schedule, User, Transit

from datetime import datetime
# Create your views here.

def getCost(fromAP, toAP):
    # if fromAP == 'LK':
    #     return getCost(toAP,fromAP)

    if fromAP == 'NB':
        if toAP == 'TSN':
            return 1500000
        elif toAP == 'PQ':
            return 1000000
        elif toAP == 'CL':
            return 1000000
        elif toAP == 'LK':
            return 1000000 
    elif fromAP == 'TSN':
        if toAP == 'PQ':
            return 1500000
        elif toAP == 'CL':
            return 1000000
        elif toAP == 'LK':
            return 1000000
    elif fromAP == 'PQ':
        if toAP == 'CL':
            return 1000000
        elif toAP == 'LK':
            return 1000000
    elif fromAP == 'CL':
        if toAP == 'LK':
            return 1000000

            
    if fromAP == 'VN':
        return 100000000
    # return getCost(toAP,fromAP)
    return 2323


def createCustomer(request,scheduleID):
    form = CustomerForm()
    schedule = Schedule.objects.get(id=scheduleID)
    user = User.objects.get(username='tan2')

    if request.method == 'POST':

        Customer.objects.create(
            customerID = request.POST.get('customerID'),
            name = request.POST.get('name'),
            sdt = request.POST.get('sdt'),
        )
        
        Ticket.objects.create(
            ticketId= schedule.flId.flId + '-0008',
            flId= schedule,
            date= schedule,
            customID = Customer.objects.get(customerID=request.POST.get('customerID')),
            booked= datetime.now(),
            cost = getCost(schedule.flId.fromAp.apId, schedule.flId.toAp.apId),
            staff= user
        )
        return redirect('ticket')

    context = {'form': form}
    return render(request, 'customer_form.html', context)


def display(request):
    i = Ticket.objects.all()
    context = {"info":i}
    return render(request,"display.html",context)


def schedule(request,pk):
    schedule = Schedule.objects.get(id=pk)
    
    flightID = schedule.flId.flId

    fromPos = schedule.flId.fromAp.place
    fromAp = schedule.flId.fromAp.apName

    toPos = schedule.flId.toAp.place
    toAp = schedule.flId.toAp.apName

    time = schedule.date
    brName = schedule.flId.brand.brName

    cost = getCost(schedule.flId.fromAp.apId, schedule.flId.toAp.apId)

    transitAps =  []#Transit.objects.get(flId=flightID)

    firstClassRest = schedule.firstClassRest
    secondClassRest = schedule.secondClassRest


    context = {"schedule":schedule,"pk":pk, "flightID":flightID, "fromPos":fromPos, "fromAp":fromAp, "toPos":toPos, "toAp":toAp,
                 "time":time, "brName":brName, "cost":cost, "transitAps": transitAps, "firstClassRest":firstClassRest, "secondClassRest":secondClassRest}
    return render(request,"schedule.html",context)


def ticket(request):
    tickets = Ticket.objects.all()
    context = {"tickets":tickets}
    return render(request, "ticket.html", context)

def updateTicket(request, pk):

    ticket = Ticket.objects.get(ticketId=pk)
    form = TicketForm(instance=ticket)
    schedules = Schedule.objects.all()
    customers = Customer.objects.all()

    # if request.user != room.host:
    #     return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        schedule_id = request.POST.get("schedule")
        schedule = Schedule.objects.get(pk=schedule_id)
        ticket.flId = schedule
        ticket.date = schedule
        ticket.cost =  getCost(schedule.flId.fromAp.apId, schedule.flId.toAp.apId)
        ticket.booked = datetime.now()
        ticket.save()
        return redirect('ticket')

    # context = {'form': form, 'topics': topics, 'ticket': ticket}


    context = {"form":form, "schedules":schedules, "customers":customers, "ticket":ticket}
    return render(request, "update_ticket.html", context)

def deleteTicket(request, pk):
    ticket = Ticket.objects.get(ticketId=pk)

    # if request.user != message.user:
    #     return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        ticket.delete()
        return redirect('ticket')

    context = {"obj":ticket}
    return render(request, "delete_ticket.html", context)

    
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
