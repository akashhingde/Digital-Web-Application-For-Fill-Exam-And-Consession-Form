# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-19 19:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0072_auto_20190417_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='subject_name',
        ),
        migrations.AddField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Semester'),
        ),
    ]
