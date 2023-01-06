from importlib.resources import path
from django.urls import path
from . import views

urlpatterns =[
<<<<<<< HEAD
    path('create_customer/<str:scheduleID>/',  views.createCustomer, name="create_customer"),
=======
    path('',views.index,name='index'),
    
    path('create_customer/',  views.createCustomer, name="create_customer"),
>>>>>>> 31f3b0bc22c9277d26a34bf5213f0c8d4a1b341f
    path('display/',  views.display, name="display"),
    path('schedule/<str:pk>/',  views.schedule, name="schedule"),

]