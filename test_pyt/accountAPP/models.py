from django.db import models
from django.contrib.auth.models import User, AbstractUser
import datetime

# Create your models here.


class SellerProfile(models.Model):
    RATE = (
        ('1',1),
        ('2',2),
        ('3',3),
        ('4',4),
        ('5',5),
    )
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=256)
    bio = models.CharField(max_length=256)
    rate = models.CharField(max_length=1, choices=RATE)
    address = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.store_name}|{self.user}'