# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 13:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0035_auto_20160625_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionanswer',
            old_name='unix_timestamp',
            new_name='timestamp',
        ),
    ]