# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0013_standardfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='customform',
            name='type_pattern',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
