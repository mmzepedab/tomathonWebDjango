# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-09 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('facebook_id', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('points', models.CharField(max_length=200)),
                ('highest_score', models.CharField(max_length=200)),
            ],
        ),
    ]