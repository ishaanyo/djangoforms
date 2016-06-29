# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 13:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_auto_20160621_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Createlink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_link', models.CharField(blank=True, max_length=2000)),
                ('customform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.CustomForm')),
            ],
        ),
    ]