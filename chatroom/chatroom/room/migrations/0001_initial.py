# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-31 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0003_auto_20200331_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomname', models.CharField(max_length=50, unique=True, verbose_name='聊天室名称')),
                ('introduce', models.TextField(verbose_name='聊天室简介')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.User')),
            ],
        ),
    ]
