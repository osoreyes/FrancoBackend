# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_producto_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='modelo',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Modelo',
        ),
    ]
