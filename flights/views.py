from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, When, F
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerForm, UserForm, TicketForm, FlightForm
from .models import Airport, Flight, Ticket, Brand, Schedule, User, Customer, Transit

from datetime import datetime,date
# Create your views here.




def loginPage(request):
    # if request.user.is_authenticated:
    #         return redirect('index')
        
    
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
            user = User.objects.get(username=username)
            
        except:      
            messages.add_message(request, messages.ERROR, 'No account found')

        # user = authenticate(request, username=username, password=password)
        

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

def getCost(fromAP, toAP):
    if fromAP == 'LK':
        return getCost(toAP,fromAP)

    if fromAP == 'NB':
        if toAP == 'TSN':
            return 1500000
        elif toAP == 'PQ':
            return 1003000
        elif toAP == 'CL':
            return 1004300
        elif toAP == 'LK':
            return 1540000 
    elif fromAP == 'TSN':
        if toAP == 'PQ':
            return 1500000
        elif toAP == 'CL':
            return 1000000
        elif toAP == 'LK':
            return 1000000
    elif fromAP == 'PQ':
        if toAP == 'CL':
            return 1230000
        elif toAP == 'LK':
            return 1050000
    elif fromAP == 'CL':
        if toAP == 'LK':
            return 1900000

    return getCost(toAP,fromAP)
  


def createCustomer(request,scheduleID):
    form = CustomerForm()
    schedule = Schedule.objects.get(id=scheduleID)
    user = request.user

    if request.method == 'POST':
        
        Customer.objects.create(
            customerID = request.POST.get('customerID'),
            name = request.POST.get('name'),
            sdt = request.POST.get('sdt'),
        )
        
        while setting.seat_number > 0:
            Ticket.objects.create(
                ticketId= schedule.flId.flId + '-' + str(Ticket.objects.count()),
                schedule = schedule,
                customID = Customer.objects.get(customerID=request.POST.get('customerID')),
                booked= datetime.now(),
                cost = getCost(schedule.flId.fromAp.apId, schedule.flId.toAp.apId),
                staff= user
            )
            
            setting.seat_number -=1
            if str(setting.class_fl) == 'economy':
                schedule.firstClassRest -=  1
            else:
                t = schedule.secondClassRest
                schedule.secondClassRest -= 1
            schedule.save()

        return redirect('ticket')

    context = {'form': form}
    return render(request, 'customer_form.html', context)


temp = 'dfdff'
def display(request):


    context = {"info":temp}
    return render(request,"display.html",context)


def create_schedule(request):
    page = 'create'
    flights = Flight.objects.all()
    
    if request.method == 'POST':
        
        flight_id = request.POST.get('flight_id')
        flight = Flight.objects.get(flId=flight_id)
        departure_date = request.POST.get('departure_date')
        firstClass = int(request.POST.get('firstClass'))
        secondClass = int(request.POST.get('secondClass'))
        
        Schedule.objects.create(
            flId = flight,
            date = departure_date,
            firstClassRest=firstClass,
            secondClassRest=secondClass,
            firstClass=firstClass,
            secondClass=secondClass
        )
        return redirect('index')
            
    context = {'flights':flights, 'page':page}
    return render(request,'schedule_form.html',context)

def update_schedule(request,schedule_id):
    page = 'update'
    flights = Flight.objects.all()
    schedule = Schedule.objects.get(id=schedule_id)
    
    if request.method == 'POST':
        flight_id = request.POST.get('flight_id')
        firstClass = int(request.POST.get('firstClass'))
        secondClass = int(request.POST.get('secondClass'))
        
        schedule.flId = Flight.objects.get(flId=flight_id)
        schedule.date = request.POST.get('departure_date')
        schedule.firstClassRest=firstClass
        schedule.secondClassRest=secondClass
        schedule.firstClass=firstClass
        schedule.secondClass=secondClass
        schedule.save()
        return redirect('index')
    
    context = {'flights':flights, 'page':page, 'schedule':schedule}
    return render(request,'schedule_form.html',context)

def deleteSchedule(request, schedule_id):
    schedule = Schedule.objects.get(ticketId=schedule_id)

    # if request.user != message.user:
    #     return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        schedule.delete()
        return redirect('index')

    context = {"obj":schedule}
    return render(request, "delete.html", context)

def schedule_detail(request,pk):
    schedule = Schedule.objects.get(id=pk)
    
    flightID = schedule.flId.flId

    fromPos = schedule.flId.fromAp.place
    fromAp = schedule.flId.fromAp.apName

    toPos = schedule.flId.toAp.place
    toAp = schedule.flId.toAp.apName

    time = schedule.date
    brName = schedule.flId.brand.brName

    cost = getCost(schedule.flId.fromAp.apId, schedule.flId.toAp.apId)

    transitAps =  Transit.objects.filter(flId=flightID)

    firstClassRest = schedule.firstClassRest
    secondClassRest = schedule.secondClassRest


    context = {"schedule":schedule,"pk":pk, "flightID":flightID, "fromPos":fromPos, "fromAp":fromAp, "toPos":toPos, "toAp":toAp,
                 "time":time, "brName":brName, "cost":cost, "transitAps": transitAps, "firstClassRest":firstClassRest, "secondClassRest":secondClassRest}
    return render(request,"schedule_detail.html",context)


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
        ticket.schedule =schedule
        ticket.cost =  getCost(schedule.flId.fromAp.apId, schedule.flId.toAp.apId)
        ticket.booked = datetime.now()
        ticket.save()
        return redirect('ticket')


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
    return render(request, "delete.html", context)

