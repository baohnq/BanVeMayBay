from importlib.resources import path
from django.urls import path
from . import views

urlpatterns =[
    path('create_customer/<str:scheduleID>/',  views.createCustomer, name="create_customer"),
    path('',views.index,name='index'),
    
    path('create_customer/',  views.createCustomer, name="create_customer"),
    path('display/',  views.display, name="display"),
    path('schedule/<str:pk>/',  views.schedule, name="schedule"),
    path('ticket/',  views.ticket, name="ticket"),
    path('update_ticket/<str:pk>/',  views.updateTicket, name="update_ticket"),
    path('delete_ticket/<str:pk>/',  views.deleteTicket, name="delete_ticket"),
]