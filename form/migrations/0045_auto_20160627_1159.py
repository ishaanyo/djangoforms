# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 06:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0044_auto_20160627_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionanswer',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 11, 59, 48, 115660)),
        ),
    ]