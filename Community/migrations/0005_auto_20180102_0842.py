# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-02 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Community', '0004_suggestcommunity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestcommunity',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
