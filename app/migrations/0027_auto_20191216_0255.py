# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-15 23:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20191215_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 12, 16, 2, 55, 2, 753021), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 12, 16, 2, 55, 2, 754007), verbose_name='Дата'),
        ),
    ]
