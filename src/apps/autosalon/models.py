from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField
    last_name = models.CharField(blank=True, null=True)
    age = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)


    def __str__(self):
        return f"{self.name}"



class Car(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    year = models.PositiveIntegerField(default=2020)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    colour = models.CharField
    engine_type = models.CharField
    status = models.CharField(default='available')

    def __str__(self):
        return f"{self.brand} {self.name}"


class Order(models.Model):
    user = models.ForeignKey(models.CASCADE)
    car = models.ForeignKey()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.name}"

class TestDrive(models.Model):
    user = models.ForeignKey
    car = models.ForeignKey(models.CASCADE)
    status = models.CharField()
    status = models.PositiveSmallIntegerField

    def __str__(self):
        return f"TestDrive #{self.id} - {self.car.name}"
    





