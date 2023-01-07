from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=True)
    password = models.CharField(max_length=50, null=True)
    # role: admin, 0: staff

    STAFF = 'st'
    role_choices = [(STAFF, 'staff')]

    role = models.CharField(max_length=2, choices=role_choices, null=True, default=STAFF)
    
    name = models.TextField(null=True)

    USERNAME_FIELD = 'username'

class Airport(models.Model):
    apId = models.CharField(max_length=5, primary_key=True)
    #ex: NB001, TSN01
    apName = models.TextField(max_length=255)
    place = models.TextField(max_length=255)

class Brand(models.Model):
    brId = models.CharField(max_length=2, primary_key=True)
    brName = models.TextField(max_length= 255)

class Flight(models.Model):
    flId = models.CharField(max_length=9, primary_key=True)  
    # 2 chữ viết tắt hãng + năm + 4 chữ số vd: VJ22-0001
    #[VJ, VN, BB, PA, HA] .
    fromAp = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="fromAP_flight")
    toAp = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="toAP_flight")
    flTime = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
class Schedule(models.Model):
    flId = models.ForeignKey(Flight, on_delete=models.CASCADE)
    date = models.DateField()
    firstClassRest = models.IntegerField()
    secondClassRest = models.IntegerField()
    firstClass = models.IntegerField()
    secondClass = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['flId', 'date'], name='unique_flId_date_combination'
            )
        ]

class Customer(models.Model):
    customerID = models.CharField(max_length=10, primary_key=True, blank=True)
    name = models.TextField(null=True, blank= True)
    sdt = models.CharField(max_length=10)

class Ticket(models.Model):
    ticketId = models.CharField(max_length=14,primary_key=True)
    # xxyy-zzzz-tttt
    # xxyy-zzzz: ma chuyen bay, tttt: so thu tu ve
    
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    
    customID = models.ForeignKey(Customer,on_delete=models.CASCADE)
    booked = models.DateTimeField(auto_now=True)
    cost = models.FloatField()
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
