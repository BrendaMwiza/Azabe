# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-04 10:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('azapp', '0002_blog_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partners',
            name='email',
        ),
    ]