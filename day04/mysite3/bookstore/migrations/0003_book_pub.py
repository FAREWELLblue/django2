# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-28 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_book_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pub',
            field=models.CharField(default='', max_length=200, verbose_name='出版社'),
        ),
    ]
