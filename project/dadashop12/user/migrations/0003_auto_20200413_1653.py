# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-04-13 08:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 13, 8, 53, 26, 416572, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='updated_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 13, 8, 53, 26, 416679, tzinfo=utc)),
        ),
    ]
