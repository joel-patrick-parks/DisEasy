# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visualization',
            name='group',
        ),
        migrations.RemoveField(
            model_name='visualization',
            name='json',
        ),
        migrations.RemoveField(
            model_name='visualization',
            name='test',
        ),
        migrations.AddField(
            model_name='visualization',
            name='Data',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='visualization',
            name='FeatureType',
            field=models.CharField(db_index=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='visualization',
            name='FeatureValue',
            field=models.CharField(db_index=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='visualization',
            name='IV',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='visualization',
            name='UserProbability',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='visualization',
            name='UserResult',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
    ]
