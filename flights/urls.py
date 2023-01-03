from importlib.resources import path
from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,'index'),
    
    path('create_customer/',  views.createCustomer, name="create_customer"),
    path('display/',  views.display, name="display"),

]