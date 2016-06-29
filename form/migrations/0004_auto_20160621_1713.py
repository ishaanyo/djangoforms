# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_choiceanswer_questionanswer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionanswer',
            old_name='answer',
            new_name='question_answer',
        ),
        migrations.RemoveField(
            model_name='choicequestion',
            name='choice_answer_text',
        ),
        migrations.AddField(
            model_name='choiceanswer',
            name='choice_answer',
            field=models.CharField(default=2, max_length=2000),
            preserve_default=False,
        ),
    ]
