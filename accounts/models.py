from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

    # age = models.PositiveBigIntegerField(null = True , blank = True)
    # first_name = models.CharField(null=True,blank=False,name="Isim",max_length=100)
    # add additional fields in here

    def __str__(self):
        return self.username