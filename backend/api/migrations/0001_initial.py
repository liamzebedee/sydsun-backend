# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('suburb', models.CharField(max_length=100)),
                ('lat', models.DecimalField(decimal_places=9, max_digits=12, verbose_name='Latitude')),
                ('lng', models.DecimalField(decimal_places=9, max_digits=12, verbose_name='Longitude')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]