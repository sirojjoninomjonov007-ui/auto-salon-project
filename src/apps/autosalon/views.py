from rest_framework import viewsets
from .models import User, Car, Order, TestDrive
from apps.serializers import UserSerializer, CarSerializer, OrderSerializer, TestDriveSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class TestDriveViewSet(viewsets.ModelViewSet):
    queryset = TestDrive.objects.all()
    serializer_class = TestDriveSerializer