from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Customer, Blind, Device

User = get_user_model()


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'phone', 'address', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class BlindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blind
        fields = '__all__'


class BlindDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blind
        fields = ['id', 'first_name', 'last_name', 'phone', 'address']


class DeviceSerializer(serializers.ModelSerializer):
    blind = BlindDetailsSerializer(read_only=True)
    class Meta:
        model = Device
        fields = ['api_key', 'ultrasonic_left_value', 'ultrasonic_right_value', 'gps_lat', 'gps_lng', 'gps_h', 'gps_m',
                  'gps_s', 'status', 'blind']


class UpdateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone', 'address', 'is_staff']
