from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CarViewSet, OrderViewSet, TestDriveViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cars', CarViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'testdrives', TestDriveViewSet)

urlpatterns = [
    path('', include(router.urls)),
]