# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-02-01 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('su', '0012_auto_20190201_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='price',
        ),
        migrations.RemoveField(
            model_name='wear',
            name='price',
        ),
        migrations.AddField(
            model_name='event_student',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='wear_student',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Price'),
        ),
    ]