# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-10 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duration',
            name='total_second',
            field=models.IntegerField(blank=True),
        ),
    ]
