from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['api_key', 'ultrasonic_left_value', 'ultrasonic_right_value', 'gps_lat', 'gps_lng', 'gps_h',
                    'gps_m',
                    'gps_s', 'membership', 'user']
