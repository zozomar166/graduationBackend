# from django_cron import CronJobBase, Schedule
from .models import Device, Blind
import random

# class DeviceCronJob():
#     # RUN_EVERY_MINS = 1
#     #
#     # schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     # code = 'V1.DeviceCronJob'
#
#     def do(self):
#         # قم بتنفيذ العمليات التي ترغب في تنفيذها هنا
#         devices = Device.objects.all()
#         for device in devices:
#             # قم بتحديث الجهاز هنا
#             device.update()


class DeviceCronJob():
    name = random.randint(0, 3)
    Blind.objects.create(first_name = name)