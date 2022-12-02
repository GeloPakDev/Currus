from django.db import models


class Car(models.Model):
    class CarState(models.TextChoices):
        new = 'NEW'
        used = 'USED'

    class BodyStyle(models.TextChoices):
        suv = 'SUV'
        sedan = 'Sedan'
        coupe = 'Coupe'
        hatchback = 'Hatchback'
        minivan = 'Minivan'
        wagon = 'Wagon'
        passenger_van = 'Passenger Van'
        pickup_truck = 'Pickup truck'
        convertible = 'Convertible'

    class Color(models.TextChoices):
        red = 'RED'
        orange = 'ORANGE'
        yellow = 'YELLOW'
        green = 'GREEN'
        blue = 'BLUE'
        indigo = 'INDIGO'
        purple = 'PURPLE'

    class FuelType(models.TextChoices):
        gasoline = 'Gasoline'
        diesel = 'Diesel'
        hybrid = 'Hybrid'
        electric = 'Electric'

    state = models.CharField(choices=CarState.choices, max_length=5)
    price = models.DecimalField(max_length=10, decimal_places=3, max_digits=6)
    picture = models.ImageField(upload_to='pictures/')
    description = models.CharField(max_length=100)
    make = models.CharField(max_length=30)
    production_year = models.IntegerField()
    mileage = models.IntegerField()
    body_style = models.CharField(choices=BodyStyle.choices, max_length=15)
    color = models.CharField(choices=Color.choices, max_length=6)
    fuel_type = models.CharField(choices=FuelType.choices, max_length=8)

    def __str__(self):
        return self.description
