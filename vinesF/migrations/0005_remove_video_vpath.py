# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-20 12:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinesF', '0004_auto_20171215_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='VPath',
        ),
    ]
