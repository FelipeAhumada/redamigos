# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-02 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0001_initial'),
        ('chip', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChipDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='edition date', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='chip',
            name='lccid',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='chipdelivery',
            name='chip',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chip_sale', to='chip.Chip'),
        ),
        migrations.AddField(
            model_name='chipdelivery',
            name='delivery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_sale', to='deliveries.Delivery'),
        ),
    ]
