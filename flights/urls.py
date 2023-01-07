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
    path('schedule_detail/<str:pk>/',  views.schedule_detail, name="schedule_detail"),
    path('ticket/',  views.ticket, name="ticket"),
    path('update_ticket/<str:pk>/',  views.updateTicket, name="update_ticket"),
    path('delete_ticket/<str:pk>/',  views.deleteTicket, name="delete_ticket"),

]