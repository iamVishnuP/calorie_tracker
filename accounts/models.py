from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    age= models.PositiveIntegerField(null=True)

    height=models.DecimalField(max_digits=5,decimal_places=2,null=True)

    weight= models.DecimalField(max_digits=5,decimal_places=2,null=True)

    dob=models.DateField(null=True)

    phone=models.CharField(max_length=10,unique=True)

    
