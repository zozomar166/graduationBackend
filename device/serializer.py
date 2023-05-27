from rest_framework import serializers
from user.models import User
from .models import *


class BlindDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blind
        fields = ['first_name', 'last_name', 'phone']


class DeviceSerializer(serializers.ModelSerializer):
    blind = BlindDeviceSerializer()

    class Meta:
        model = Device
        fields = ['api_key', 'ultrasonic_left_value', 'ultrasonic_right_value', 'gps_lat', 'gps_lng', 'gps_h',
                  'gps_m',
                  'gps_s', 'membership', 'blind']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'phone', 'address', 'active', 'user', 'user_name', 'password']


class BlindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blind
        fields = '__all__'


