from django.db import models
# authentication 
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=100)

class Recipy(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True )
    recipy_name=models.CharField(max_length=100)
    recipy_description=models.TextField()
    recipy_image=models.ImageField(upload_to="recipy")
    