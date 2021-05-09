from django.db import models

# Create your models here.
class Advisor(models.Model):
    advisorname = models.CharField(max_length = 100)
    picture = models.ImageField(upload_to='media/')
    
class User(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    email = models.EmailField()
    
class Booking(models.Model):
    username = models.CharField(max_length = 100)
    userid = models.IntegerField()
    advisorname = models.CharField(max_length = 100)
    advisorid = models.IntegerField()
    time = models.CharField(max_length = 100)
    