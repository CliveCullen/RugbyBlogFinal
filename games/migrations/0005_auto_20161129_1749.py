# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20161129_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overall',
            name='location',
            field=models.TextField(max_length=50),
        ),
    ]
