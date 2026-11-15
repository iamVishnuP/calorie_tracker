from django.db import models

from accounts.models import User

# Create your models here.

class FoodLog(models.Model):

    title=models.CharField(max_length=200,null=True)

    serving_size=models.CharField(max_length=200)

    calorie= models.FloatField()

    MEAL_TYPE_CHOICES= [
        ('breakfast','BreakFast'),
        ('lunch','Lunch'),
        ('dinner','Dinner'),
        ('snacks','Snacks'),
    ]

    meal_type= models.CharField(max_length=200,choices=MEAL_TYPE_CHOICES,default='breakfast')

    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    food_image= models.ImageField(upload_to='foods',null=True)

    created_at= models.DateTimeField(auto_now_add=True)
