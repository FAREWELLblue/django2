# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-31 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telnumber',
            field=models.CharField(max_length=11),
        ),
    ]