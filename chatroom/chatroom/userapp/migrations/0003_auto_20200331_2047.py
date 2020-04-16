# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-31 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_auto_20200331_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=32, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='telnumber',
            field=models.CharField(max_length=11, verbose_name='手机号码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True, verbose_name='用户名'),
        ),
    ]
