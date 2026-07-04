from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50) # max_length qo'shildi
    last_name = models.CharField(max_length=50, blank=True, null=True) # max_length qo'shildi
    age = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(max_length=20, blank=True, null=True) # max_length qo'shildi
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Car(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    year = models.PositiveIntegerField(default=2020)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    colour = models.CharField(max_length=30) # max_length qo'shildi
    engine_type = models.CharField(max_length=30) # max_length qo'shildi
    status = models.CharField(max_length=30, default='available') # max_length qo'shildi

    def __str__(self):
        return f'{self.brand} {self.name}'


class Order(models.Model):
    # To'g'ri ForeignKey bog'lanishi
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    car = models.ForeignKey(Car, on_delete=models.CASCADE) 
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.user.name}"


class TestDrive(models.Model):
    # To'g'ri ForeignKey bog'lanishi
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    car = models.ForeignKey(Car, on_delete=models.CASCADE) 
    # Bitta status maydoni qoldirildi (biri matn, biri raqam edi, raqamlisini qoldirdik)
    status = models.PositiveSmallIntegerField(default=0) 

    def __str__(self):
        return f"TestDrive {self.user.name} - {self.car.brand}"