from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'is_staff']
    ordering = ['id']



@admin.register(models.Blind)
class BlindAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'address', 'user']


@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['api_key', 'status', 'blind']
