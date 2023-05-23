from django.contrib import admin
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


# Register your models here.

@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['api_key', 'ultrasonic_left_value', 'ultrasonic_right_value', 'gps_lat', 'gps_lng', 'gps_h',
                    'gps_m',
                    'gps_s', 'membership', 'user_id']

    @admin.display(ordering='user_id')
    def user_id(self, device):
        url = (
                reverse('admin:user_user_changelist')
                + '?'
                + urlencode({
            'device__id': str(device.user)
        }))
        return format_html('<a href="{}">{} "User"</a>', url, device.user)
