from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=40)
    price=models.FloatField()
    author=models.CharField(max_length=30)
    publisher=models.CharField(max_length=50)

class brmuser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nickname=models.CharField(max_length=20,null=False)
