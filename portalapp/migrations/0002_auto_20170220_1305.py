# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_table',
            name='recentdate',
            field=models.DateField(default=datetime.date(2017, 2, 20)),
        ),
        migrations.AlterField(
            model_name='company_table',
            name='startdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='experience_internship',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 13, 5, 5, 720387)),
        ),
        migrations.AlterField(
            model_name='experience_placement',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 13, 5, 5, 718718)),
        ),
        migrations.AlterField(
            model_name='personinformation',
            name='createdondate',
            field=models.DateField(default=datetime.date(2017, 2, 20)),
        ),
        migrations.AlterField(
            model_name='personinformation',
            name='is_active',
            field=models.IntegerField(default=1),
        ),
    ]
