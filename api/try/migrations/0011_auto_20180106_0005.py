# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-06 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('try', '0010_auto_20180105_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='compony',
        ),
        migrations.AddField(
            model_name='users',
            name='compony',
            field=models.ManyToManyField(null=True, to='try.compony'),
        ),
    ]
