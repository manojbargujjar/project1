# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-04 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='usr',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]