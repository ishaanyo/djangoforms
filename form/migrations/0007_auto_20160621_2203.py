# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_createlink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createform',
            name='accounts',
        ),
        migrations.RemoveField(
            model_name='customform',
            name='createform',
        ),
        migrations.AddField(
            model_name='customform',
            name='accounts',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='form.Accounts'),
        ),
        migrations.DeleteModel(
            name='CreateForm',
        ),
    ]
