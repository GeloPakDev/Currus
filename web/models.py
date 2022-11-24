from django.db import models
from enum import Enum


class Car(models.Model):
    class CarState(Enum):
        new = 'NEW'
        used = 'USED'

    class BodyStyle(Enum):
        suv = 'SUV'
        sedan = 'Sedan'
        coupe = 'Coupe'
        hatchback = 'Hatchback'
        minivan = 'Minivan'
        wagon = 'Wagon'
        passenger_van = 'Passenger Van'
        pickup_truck = 'Pickup truck'
        convertible = 'Convertible'

    class Color(Enum):
        red = 'RED'
        orange = 'ORANGE'
        yellow = 'YELLOW'
        green = 'GREEN'
        blue = 'BLUE'
        indigo = 'INDIGO'
        purple = 'PURPLE'

    class FuelType(Enum):
        gasoline = 'Gasoline'
        diesel = 'Diesel'
        hybrid = 'Hybrid'
        electric = 'Electric'

    state = models.CharField(choices=CarState)
    price = models.DecimalField(max_length=10)
    picture = models.ImageField(upload_to='pictures/')
    description = models.CharField(max_length=100)
    make = models.CharField(max_length=30)
    production_year = models.IntegerField(max_length=4)
    mileage = models.IntegerField()
    body_style = models.CharField(choices=BodyStyle)
    color = models.CharField(choices=Color)
    fuel_type = models.CharField(choices=FuelType)
