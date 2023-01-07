from importlib.resources import path
from django.urls import path
from . import views

urlpatterns =[
    path('', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('home/',views.index,name='main'),
    path('book/',views.index,name='index'),
    path('create_customer/',  views.createCustomer, name="create_customer"),
    path('create_user/',  views.createUser, name="create_user"),
    path('display/',  views.display, name="display"),

]