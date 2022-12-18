from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


class Car(models.Model):
    class CarState(models.TextChoices):
        new = 'NEW'
        used = 'USED'

    class BodyStyle(models.TextChoices):
        suv = 'Suv'
        sedan = 'Sedan'
        coupe = 'Coupe'
        hatchback = 'Hatchback'
        minivan = 'Minivan'
        wagon = 'Wagon'
        passenger_van = 'Passenger Van'
        pickup_truck = 'Pickup truck'
        convertible = 'Convertible'

    class Color(models.TextChoices):
        red = 'Red'
        orange = 'Orange'
        yellow = 'Yellow'
        green = 'Green'
        blue = 'Blue'
        indigo = 'Indigo'
        purple = 'Purple'
        white = 'White'
        black = 'Black'
        gray = 'Gray'

    class FuelType(models.TextChoices):
        gasoline = 'Gasoline'
        diesel = 'Diesel'
        hybrid = 'Hybrid'
        electric = 'Electric'

    class Make(models.TextChoices):
        ferrari = 'Ferrari'
        bmw = 'BMW'
        mercedes = 'Mercedes'
        lamborghini = 'Lamborghini'
        porsche = 'Porsche'
        audi = 'Audi'
        tesla = 'Tesla'
        jaguar = 'Jaguar'
        jeep = 'Jeep'
        kia = 'Kia'

    state = models.CharField(choices=CarState.choices, max_length=5)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    picture = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)
    make = models.CharField(choices=Make.choices, max_length=30)
    url = models.CharField(max_length=150)
    production_year = models.IntegerField()
    mileage = models.IntegerField()
    body_style = models.CharField(choices=BodyStyle.choices, max_length=15)
    color = models.CharField(choices=Color.choices, max_length=6)
    fuel_type = models.CharField(choices=FuelType.choices, max_length=8)

    def __str__(self):
        return self.name + " $ " + str(self.price)
