import email
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
