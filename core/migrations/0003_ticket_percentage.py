# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-22 03:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160821_0537'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='percentage',
            field=models.IntegerField(default=0),
        ),
    ]