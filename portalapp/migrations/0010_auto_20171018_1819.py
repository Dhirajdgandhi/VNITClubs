# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0009_auto_20171018_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience_internship',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 18, 18, 19, 47, 553000)),
        ),
        migrations.AlterField(
            model_name='experience_placement',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 18, 18, 19, 47, 550000)),
        ),
        migrations.AlterField(
            model_name='forgotpasskeys',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 18, 18, 19, 47, 556000)),
        ),
    ]
