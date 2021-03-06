# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 08:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0052_auto_20160629_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='form.Question'),
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 29, 13, 55, 54, 453431)),
        ),
    ]
