# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-18 09:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('azapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=60)),
                ('activity_image', models.ImageField(upload_to='activity/')),
                ('price', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('partner_image', models.ImageField(upload_to='partner/')),
            ],
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='child',
        ),
        migrations.DeleteModel(
            name='Trainer',
        ),
        migrations.AddField(
            model_name='activities',
            name='partner_image',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='azapp.Partners'),
        ),
    ]
