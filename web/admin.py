from django.contrib import admin

from . import models


class CarAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Car)
