import uuid
from django.contrib import admin
from django.contrib.auth import settings
from django.db import models


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.first_name

class Device(models.Model):
    SAVE = 'S'
    DANGER = 'D'
    OUT_OF_AREA = 'O'

    MEMBERSHIP_CHOICES = [
        (SAVE, '0'),
        (DANGER, '1'),
        (OUT_OF_AREA, '2'),
    ]

    api_key = models.UUIDField(primary_key=True, default=uuid.uuid4)
    ultrasonic_left_value = models.FloatField()
    ultrasonic_right_value = models.FloatField()
    gps_lat = models.FloatField()
    gps_lng = models.FloatField()
    gps_h = models.FloatField()
    gps_m = models.FloatField()
    gps_s = models.FloatField()
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=SAVE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



