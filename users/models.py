from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    # role: 1 là admin, 0 là nhân viên
    role = models.IntegerField()
    
    name = models.TextField()
    
