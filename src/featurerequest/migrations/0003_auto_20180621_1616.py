# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-21 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('featurerequest', '0002_auto_20180621_1355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='features',
            options={'verbose_name_plural': 'features'},
        ),
        migrations.AddField(
            model_name='features',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
