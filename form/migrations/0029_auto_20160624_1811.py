# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 12:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0028_auto_20160624_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choiceanswer',
            name='choicequestion',
        ),
        migrations.RemoveField(
            model_name='optionchoice',
            name='choicequestion',
        ),
        migrations.DeleteModel(
            name='ChoiceAnswer',
        ),
        migrations.DeleteModel(
            name='OptionChoice',
        ),
    ]