# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_auto_20160621_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_answer',
        ),
        migrations.AlterField(
            model_name='choiceanswer',
            name='choice_answer',
            field=models.CharField(default='', max_length=2000),
        ),
    ]