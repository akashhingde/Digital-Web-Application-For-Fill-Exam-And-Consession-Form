# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-20 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0087_remove_consessionformmodel_to_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='consessionformmodel',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
