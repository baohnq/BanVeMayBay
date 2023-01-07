from django.forms import ModelForm
from .models import Customer, Ticket
from django.contrib.auth.models import User


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        #exclude = ['host', 'participants']

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        