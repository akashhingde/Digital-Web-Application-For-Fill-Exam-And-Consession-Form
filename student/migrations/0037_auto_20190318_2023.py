# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-18 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0036_auto_20190316_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='mobile_no',
            field=models.IntegerField(default=0, max_length=10, null=True),
        ),
    ]
