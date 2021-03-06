# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 17:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0002_auto_20170827_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Shopping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spending.Shopping')),
            ],
        ),
    ]
