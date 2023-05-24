from django.contrib import admin
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


# Register your models here.

@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['api_key', 'ultrasonic_left_value', 'ultrasonic_right_value', 'gps_lat', 'gps_lng', 'gps_h',
                    'gps_m',
                    'gps_s', 'membership', 'customer_id']
    list_select_related = ['customer']

    @admin.display(ordering='customer_id')
    def customer_id(self, device):
        url = (
                reverse('admin:device_customer_changelist')
                + '?'
                + urlencode({
            'device__id': str(device.customer.id)
        }))

        return format_html('<a href="{}">{} "Customers"</a>', url, device.customer.first_name)


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'address', 'active', 'user_id']
    list_select_related = ['user']

    @admin.display(ordering='user_id')
    def user_id(self, customer):
        url = (
                reverse('admin:user_user_changelist')
                + '?'
                + urlencode({
            'customer__id': str(customer.user.id)
        }))
        return format_html('<a href="{}">{} "Customers"</a>', url, customer.user)
