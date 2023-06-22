from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsAdminOrReadOnly, CustomerBlindPermissions, BlindDevicePermissions
from .serializer import CustomerSerializer, BlindSerializer, DeviceSerializer, UpdateCustomerSerializer, BlindDetailsSerializer
from .models import Customer, Blind, Device


# Create your views here.
class CustomerViewSet(ModelViewSet):
    # queryset = Customer.objects.all()
    # serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, CustomerBlindPermissions]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Customer.objects.all()
        return Customer.objects.filter(blinds__user_id=user.id)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CustomerSerializer
        # elif self.request.method == 'PATCH':
        # return UpdateCartItemSerializer
        return UpdateCustomerSerializer


class BlindViewSet(ModelViewSet):
    serializer_class = BlindSerializer
    permission_classes = [IsAuthenticated, CustomerBlindPermissions, BlindDevicePermissions]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Blind.objects.all()
        return Blind.objects.filter(user_id=user.id)


class DeviceViewSet(ModelViewSet):
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated, BlindDevicePermissions]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Device.objects.all()
        return Device.objects.filter(blind__user_id=user.id)

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            # exclude the 'blind' field from the serializer for POST, PUT, and PATCH requests
            return DeviceSerializer
        return self.serializer_class
