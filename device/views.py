from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .serializer import *
from .models import *


# Create your views here.
class DeviceViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
