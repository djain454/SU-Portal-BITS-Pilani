# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-02-01 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('su', '0011_auto_20190201_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wear_student',
            name='meal',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')], default='S', max_length=16, verbose_name='Size Selected'),
        ),
    ]