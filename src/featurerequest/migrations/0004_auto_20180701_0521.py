# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-01 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('featurerequest', '0003_auto_20180621_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='target_date',
            field=models.DateField(),
        ),
    ]
