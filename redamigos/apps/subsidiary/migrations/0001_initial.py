# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-01 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enterprise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subsidiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='edition date', null=True)),
                ('town', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='templates/images/picture/')),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('user', models.CharField(max_length=150)),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enterprise', to='enterprise.Enterprise')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
