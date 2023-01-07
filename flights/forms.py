from django.forms import ModelForm
from .models import Customer, User, Ticket, Flight

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        #exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'name']
        # exclude = ['email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_superuser', 'is_staff', 'is_active']

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'