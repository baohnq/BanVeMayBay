from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    # page = 'login'

    if request.method == 'POST':
        username = request.POST.get('username').lower
        password = request.POST.get('password')

        if username == 'group25' & password == 'group25':
            print('superuser')
        else:
            print('Welcome stranger')

    context = {}
    return render(request, 'base/login.html')
