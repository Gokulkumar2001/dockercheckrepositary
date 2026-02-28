from django.db import models
# Create your models here.

class Login(models.Model):
    name = models.CharField(max_length=120,null=True,blank=True)
    password = models.CharField(max_length=128,null=True,blank=True)
    status = models.IntegerField(default=1,null=True,blank=True)

