# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0003_auto_20171027_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_table',
            name='recentdate',
            field=models.DateField(default=datetime.date(2017, 12, 1)),
        ),
        migrations.AlterField(
            model_name='experience_internship',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 1, 1, 15, 6, 418000)),
        ),
        migrations.AlterField(
            model_name='experience_placement',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 1, 1, 15, 6, 418000)),
        ),
        migrations.AlterField(
            model_name='forgotpasskeys',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 1, 1, 15, 6, 418000)),
        ),
        migrations.AlterField(
            model_name='personinformation',
            name='createdondate',
            field=models.DateField(default=datetime.date(2017, 12, 1)),
        ),
    ]
