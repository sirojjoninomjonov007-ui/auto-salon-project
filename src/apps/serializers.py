from rest_framework import serializers
from apps.autosalon.models import User, Car, Order, TestDrive

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class TestDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDrive
        fields = "__all__"