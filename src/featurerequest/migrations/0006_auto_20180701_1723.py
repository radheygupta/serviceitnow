# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-01 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('featurerequest', '0005_auto_20180701_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='enddate',
            field=models.DateField(),
        ),
    ]
