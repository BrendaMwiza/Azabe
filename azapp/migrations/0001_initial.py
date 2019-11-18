# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-17 15:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('noChild', models.IntegerField()),
                ('residence', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, null=True)),
                ('description', models.CharField(max_length=60, null=True)),
                ('location', models.CharField(max_length=60)),
                ('time', models.CharField(max_length=60)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('child', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='azapp.Child')),
            ],
        ),
        migrations.AddField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='azapp.Parents'),
        ),
    ]
