# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0009_auto_20160621_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='optionchoice',
            name='label_to_show',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
