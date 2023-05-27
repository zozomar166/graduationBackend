from django.db import models
from user.models import User


# Create your models here.
class Customer(User):
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
