# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 09:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0021_auto_20160623_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='ftype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Question'),
        ),
    ]
