# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0008_auto_20170929_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_table',
            name='recentdate',
            field=models.DateField(default=datetime.date(2017, 10, 18)),
        ),
        migrations.AlterField(
            model_name='experience_internship',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 18, 18, 18, 40, 3000)),
        ),
        migrations.AlterField(
            model_name='experience_placement',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 18, 18, 18, 39, 988000)),
        ),
        migrations.AlterField(
            model_name='forgotpasskeys',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 18, 18, 18, 40, 3000)),
        ),
        migrations.AlterField(
            model_name='personinformation',
            name='createdondate',
            field=models.DateField(default=datetime.date(2017, 10, 18)),
        ),
    ]
