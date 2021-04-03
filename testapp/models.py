from django.db import models

#Create your models here.uvsn
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    eaddr=models.CharField(max_length=60)
    esal=models.FloatField()
    def __str__(self):
          return self.esal
