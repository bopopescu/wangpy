# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-26 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name=b'id')),
                ('name', models.CharField(max_length=50, verbose_name=b'name')),
                ('weight', models.CharField(max_length=20, verbose_name=b'weight')),
                ('size', models.CharField(max_length=20, verbose_name=b'size')),
            ],
        ),
    ]