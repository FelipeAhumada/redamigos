# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-02 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0002_remove_enterprise_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
