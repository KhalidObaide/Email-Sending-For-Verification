# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-09-30 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=500000)),
                ('very', models.CharField(max_length=500000)),
            ],
        ),
    ]
