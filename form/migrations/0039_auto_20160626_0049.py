# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 19:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0038_auto_20160625_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionanswer',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 26, 0, 49, 58, 644800)),
        ),
    ]
