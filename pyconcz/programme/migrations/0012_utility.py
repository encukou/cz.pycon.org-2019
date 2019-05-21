# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-20 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0011_auto_20190508_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Utility',
                'verbose_name_plural': 'Utilities',
            },
        ),
    ]