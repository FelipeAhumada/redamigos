# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-02 16:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0003_auto_20180202_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enterprise',
            name='name',
        ),
    ]