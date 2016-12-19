# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-19 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('host', models.TextField()),
                ('teamA', models.TextField()),
                ('teamB', models.TextField()),
                ('scoreA', models.IntegerField()),
                ('scoreB', models.IntegerField()),
                ('competition', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamA', models.TextField()),
                ('teamB', models.TextField()),
                ('wonByTeamA', models.IntegerField()),
                ('wonByTeamB', models.IntegerField()),
                ('drawn', models.IntegerField()),
                ('teamAPoints', models.IntegerField()),
                ('teamBPoints', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='teams',
            new_name='team',
        ),
        migrations.DeleteModel(
            name='games',
        ),
    ]