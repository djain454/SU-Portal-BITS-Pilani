# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-02-03 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('su', '0016_auto_20190204_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='meal',
            field=models.CharField(choices=[('Workshop', 'Workshop'), ('Prof Show', 'Prof Show'), ('Other', 'Other')], default='Workshop', max_length=16, verbose_name='Event Type'),
        ),
    ]
