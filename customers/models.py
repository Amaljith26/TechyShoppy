from django.db import models
from django.contrib.auth.models import User


class Customers( models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))
    Name= models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='customer_profile')
    Delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at =models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)


def __str__(self) -> str:
    return self.Title
