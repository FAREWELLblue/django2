# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-28 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0007_auto_20200328_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='是否活跃'),
        ),
    ]
