# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-12-03 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
