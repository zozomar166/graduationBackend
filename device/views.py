from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from user.models import User
from .permissions import *
from .serializer import *
from .models import *


# Create your views here.

class DeviceViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    # queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Device.objects.all()
        elif not user.is_staff:
            return Device.objects.filter(user_id=user.id)
