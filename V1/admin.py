from django.contrib import admin
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


# Register your models here.
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'is_staff']
    ordering = ['id']


@admin.register(models.Blind)
class BlindAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'address', 'get_user_id_link']


    @admin.display(ordering='get_user_id')
    def get_user_id_link(self, blind):
        url = (
                reverse('admin:V1_customer_changelist')
                + '?'
                + urlencode({
            'blind__id': str(blind.user.id)
        }))
        return format_html('<a href="{}">{} Blinds</a>', url, blind.user)


@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['api_key', 'status', 'blind']
