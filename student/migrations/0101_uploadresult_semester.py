# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-25 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0100_auto_20190425_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadresult',
            name='semester',
            field=models.CharField(choices=[('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI')], max_length=200, null=True),
        ),
    ]
