# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-09 02:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20191209_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 12, 9, 5, 20, 37, 802724), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 12, 9, 5, 20, 37, 803725), verbose_name='Дата'),
        ),
    ]