# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 17:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Marcas',
                'verbose_name': 'Marca',
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Modelos',
                'verbose_name': 'Modelo',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('anio_inicio', models.IntegerField()),
                ('anio_fin', models.IntegerField()),
                ('motor', models.CharField(max_length=50)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Marca', verbose_name='marca')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Modelo', verbose_name='marca')),
            ],
            options={
                'verbose_name_plural': 'Productos',
                'verbose_name': 'Producto',
            },
        ),
    ]