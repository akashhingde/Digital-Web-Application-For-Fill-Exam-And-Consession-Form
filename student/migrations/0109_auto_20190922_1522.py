# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-09-22 09:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0108_auto_20190429_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Branch'),
        ),
        migrations.AddField(
            model_name='subject',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Year'),
        ),
    ]
