# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 07:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0025_auto_20160624_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='options',
            name='stype',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='form.StandardField'),
        ),
    ]