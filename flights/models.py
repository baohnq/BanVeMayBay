from django.db import models
from users.models import User
# Create your models here.

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
    #[VJ, VN, BB, PA, JP] .
    fromAp = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="fromAP_flight")
    toAp = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="toAP_flight")
    flTime = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
class Schedule(models.Model):
    flId = models.ForeignKey(Flight, on_delete=models.CASCADE)
    date = models.DateField()
    firstClassBooked = models.IntegerField()
    secondClassBooked = models.IntegerField()
    firstClass = models.IntegerField()
    secondClass = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['flId', 'date'], name='unique_flId_date_combination'
            )
        ]


class Ticket(models.Model):
    ticketId = models.CharField(max_length=14,primary_key=True)
    # xxyy-zzzz-tttt
    # xxyy-zzzz: ma chuyen bay, tttt: so thu tu ve
    
    flId = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="flId_ticket")
    date = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="date_ticket")
    customID = models.TextField()
    booked = models.DateTimeField(auto_now=True)
    cost = models.FloatField()
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
