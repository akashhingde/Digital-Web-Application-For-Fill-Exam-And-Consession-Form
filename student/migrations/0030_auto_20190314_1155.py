# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-14 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0029_auto_20190313_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='examform',
            name='admission_no',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='examform',
            name='branch',
            field=models.CharField(max_length=100, null=True),
        ),
    ]