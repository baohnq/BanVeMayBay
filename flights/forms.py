from django.forms import ModelForm
from .models import Customer, User

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        #exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'