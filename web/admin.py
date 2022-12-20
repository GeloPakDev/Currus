from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from . import models


class CarAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Car, CarAdmin)


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff'
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_staff'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )


admin.site.register(models.CustomUser, CustomUserAdmin)
