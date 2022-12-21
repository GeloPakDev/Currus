# Generated by Django 4.1.3 on 2022-12-20 21:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0002_alter_car_favourites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='favourites',
            field=models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
