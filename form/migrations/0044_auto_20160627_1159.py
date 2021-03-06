# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 06:29
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('form', '0043_auto_20160626_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='highlighted',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='snippet',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 11, 59, 10, 756792)),
        ),
    ]
