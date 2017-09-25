# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0002_auto_20170220_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience_internship',
            name='selected',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='experience_placement',
            name='selected',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='company_table',
            name='recentdate',
            field=models.DateField(default=datetime.date(2017, 3, 1)),
        ),
        migrations.AlterField(
            model_name='experience_internship',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 1, 17, 3, 56, 830382)),
        ),
        migrations.AlterField(
            model_name='experience_placement',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 1, 17, 3, 56, 828661)),
        ),
        migrations.AlterField(
            model_name='personinformation',
            name='createdondate',
            field=models.DateField(default=datetime.date(2017, 3, 1)),
        ),
    ]
