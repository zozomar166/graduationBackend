from django.db import models
from user.models import User
from uuid import uuid4


# Create your models here.
class Customer(User):
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['id']


class Blind(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blinds')

    def __str__(self) -> str:
        return self.first_name


class Device(models.Model):
    INSIDE = '0'
    DANGER = '1'
    OUT_OF_SIDE = '2'
    MEMBERSHIP_CHOICES = [
        (INSIDE, '0'),
        (DANGER, '1'),
        (OUT_OF_SIDE, '2'),
    ]
    api_key = models.UUIDField(primary_key=True, default=uuid4)
    ultrasonic_left_value = models.CharField(max_length=255, blank=True, null=True)
    ultrasonic_right_value = models.CharField(max_length=255, blank=True, null=True)
    gps_lat = models.FloatField(blank=True, null=True)
    gps_lng = models.FloatField(blank=True, null=True)
    gps_h = models.FloatField(blank=True, null=True)
    gps_m = models.FloatField(blank=True, null=True)
    gps_s = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=INSIDE, blank=True, null=True)
    blind = models.OneToOneField(Blind, on_delete=models.CASCADE, related_name='device')
