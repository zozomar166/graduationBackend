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
        username = get_user_model()
        if user.is_staff:
            return Device.objects.all()
        elif not user.is_staff:
            user_id = username.objects.get(username=username).id
            return Device.objects.filter(user_id=user_id)
