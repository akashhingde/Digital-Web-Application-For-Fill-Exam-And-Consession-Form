# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-16 07:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0034_auto_20190316_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examform',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.UserProfileModel'),
        ),
    ]
