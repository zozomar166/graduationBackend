from rest_framework import serializers
from .models import *


class CustomerDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone']


class DeviceSerializer(serializers.ModelSerializer):
    customer = CustomerDeviceSerializer()

    class Meta:
        model = Device
        fields = ['api_key', 'ultrasonic_left_value', 'ultrasonic_right_value', 'gps_lat', 'gps_lng', 'gps_h',
                  'gps_m',
                  'gps_s', 'membership', 'customer']


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone', 'address', 'active']
