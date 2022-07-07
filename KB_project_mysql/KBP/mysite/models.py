from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    password_check = models.CharField(max_length=100)