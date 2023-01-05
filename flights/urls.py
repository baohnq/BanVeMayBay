from importlib.resources import path
from django.urls import path
from . import views

urlpatterns =[
    path('create_customer/<str:scheduleID>/',  views.createCustomer, name="create_customer"),
    path('display/',  views.display, name="display"),
    path('schedule/<str:pk>/',  views.schedule, name="schedule"),

]