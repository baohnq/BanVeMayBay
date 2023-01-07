from importlib.resources import path
from django.urls import path
from . import views

urlpatterns =[
    path('', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('home/',views.main,name='main'),
    path('book/',views.index,name='index'),
    
    path('create_user/',  views.createUser, name="create_user"),
    path('display/',  views.display, name="display"),
    
    path('create_customer/<str:scheduleID>/',  views.createCustomer, name="create_customer"),
    
    path('create_schedule/',views.create_schedule,name="create_schedule"),
    path('update_schedule/<str:schedule_id>',views.update_schedule,name="update_schedule"),
    path('delete_schedule/<str:schedule_id>',views.deleteSchedule,name="update_schedule"),
    path('schedule_detail/<str:pk>/',  views.schedule_detail, name="schedule_detail"),
    
    path('ticket/', views.ticket, name="ticket"),

    path('update_ticket/<str:pk>/',  views.updateTicket, name="update_ticket"),
    path('delete_ticket/<str:pk>/',  views.deleteTicket, name="delete_ticket"),

    path('flight_list/', views.flights_list, name='flight_list'),
    path('add_flight/', views.addFlight, name='add_flight'),
    path('update_flight/<str:pk>/', views.updateFlight, name='update_flight'),
    path('delete_flight/<str:pk>/', views.deleteFlight, name='delete_flight'),
]