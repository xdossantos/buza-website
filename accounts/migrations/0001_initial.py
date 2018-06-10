# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-10 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to=b'users/%Y/%m/%d')),
                ('school', models.CharField(blank=True, max_length=100, null=True)),
                ('interests', models.CharField(blank=True, max_length=300, null=True)),
                ('bio', models.CharField(blank=True, max_length=250, null=True)),
                ('grade', models.IntegerField(blank=True, default=7)),
                ('reputation', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
