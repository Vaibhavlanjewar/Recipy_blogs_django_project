from django.db import models

# Create your models here.

gender=(
    ('M','Male'),
    ('F','Female')
)
class Student(models.Model):
  # id=models.AutoField() # djago add automatically it is primary key 
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField(null=False,blank=True)
   
    
class Car(models.Model):
     car_name=models.CharField(max_length=500)
     speed=models.IntegerField(default=50)

     def __str__(self)->str:
          return self.car_name