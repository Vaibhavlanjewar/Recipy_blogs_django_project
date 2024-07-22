from django.db import models

# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=100)

class Recipy(models.Model):
    recipy_name=models.CharField(max_length=100)
    recipy_description=models.TextField()
    recipy_image=models.ImageField(upload_to="recipy")
    