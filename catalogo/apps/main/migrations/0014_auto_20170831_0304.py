# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 03:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_producto_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='KitProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Kit de Productos',
                'verbose_name': 'KitProducto',
            },
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='anio',
            new_name='anio_inicio',
        ),
        migrations.AddField(
            model_name='producto',
            name='anio_fin',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='anio_fin', to='main.Anio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kitproducto',
            name='productos',
            field=models.ManyToManyField(to='main.Producto'),
        ),
    ]
