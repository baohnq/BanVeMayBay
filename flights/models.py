from django.db import models
from ..users.models import User
# Create your models here.

class Airport(models.Model):
    apId = models.CharField(max_length=5, primary_key=True)
    #ex: NB001, TSN01
    apName = models.TextField(max_length=255)
    place = models.TextField(max_length=255)

class Brand(models.Model):
    brId = models.CharField(primary_key=True)
    brName = models.TextChoices()

class Flight(models.Model):
    flId = models.CharField(max_length=9, primary_key=True)  
    # 2 chữ viết tắt hãng + năm + 4 chữ số vd: VJ22-0001
    #[VJ, VN, BB, PA, JP] .
    fromAp = models.ForeignKey(Airport)
    toAp = models.ForeignKey(Airport)
    flTime = models.IntegerField()
    brand = models.ForeignKey(Brand)
    
class Schedule(models.Model):
    flId = models.ForeignKey(Flight, primary_key=True, on_delete=models.CASCADE)
    date = models.DateField(primary_key=True)
    firstClassBooked = models.IntegerField()
    secondClassBooked = models.IntegerField()
    firstClass = models.IntegerField()
    secondClass = models.IntegerField()


class Ticket(models.Model):
    ticketId = models.CharField(max_length=14,primary_key=True)
    # xxyy-zzzz-tttt
    # xxyy-zzzz: ma chuyen bay, tttt: so thu tu ve
    
    flId, date = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    customID = models.TextField()
    booked = models.DateTimeField(auto_now=True)
    cost = models.FloatField()
    staff = models.ForeignKey(User)
