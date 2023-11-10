from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    business_name = models.CharField(max_length=250, blank=True, null=True)
    username = models.CharField(max_length=250, unique=True)
    admin =models.BooleanField(default=False)

    REQUIRED_FIELDS = []
