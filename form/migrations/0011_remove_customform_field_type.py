# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 09:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0010_optionchoice_label_to_show'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customform',
            name='field_type',
        ),
    ]
