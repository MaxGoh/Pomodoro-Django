# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-24 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20160824_0442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='creator',
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]