# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-27 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='icon',
        ),
        migrations.AlterField(
            model_name='activities',
            name='activity_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='activities',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]