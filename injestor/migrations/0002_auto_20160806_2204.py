# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('injestor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='dropoff_lat',
            field=models.DecimalField(decimal_places=12, max_digits=15),
        ),
        migrations.AlterField(
            model_name='trip',
            name='dropoff_long',
            field=models.DecimalField(decimal_places=12, max_digits=15),
        ),
        migrations.AlterField(
            model_name='trip',
            name='pickup_lat',
            field=models.DecimalField(decimal_places=12, max_digits=15),
        ),
        migrations.AlterField(
            model_name='trip',
            name='pickup_long',
            field=models.DecimalField(decimal_places=12, max_digits=15),
        ),
    ]
