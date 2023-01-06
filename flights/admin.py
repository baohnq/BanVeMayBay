from django.contrib import admin
from .models import Airport, Flight, Schedule, Ticket, Customer, Brand, User
# Register your models here.

admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Brand)
admin.site.register(Schedule)

