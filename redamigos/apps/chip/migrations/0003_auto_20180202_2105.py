# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-02 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chip', '0002_auto_20180202_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chip',
            name='lccid',
            field=models.CharField(max_length=20),
        ),
    ]
