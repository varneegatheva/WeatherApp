# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=False)

class FavouriteCity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100, null=True, unique=True)