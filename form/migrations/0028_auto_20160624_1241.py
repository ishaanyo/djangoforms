# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 07:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0027_auto_20160624_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='options',
            old_name='ytype',
            new_name='stype',
        ),
    ]
