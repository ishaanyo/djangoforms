# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 08:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0017_auto_20160623_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ftype',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='form.Question'),
        ),
    ]