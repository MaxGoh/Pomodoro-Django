# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-01 11:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20160901_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 9, 1, 11, 51, 49, 195478, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
