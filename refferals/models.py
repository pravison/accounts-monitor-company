from django.db import models

# Create your models here.

class Refferal(models.Model):
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=17)
    location = models.CharField(max_length=250)
    active = models.BooleanField(default=False)
    refferal_code = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name
