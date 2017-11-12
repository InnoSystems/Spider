# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 15:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping',
            name='shop_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopping',
            name='store_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
