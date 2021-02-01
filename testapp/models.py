from django.db import models

# Create your models here.

class Employee(models.Model):
    ename = models.CharField(max_length=64)
    eno = models.IntegerField()
    esal = models.FloatField()
    eaddr = models.CharField(max_length=64)
