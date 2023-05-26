from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from django.contrib.auth import get_user_model
from user.models import User
from .permissions import *
from .serializer import *
from .models import *


# Create your views here.

class DeviceViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = DeviceSerializer
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Device.objects.all()
        elif not user.is_staff:
            return Device.objects.filter(customer=user.id)


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Customer.objects.all()
        elif not user.is_staff:
            return Customer.objects.filter(user=user.id)

class BlindViewSet(ModelViewSet):
    queryset = Blind.objects.all()
    serializer_class = BlindSerializer
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]