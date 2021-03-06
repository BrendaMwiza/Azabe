# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-02 07:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=300, null=True)),
                ('activity_image', models.ImageField(blank=True, null=True, upload_to='activity/')),
                ('price', models.CharField(max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, null=True)),
                ('content', tinymce.models.HTMLField(null=True)),
                ('time', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=60, null=True)),
                ('descriptions', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=60, null=True)),
                ('age', models.IntegerField()),
                ('activity_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='azapp.Activities')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_cont', models.CharField(max_length=120)),
                ('commented_act', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='azapp.Activities')),
            ],
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('biography', models.CharField(max_length=300)),
                ('noChild', models.IntegerField()),
                ('location', models.CharField(max_length=60, null=True)),
                ('email', models.CharField(max_length=60, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='parent/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=60, null=True)),
                ('description', models.CharField(max_length=300, null=True)),
                ('email', models.CharField(max_length=60, null=True)),
                ('partner_image', models.ImageField(null=True, upload_to='partner/')),
                ('approved', models.BooleanField(default=False)),
                ('phone', models.CharField(max_length=60, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, null=True)),
                ('description', models.CharField(max_length=60, null=True)),
                ('location', models.CharField(max_length=60, null=True)),
                ('time', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='commented_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='azapp.Parents'),
        ),
        migrations.AddField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='azapp.Parents'),
        ),
        migrations.AddField(
            model_name='activities',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='azapp.Categories'),
        ),
        migrations.AddField(
            model_name='activities',
            name='partner_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='azapp.Partners'),
        ),
    ]
