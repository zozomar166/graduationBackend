# from django_cron import CronJobBase, Schedule
from .models import Device, Blind
import random


# class DeviceCronJob():
#     devices = Device.objects.all()
#     for device in devices:
#         # قم بتحديث الجهاز هنا
#         device.update()


class DeviceCronJob():
    name = random.randint(0, 3)
    Blind.objects.create(first_name=name)