def main(request):
    return render(request,"main.html",)

class setting:
    ticket_type = 'one way'
    class_fl = 'economy'
    seat_number = ''
    from_ap = ''
    to_ap = ''
    departure_date = datetime.now().date().strftime('%Y-%m-%d')

# Create your views here.
def index(request):
    airports = Airport.objects.all()
    schedules = {}
    #setting.departure_date = ''
    is_search = 0
    temp_fAp= ''
    temp_tAp= ''
    if request.method == 'GET':
        setting.ticket_type = request.GET.get('ticket_type')
        setting.class_fl = request.GET.get('class')
        if request.GET.get('seat_number') != None:
            setting.seat_number = int(request.GET.get('seat_number'))

        setting.from_ap = request.GET.get('from')
        
        setting.to_ap = request.GET.get('to')
        if not (request.GET.get('departure_date') is None):
            setting.departure_date = datetime.strptime(request.GET.get('departure_date'),'%Y-%m-%d').date() 

        # retrive ticket
        if setting.ticket_type == 'one way':
            schedules = Schedule.objects.filter(
                Q(date=setting.departure_date),
                Q(flId__fromAp__apId__contains=setting.from_ap),
                Q(flId__toAp__apId__contains=setting.to_ap)
            )
            
            if setting.class_fl=='economy':
                schedules = schedules.filter(Q(firstClassRest__gte=setting.seat_number))
            else:
                schedules = schedules.filter(Q(secondClassRest__gte=setting.seat_number))
            
            is_search = 1

            if Airport.objects.get(apId=setting.from_ap) != None:
                temp_fAp = Airport.objects.get(apId=setting.from_ap)
            if Airport.objects.get(apId=setting.from_ap) != None:
                temp_tAp = Airport.objects.get(apId=setting.to_ap)  

        # else ticket_type = 'round trip'
        else:
            pass

    
    context = {
                'airports':airports,
                'schedules': schedules,
                'departure_date':setting.departure_date,
                'is_search':is_search,
                'ticket_type': setting.ticket_type,
                'class_fl': setting.class_fl,
                'seat_number': setting.seat_number,
                'from_ap': setting.from_ap,
                'to_ap': setting.to_ap,
                'temp_fAp': temp_fAp,
                'temp_tAp': temp_tAp,
            }
    return render(request,'index.html',context)

def flights_list(request):
    flights = Flight.objects.all()
    context = {"flights":flights}
    return render(request, "flight_list.html", context)

def addFlight(request):
    flight_form = FlightForm
    airports = Airport.objects.all()
    brands = Brand.objects.all()
    
    if request.method == "POST":
        brand = Brand.objects.get(brId=request.POST.get('brand'))
        fromAp = Airport.objects.get(apId=request.POST.get('fromAp'))
        toAp = Airport.objects.get(apId=request.POST.get('toAp'))
        flTime = request.POST.get('flTime')

        flight_in_dtb = Flight.objects.filter(brand=brand)
        flight_count = flight_in_dtb.count() + 1
        today = date.today()
        year = str(today.year)[2:4]

        autoId = str(brand.brId)
        autoId += year
        autoId += '-'
        num = '000'+str(flight_count) if flight_count < 10 else '00'+str(flight_count)
        autoId += num

        Flight.objects.create(
            fromAp = fromAp,
            toAp = toAp,
            flTime = flTime,
            brand = brand, 
            flId = str(autoId)
        )
        print(autoId)
        flights = Flight.objects.all()
        context = {'flights':flights}
        return render(request, "flight_list.html", context)  

    context = {'airports':airports, 'brands':brands  }
    return render(request, 'add_flight.html', context)

def updateFlight(request, pk):
    flight = Flight.objects.get(flId=pk)
    form = FlightForm(instance=flight)
    
    airports = Airport.objects.all()
    if request.method == 'POST':
        fromAp = request.POST.get('fromAp')
        toAp = request.POST.get('toAp')
        flTime = request.POST.get('flight_time')

        flight.fromAp = fromAp
        flight.toAp = toAp
        flight.flTime = flTime
        flight.save()
        return render(request, 'update_flight.html')
    
    context = {"form":form, 'airports':airports, 'flight':flight}
    return render(request, 'update_flight.html', context)

def deleteFlight(request, pk):
    flight = Flight.objects.get(flId=pk)

    if request.method == 'POST':
        flight.delete()
        return redirect('flight_list')

    context = {"obj":flight}
    return render(request, "delete.html", context)
