# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-30 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0009_auto_20200328_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='', max_length=50, primary_key=True, verbose_name='书名'),
        ),
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
    ]
