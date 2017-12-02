# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0006_auto_20171201_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_table',
            name='recentdate',
            field=models.DateField(default=datetime.date(2017, 12, 2)),
        ),
        migrations.AlterField(
            model_name='experience_internship',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 2, 10, 43, 42, 773000)),
        ),
        migrations.AlterField(
            model_name='experience_placement',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 2, 10, 43, 42, 770000)),
        ),
        migrations.AlterField(
            model_name='forgotpasskeys',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 2, 10, 43, 42, 777000)),
        ),
        migrations.AlterField(
            model_name='personinformation',
            name='createdondate',
            field=models.DateField(default=datetime.date(2017, 12, 2)),
        ),
    ]
