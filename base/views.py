from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def login(request):
    # page = 'login'
    username = ''
    password = ''

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse('No accounts found')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            return HttpResponse('Login successfully')
        else:
            return HttpResponse('Wait a minute, who are you')

    context = {}
    return render(request, 'base/login.html', context)