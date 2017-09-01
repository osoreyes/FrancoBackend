# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 06:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20170829_0551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='descripcion',
            name='anio',
        ),
        migrations.RemoveField(
            model_name='descripcion',
            name='producto',
        ),
        migrations.AddField(
            model_name='producto',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='anio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='anio_inicio', to='main.Anio'),
        ),
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(default='dfasdfsd'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='dsfs', upload_to='productos/imagenes'),
        ),
        migrations.AddField(
            model_name='producto',
            name='motor',
            field=models.CharField(default='sdfas', max_length=50),
        ),
        migrations.AddField(
            model_name='producto',
            name='slug',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.DeleteModel(
            name='Descripcion',
        ),
    ]
