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


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class UpdateCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone', 'address', 'is_staff']