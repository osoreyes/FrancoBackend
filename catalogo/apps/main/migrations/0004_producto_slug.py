# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170826_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='slug',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
