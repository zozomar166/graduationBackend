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
    user = serializers.HyperlinkedRelatedField(
        queryset=Customer.objects.all(),
        view_name='customers-detail'
    )

    class Meta:
        model = Blind
        fields = '__all__'


class BlindDetailsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    id = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255, read_only=True)
    last_name = serializers.CharField(max_length=255, read_only=True)
    phone = serializers.CharField(max_length=255, read_only=True)
    address = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Blind
        fields = ['id', 'user', 'first_name', 'last_name', 'phone', 'address']


class DeviceSerializer(serializers.ModelSerializer):
    api_key = serializers.UUIDField(read_only=True)
    blind = BlindDetailsSerializer()

    def create(self, validated_data):
        nested_data = validated_data.pop('blind', None)
        blind_id = nested_data.get('id') if nested_data else None
        instance = super().create(validated_data)
        if blind_id:
            blind_user = nested_data.pop('user', None)
            blind_instance = Blind.objects.get(id=blind_id)
            instance.blind = blind_instance
            instance.save()
        return instance

    def update(self, instance, validated_data):
        nested_data = validated_data.pop('blind', None)
        print("n=", validated_data)
        if nested_data:
            blind_serializer = self.fields['blind']
            blind_instance = instance.blind
            blind_serializer.update(blind_instance, nested_data)
            instance.save()
        return super().update(instance, validated_data)

    class Meta:
        model = Device
        fields = ['api_key', 'ultrasonic_left_value', 'ultrasonic_right_value', 'gps_lat', 'gps_lng', 'gps_h', 'gps_m',
                  'gps_s', 'c_lat', 'c_lng', 'r1_radius', 'r2_radius', 'status', 'blind']


class UpdateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone', 'address', 'is_staff']


class UpdateDeviceSerializer(serializers.ModelSerializer):
    status = serializers.CharField(max_length=255, required=False)
    c_lat = serializers.FloatField(required=False)
    c_lng = serializers.FloatField(required=False)
    r1_radius = serializers.FloatField(required=False)
    r2_radius = serializers.FloatField(required=False)
    class Meta:
        model = Device
        fields = ['api_key', 'ultrasonic_left_value', 'ultrasonic_right_value', 'gps_lat', 'gps_lng', 'status', 'c_lat', 'c_lng', 'r1_radius', 'r2_radius']
