from django.contrib import admin
from apps.autosalon import models
from apps.autosalon.models import User, Car, Order, TestDrive

# Register your models here.
admin.site.register(User)
admin.site.register(Car)
admin.site.register(Order)
admin.site.register(TestDrive)


