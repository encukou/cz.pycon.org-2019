# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-07 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0003_auto_20190406_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='has_detail',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='talk',
            name='in_data_track',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='workshop',
            name='has_detail',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='workshop',
            name='in_data_track',
            field=models.BooleanField(default=False),
        ),
    ]