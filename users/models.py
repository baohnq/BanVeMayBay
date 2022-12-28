from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    # role: admin, 0: staff
    role = models.IntegerField()
    
    name = models.TextField()

class Customer(models.Model):
    cusId = models.IntegerField(max_length=10, primary_key=True)
    cusName = models.TextField(max_length=255)
    cusPhone = models.TextField(max_length=20)
