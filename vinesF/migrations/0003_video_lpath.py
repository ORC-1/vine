# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-15 14:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vinesF', '0002_auto_20171206_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='LPath',
            field=models.FilePathField(default=datetime.datetime(2017, 12, 15, 14, 25, 9, 651000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
